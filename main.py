######################
##### LIBRAIRIES #####
######################

import turtle as t
from random import choice

######################
####### SETUP ########
######################

size = int(input('Thickness of the curve : '))
spd = int(input('Speed of the build of the curve : '))

t.up()
t.Screen().setup(1100, 650)
t.pensize(size)
t.speed(spd)
t.hideturtle()
t.bgcolor('#222222')
t.title("Curve of probability 50 ~~ 50 - CalouDev")
t.goto(-545, 0)
t.down()
t.begin_fill()

######################
####### MAIN #########
######################

first = False
red = blue = 0

for i in range(153):
	nbr = choice([0, 1])
	if nbr == 0:
		blue += 1
		down = False
		t.color('#138cc8')
		if first == False:
			t.left(45)
			t.forward(10)
			first += 1
			up = True

		elif first and up:
			t.forward(10)

		else:
			t.left(90)
			t.forward(10)
			up = True
	else:
		red += 1
		up = False
		t.color('#d83230')
		if first == False:
			t.right(45)
			t.forward(10)
			first += 1
			down = True 

		elif first and down:
			t.forward(10)

		else:
			t.right(90)
			t.forward(10)
			down = True

print('''____________________
| BLUE : {}        |
--------------------
| RED  : {}        |
--------------------'''.format(blue, red))

t.done()
