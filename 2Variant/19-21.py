from functools import lru_cache
# +1 or first*2 or second*3
# end >= 84
# 1 <= S <= 67


def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*3)


@lru_cache(None)
def game(h):
    if sum(h) >= 84:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)):
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"


for s in range(1, 68):
    if game((16, s)) is not None:
        print(s, game((16, s)))
