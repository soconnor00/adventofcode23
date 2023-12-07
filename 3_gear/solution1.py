# Heavily inspired by https://www.reddit.com/r/adventofcode/comments/189m3qw/comment/kbs9g3g/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import re

def main():
    total = 0
    with open('input.txt', 'r') as f:
        data = list(f)
        num_rows, num_columns = len(data), len(data[0]) - 1
        # Get locations of all symbols on board, 
        # and create arrays to hold their part numbers
        symbols = {
            (r, c): [] 
            for r in range(num_rows) 
            for c in range(num_columns) 
            if data[r][c] not in '0123456789.'
        }
        # Find all part numbers on board 
        # and add them to their part arrays 
        # (if they have one)
        for r, row in enumerate(data):
            for n in re.finditer(r'\d+', row):
                border = {
                    (r, c) 
                    for r in (r - 1, r, r + 1)
                    for c in range(n.start() - 1, n.end() + 1)
                }
                for symbol in border & symbols.keys():
                    symbols[symbol].append(int(n.group()))
    # Add up all part numbers that were added to part arrays
    total = sum(
        sum(part_numbers) 
        for part_numbers in symbols.values()
    )
    print(total)

if __name__ == "__main__":
    main()