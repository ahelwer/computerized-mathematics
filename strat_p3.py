exec(open("cards4.py").read())

for a in S:
    for b in S:
        for c in S:
            print(f"({a}, {b}, x, {c}) -> {m.evaluate(t3(a, b, c))}")
