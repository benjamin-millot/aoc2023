class Draw:
    """A draw is a set of balls that can be drawn from a bag."""

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        """Initializes a draw with the given number of balls of each color."""
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
    
    def check_if_draw_possible(self, red: int, green: int, blue: int) -> bool:
        """Checks if the draw is possible with the given number of balls of each color."""
        return self.red <= red and self.green <= green and self.blue <= blue

class Game:
    """A game is a set of draws that can be played in a row."""

    def __init__(self, n):
        """Initializes a game with the given number."""
        self.n: int = n
        self.draws: list[Draw] = []

    def add_draw(self, draw: Draw):
        """Adds a draw to the game."""
        self.draws.append(draw)
    
    def check_if_game_possible(self, max: Draw) -> bool:
        """Checks if the game is possible with the given number of balls of each color."""
        for draw in self.draws:
            if not draw.check_if_draw_possible(max.red, max.green, max.blue):
                return False
        return True

    def get_minimal_draw(self) -> Draw:
        """Gets the minimal draw required to make the game possible."""
        minimal_draw = Draw(red=0, green=0, blue=0)
        for draw in self.draws:
            minimal_draw.red = max(draw.red, minimal_draw.red)
            minimal_draw.green = max(draw.green, minimal_draw.green)
            minimal_draw.blue = max(draw.blue, minimal_draw.blue)
        return minimal_draw

    def get_game_power(self) -> int:
        """Gets the game power of the game."""
        minimal_draw = self.get_minimal_draw()
        return minimal_draw.red * minimal_draw.green * minimal_draw.blue

def parse_game(line: str):
    """Parses a game from the given line."""
    parse_on_colon = line.split(":", maxsplit=1)

    game = Game(n=int(parse_on_colon[0].removeprefix("Game ")))
    
    draws = parse_on_colon[1].split(";")
    for draw in draws:
        balls = draw.split(",")

        n_red: int = 0
        n_blue: int = 0
        n_green: int = 0

        for ball in balls:
            n_balls, color = ball.lstrip(" ").split(" ")
            if color == "red":
                n_red = int(n_balls)
            elif color == "blue":
                n_blue = int(n_balls)
            elif color == "green":
                n_green = int(n_balls)
            else:
                raise ValueError("Unknown color: {0}".format(color))
        game.add_draw(Draw(red=n_red, green=n_green, blue=n_blue))
    return game

if __name__ == "__main__":
    max_draw = Draw(red=12, green=13, blue=14)
    games: list[Game] = []
    
    with open("day_2/input.txt") as input_file:
        for line in input_file:
            games.append(parse_game(line.rstrip()))
    
    # Part 1 - Possible number of games with the given max draw
    total = 0
    for game in games:
        if game.check_if_game_possible(max_draw):
            total += game.n
    print("The summed IDs of games that can be played with {} red, {} green and {} blue balls is: {}".format(max_draw.red, max_draw.green, max_draw.blue, total))

    # Part 2 - Combined game power of all games with their minimal draw possible
    total = 0
    for game in games:
        total += game.get_game_power()
    print("The combined game power is: {}".format(total))