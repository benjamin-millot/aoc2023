
class Card:
    """A card in the game."""

    def __repr__(self) -> str:
        return "Card {}".format(self.n)

    def __init__(self, n: int, winning: set[int], draw: set[int]) -> None:
        """Initialize a card with its number, winning and draw numbers."""
        self.n: int = n
        self.winning: set[int] = winning
        self.draw: set[int] = draw

    def get_commons(self) -> set[int]:
        """Return the set of common numbers between winning and draw."""
        return self.winning.intersection(self.draw)

    def get_worth(self) -> int:
        """Return the worth of the card."""
        worth = 0
        n_commons = len(self.get_commons())
        for i in range(n_commons):
            if i == 0:
                worth += 1
            else:
                worth *= 2
        return worth

class SameCard:
    """Multiple copies of the same card."""

    def __repr__(self) -> str:
        """Return a string representation of one or more of the same card."""
        return "{} copy of card {}".format(self.n, self.card.n)

    def __init__(self, card: Card, n: int = 1) -> None:
        """Initialize a card with its value and the number of copy."""
        self.n: int = n
        self.card: Card = card
    
    def add_card(self) -> None:
        """Add a copy to the pool the card."""
        self.n += 1
    
def parse_game(line: str):
    """Parse a line of the input file."""
    a = line.split(":", maxsplit=1)
    b = [x.split() for x in a[1].strip().split(" | ")]
    return Card(n=int(a[0].removeprefix("Card ")), winning=set(b[0]), draw=set(b[1]))


if __name__ == "__main__":
    # Part 1 - Get the combined worth of all cards
    with open("day_4/input.txt") as input_file:
        total = 0
        for line in input_file:
            card = parse_game(line.rstrip())
            total += card.get_worth()
        print("The total worth of all cards is {}".format(total))

    # Part 2 - Compute the sum of the number of copies of the same card
    with open("day_4/input.txt") as input_file:
        copies: list[SameCard] = []
        for line in input_file:
            card = parse_game(line.rstrip())
            copies.append(SameCard(card=card))
        
        for i, copy in enumerate(copies):
            next_cards_to_add = len(copy.card.get_commons())
            for n_cards in range(copy.n):
                for j in copies[i+1: i+next_cards_to_add+1]:
                    j.add_card()
        
        total = 0
        for c in copies:
            total += c.n
        print("The sum of the number of copies of the same card is {}".format(total))

