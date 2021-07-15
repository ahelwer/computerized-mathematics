exec(open("cards4.py").read())

for a in S:
    for b in S:
        for c in S:
            print(f"({a}, x, {b}, {c}) -> {m.evaluate(t2(a, b, c))}")
