import re


def to_words(move: str) -> str:
    figures = {"K": "King", "Q": "Queen", "B": "Bishop", "R": "Rook", "N": "Knight"}

    res = ''

    if move == "O-O":
        res += f'A kingside castle'
        if '+' in move:  # dxa3+
            res += ', check'
            return f"{res}."
        if '#' in move:  # dxa3#
            res += ', checkmate'
            return f"{res}."
        else:
            return f"{res}."

    if move == "O-O-O":
        res += f'A queenside castle'
        if '+' in move:  # dxa3+
            res += ', check'
            return f"{res}."
        if '#' in move:  # dxa3#
            res += ', checkmate'
            return f"{res}."
        else:
            return f"{res}."

    if move[0].isupper() and move[1].isdigit():
        if 'x' in move:
            res = f'{figures[move[0]]} on rank {move[1]} moved to {move[3:5]} and captured'
            if '+' in move:  # Qa3+
                res += ', check'
                return f"{res}."
            if '#' in move:  # Qa3#
                res += ', checkmate'
                return f"{res}."
            else:
                return f"{res}."
        else:
            res = f'{figures[move[0]]} on rank {move[1]} moved to {move[2:4]}'
            if '+' in move:  # Qa3+
                res += ', check'
                return f"{res}."
            if '#' in move:  # Qa3#
                res += ', checkmate'
                return f"{res}."
            else:
                return f"{res}."

    if move[0].isupper() and (move[2].isdigit() or move[3].isdigit()):
        if move[1] == 'x':
            res = f'{figures[move[0]]} moved to {move[2:4]} and captured'  # Qxa3
            if '+' in move:  # Qa3+
                res += ', check'
                return f"{res}."
            if '#' in move:  # Qa3#
                res += ', checkmate'
                return f"{res}."
            else:
                return f"{res}."  # Qa3
        if move[1].islower() and move[2].islower() and move[1] != "x":
            if 'x' in move:
                res = f'{figures[move[0]]} on file {move[1]} moved to {move[3:5]} and captured'
                if '+' in move:
                    res += ', check'
                    return f"{res}."
                if '#' in move:
                    res += ', checkmate'
                    return f"{res}."
                else:
                    return f"{res}."
            else:
                res = f'{figures[move[0]]} on file {move[1]} moved to {move[2:4]}'
                if '+' in move:
                    res += ', check'
                    return f"{res}."
                if '#' in move:
                    res += ', checkmate'
                    return f"{res}."
                else:
                    return f"{res}."
        else:
            res = f'{figures[move[0]]} moved to {move[1:3]}'  # Qa3
            if '+' in move:  # Qa3+
                res += ', check'
                return f"{res}."
            if '#' in move:  # Qa3#
                res += ', checkmate'
                return f"{res}."
            else:
                return f"{res}."  # Qa3

    if move[0].isupper() and move[1] != 'x':
        if 'x' in move:
            res = f'{figures[move[0]]} on file {move[1]} moved to {move[3:5]} and captured'
            if '+' in move:
                res += ', check'
                return f"{res}."
            if '#' in move:
                res += ', checkmate'
                return f"{res}."
            else:
                return f"{res}."
        else:
            res = f'{figures[move[0]]} on file {move[1]} moved to {move[2:4]}'
            if '+' in move:
                res += ', check'
                return f"{res}."
            if '#' in move:
                res += ', checkmate'
                return f"{res}."
            else:
                return f"{res}."

    if '=' in move:
        res = f'Pawn moved to {move[:2]} and promoted to {figures[move[3]].lower()}'
        if '+' in move:  # dxa3+
            res += ', check'
            return f"{res}."
        if '#' in move:  # dxa3#
            res += ', checkmate'
            return f"{res}."
        else:
            return f"{res}."


    else:
        if move[1] == 'x':
            if 'e.p.' in move:
                res = f'Pawn moved to {move[2:4]}, capturing en passant'
                if '+' in move:  # dxa3+
                    res += ', check'
                    return f"{res}."
                if '#' in move:  # dxa3#
                    res += ', checkmate'
                    return f"{res}."
                else:
                    return f"{res}."
            else:
                res = f'Pawn moved to {move[2:4]} and captured'  # exa3
                if '+' in move:  # dxa3+
                    res += ', check'
                    return f"{res}."
                if '#' in move:  # dxa3#
                    res += ', checkmate'
                    return f"{res}."
                else:
                    return f"{res}."  # exa3
        else:
            res = f'Pawn moved to {move}'  # exa3
            if '+' in move:  # dxa3+
                res += ', check'
                return f"{res}."
            if '#' in move:  # dxa3#
                res += ', checkmate'
                return f"{res}."

            else:
                return f"{res}."  # exa3


print(to_words("N7xc3#"))
