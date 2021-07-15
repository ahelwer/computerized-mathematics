exec(open("cards4.py").read())

for a in S:
    for b in S:
        for c in S:
            print(f"(x, {a}, {b}, {c}) -> {m.evaluate(t1(a, b, c))}")
