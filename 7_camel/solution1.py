# heavily inspired by https://github.com/fuglede/adventofcode/blob/master/2023/day07/solutions.py

from collections import Counter

def hand_type(hand):
    # Counter extracts pretty much all the info we need from the hand
    counts = sorted(Counter(hand).values())
    match counts:
        # Five of a kind
        case *_, 5:
            return 7
        # Four of a kind
        case *_, 4:
            return 6
        # Full house
        case *_, 2, 3:
            return 5
        # Three of a kind
        case *_, 3:
            return 4
        # Two pair
        case *_, 2, 2:
            return 3
        # Two of a kind
        case *_, 2:
            return 2
        # High card
        case _:
            return 1

def sorted_hands(hands):
    return sorted(
        (
            hand_type(hand), *map("*23456789TJQKA".index, hand),
            int(bid)
        ) for hand, bid in hands
    )

def get_winnings(hands):
    return sum(
        rank * bid for rank, (*_, bid) in enumerate(
            sorted_hands(hands),
            1
        )
    )

def main():
    with open('input.txt', 'r') as f:
        data = f.read().strip()
        hands = [hand.split() for hand in data.split('\n')]
        print(get_winnings(hands))

if __name__ == "__main__":
    main()