exec(open("cards3.py").read())


with open('strat_p1.out.txt', 'w') as strat1:
    for a in S:
        for b in S:
            strat1.write(f"(x, {a}, {b}) -> {m.evaluate(t1(a, b))}\n")


with open('strat_p2.out.txt', 'w') as strat2:
    for a in S:
        for b in S:
            strat2.write(f"({a}, x, {b}) -> {m.evaluate(t2(a, b))}\n")



with open('strat_p3.out.txt', 'w') as strat3:
    for a in S:
        for b in S:
            strat3.write(f"({a}, {b}, x) -> {m.evaluate(t3(a, b))}\n")
