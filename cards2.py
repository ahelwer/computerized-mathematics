from z3 import *

# create solver
s = Solver()

# Declare color data type,
# with two values, black and red
Color = Datatype('Color')
Color.declare('red')
Color.declare('black')
Color = Color.create()

# Both decision tables can be though of as a function
# that takes in a color and outputs a color

# (the last field is the output type)
#t1 is person 1's decision table
t1 = Function('t1', Color, Color)
#t2 is person 2's decision table
t2 = Function('t2', Color, Color)

#declare constants for later
# c1 is player 1's card (which they cannot see!)
c1 = Const('c1', Color)
c2 = Const('c2', Color)

#s.add( t1(c2) == c1 or t2(c1) == c2 )
s.add( ForAll(
    [c1, c2], #for all pairs for colors
    Or( #either:
        t1(c2) == c1, #player 1's decision based on player 2's card is equal to their own card
        t2(c1) == c2) #player 2's decision based on player 1's card is equal to their own card
    )
)

s.check() # make a model
# there are better ways to do this, probably
try:
    print(s.model())
except:
    print('unsat')
# This is the output:
# [t2 = [else -> Var(0)], t1 = [red -> black, else -> red]]

