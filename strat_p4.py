exec(open("cards4.py").read())

for a in S:
    for b in S:
        for c in S:
            print(f"({a}, {b}, {c}, x) -> {m.evaluate(t4(a, b, c))}")
