from z3 import *


s = Solver()



Suite = Datatype('Suite')
Suite.declare('clubs')
Suite.declare('spade')
Suite.declare('heart')
Suite = Suite.create()






t1 = Function('t1', Suite, Suite, Suite)
t2 = Function('t2', Suite, Suite, Suite)
t3 = Function('t3', Suite, Suite, Suite)



s1 = Const('c1', Suite)
s2 = Const('c2', Suite)
s3 = Const('c3', Suite)


s.add( ForAll(
    [s1, s2, s3], 
    Or( 
        t1(s2, s3) == s1,
        t2(s1, s3) == s2,
        t3(s1, s2) == s3,
    )
))

s.check() 

try:
    m = s.model()
    #print(m.evaluate(t4(Suite.spade, Suite.spade, Suite.spade)))
    #print(s.model()[0])
except:
    print('unsat')

S = [
    Suite.clubs,
    Suite.spade,
    Suite.heart
]
def game(p1, p2, p3):
    print("p\thas\tsays")
    print(f"p1\t{p1}\t{m.evaluate(t1(p2, p3))}")
    print(f"p2\t{p2}\t{m.evaluate(t2(p1, p3))}")
    print(f"p3\t{p3}\t{m.evaluate(t3(p1, p2))}")

#game(Suite.diam, Suite.spade, Suite.club, Suite.heart)
