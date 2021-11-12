from functools import lru_cache

# +1, *3
# 1 <= S <= 72
# end >= 79


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)


@lru_cache(None)
def game(h):
    if sum(h) >= 79:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)): # менять на ANY для 19-ого задания
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"


for s in range(1, 73):
    if game((6, s)) is not None:
        print(s, game((6, s)))
