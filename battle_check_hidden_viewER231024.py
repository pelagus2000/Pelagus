import random

class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.hits = 0
        self.positions = []

    def is_sunk(self):
        return self.hits >= self.length

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def add_ship(self, ship, start_row, start_col, orientation):
        if orientation == 'H':
            if start_col + ship.length > self.size:
                return False
            for i in range(ship.length):
                if self.grid[start_row][start_col + i] != '.':
                    return False
            for i in range(ship.length):
                ship.positions.append((start_row, start_col + i))
        elif orientation == 'V':
            if start_row + ship.length > self.size:
                return False
            for i in range(ship.length):
                if self.grid[start_row + i][start_col] != '.':
                    return False
            for i in range(ship.length):
                ship.positions.append((start_row + i, start_col))
        self.ships.append(ship)
        return True

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    def attack(self, row, col):
        if self.grid[row][col] == 'S':
            for ship in self.ships:
                if (row, col) in ship.positions:
                    ship.hits += 1
            self.grid[row][col] = 'H'
            return True
        elif self.grid[row][col] == '.':
            self.grid[row][col] = 'M'
            return False
        return None

class User:
    def __init__(self, name):
        self.name = name
        self.board = Board(6)

    def take_turn(self):
        while True:
            try:
                row = int(input(f"{self.name}, enter row (0-5): "))
                col = int(input(f"{self.name}, enter column (0-5): "))
                if 0 <= row < 6 and 0 <= col < 6:
                    return row, col
                else:
                    print("Invalid input. Please enter values between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

class AI(User):
    def take_turn(self):
        return random.randint(0, 5), random.randint(0, 5)

def main():
    player = User("Player")
    ai = AI("AI")

    player.board.add_ship(Ship("Battleship", 3), 0, 0, 'H')
    player.board.add_ship(Ship("Cruiser", 2), 3, 3, 'V')
    player.board.add_ship(Ship("Submarine", 2), 1, 4, 'V')
    player.board.add_ship(Ship("Destroyer1", 1), 2, 2, 'H')
    player.board.add_ship(Ship("Destroyer2", 1), 4, 0, 'H')
    player.board.add_ship(Ship("Destroyer3", 1), 5, 5, 'H')

    ai.board.add_ship(Ship("Battleship", 3), 1, 1, 'H')
    ai.board.add_ship(Ship("Cruiser", 2), 3, 3, 'V')
    ai.board.add_ship(Ship("Submarine", 2), 4, 4, 'H')
    ai.board.add_ship(Ship("Destroyer1", 1), 2, 1, 'H')
    ai.board.add_ship(Ship("Destroyer2", 1), 0, 5, 'H')
    ai.board.add_ship(Ship("Destroyer3", 1), 5, 3, 'H')

    while True:
        print("Player's Board:")
        player.board.display()
        print("AI's Board:")
        ai.board.display()

        row, col = player.take_turn()
        result = ai.board.attack(row, col)
        if result is True:
            print("Hit!")
        elif result is False:
            print("Miss!")
        else:
            print("Already attacked this position!")

        row, col = ai.take_turn()
        result = player.board.attack(row, col)
        if result is True:
            print("AI hit your ship!")
        elif result is False:
            print("AI missed!")
        else:
            print("AI already attacked this position!")

        if all(ship.is_sunk() for ship in player.board.ships):
            print("AI wins!")
            break
        elif all(ship.is_sunk() for ship in ai.board.ships):
            print("Player wins!")
            break

if __name__ == "__main__":
    main()