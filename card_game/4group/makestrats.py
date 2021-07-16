exec(open("cards4.py").read())


with open('strat_p1.out.txt', 'a') as strat1:
    for a in S:
        for b in S:
            for c in S:
                strat1.write(f"(x, {a}, {b}, {c}) -> {m.evaluate(t1(a, b, c))}\n")


with open('strat_p2.out.txt', 'a') as strat2:
    for a in S:
        for b in S:
            for c in S:
                strat2.write(f"({a}, x, {b}, {c}) -> {m.evaluate(t2(a, b, c))}\n")



with open('strat_p3.out.txt', 'a') as strat3:
    for a in S:
        for b in S:
            for c in S:
                strat3.write(f"({a}, {b}, x, {c}) -> {m.evaluate(t3(a, b, c))}\n")


with open('strat_p4.out.txt', 'a') as strat4:
    for a in S:
        for b in S:
            for c in S:
                strat4.write(f"({a}, {b}, {c}, x) -> {m.evaluate(t4(a, b, c))}\n")
