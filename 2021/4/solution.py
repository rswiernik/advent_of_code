import sys
from typing import List
from collections import defaultdict


class BingoBoard(object):
    def __init__(self,
                 id: int,
                 input_array: List[List[int]]):
        self.id = id
        size = len(input_array)
        self.board = input_array
        self.drawn = [
            [ False for _ in range(len(self.board))] for x in range(len(self.board))
        ]
        self._solved = False

    @staticmethod
    def _check_for_win(board) -> bool:
        for row in board:
            if all(row):
                return True
        return False

    def get_unmarked_total(self) -> int:
        total = 0
        row_pos = 0
        col_pos = 0
        for row in self.drawn:
            for col in row:
                if not col:
                    total += self.board[row_pos][col_pos]
                col_pos += 1
            col_pos = 0
            row_pos += 1
        return total

    def is_solved(self) -> bool:
        if self._solved:
            return self._solved
        for board in (
                self.drawn,
                list(map(list, zip(*self.drawn))),  # Transposition
                # [[ self.drawn[x][x] for x in range(len(self.drawn))]],
                # [[ self.drawn[x][(len(self.drawn)-1)-x] for x in range(len(self.drawn))]],
                ):
            if self._check_for_win(board):
                self._solved = True
                return self._solved
        return self._solved

    def play(self, number) -> None:
        row_pos = 0
        col_pos = 0
        for row in self.board:
            for col in row:
                if col == number:
                    self.drawn[row_pos][col_pos] = True
                col_pos += 1
            col_pos = 0
            row_pos += 1


# Part 1
def play_bingo(boards: List[BingoBoard], game_input: List[int]):
    print('Lets play Bingo!')
    for number in game_input:
        for board in boards:
            board.play(number)
            if board.is_solved():
                print('board {} wins!'.format(board.id))
                print('\n'.join(''.join(str(x)) for x in board.board))
                print()
                print('\n'.join(''.join(str(x)) for x in board.drawn))
                total = board.get_unmarked_total()
                print('{} * {} = {}'.format(
                    total,
                    number,
                    total * number,
                ))
                return


if __name__ == "__main__":
    in_file = sys.argv[1]

    board_id = 1
    boards = []  # type: List[BingoBoard]
    board_input = []
    game_input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                if not game_input:
                    game_input = [int(x) for x in line.strip().split(',')]
                    continue
                else:
                    board_input.append(
                        [
                            int(x) for x in \
                            list(line.strip().split())
                        ]
                    )
            else:
                if board_input:
                    boards.append(BingoBoard(board_id, board_input))
                    board_id += 1
                board_input = []
        if board_input:
            boards.append(BingoBoard(board_id, board_input))

    # Part 1
    play_bingo(boards, game_input)
