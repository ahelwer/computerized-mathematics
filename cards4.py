from z3 import *


s = Solver()



Suite = Datatype('Suite')
Suite.declare('club')
Suite.declare('spade')
Suite.declare('heart')
Suite.declare('diam')
Suite = Suite.create()






t1 = Function('t1', Suite, Suite, Suite, Suite)
t2 = Function('t2', Suite, Suite, Suite, Suite)
t3 = Function('t3', Suite, Suite, Suite, Suite)
t4 = Function('t4', Suite, Suite, Suite, Suite)



s1 = Const('c1', Suite)
s2 = Const('c2', Suite)
s3 = Const('c3', Suite)
s4 = Const('c4', Suite)


s.add( ForAll(
    [s1, s2, s3, s4], 
    Or( 
        t1(s2, s3, s4) == s1,
        t2(s1, s3, s4) == s2,
        t3(s2, s1, s4) == s3,
        t4(s2, s3, s1) == s4
    )
))

s.check() 

try:
    print(s.model())
except:
    print('unsat')



