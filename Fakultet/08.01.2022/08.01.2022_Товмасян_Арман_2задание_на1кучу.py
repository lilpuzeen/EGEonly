from functools import lru_cache
# №6
# 6 - 6
# 7 - 5 13 14
# 8 - 12

# +1, +2, *3
# 1 <= S <= 45
# end >= 46

def moves(h):
    return (h + 1), (h + 2), (h * 3)


@lru_cache(None)
def game(h):
    if h >= 46:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)):  # менять на ANY для 19-ого задания
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"


for s in range(1, 47):
    if game(s) is not None:
        print(s, game(s))
