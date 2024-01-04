import turtle

screen= turtle.Screen()
screen.setup(height=750, width=1350)
screen.title(2024)
screen.bgcolor("gray")

pen1=turtle.Turtle()
pen1.up()
pen1.goto( -620, 300)
pen1.down()

pen1.speed(0)


#________________H_________________________

def height_right():
    pen1.right(90)
    pen1.forward(160)

def height_left():
    pen1.left(90)
    pen1.forward(160)


def weight_right():
    pen1.right(90)
    pen1.forward(50)

def weight_left():
    pen1.left(90)
    pen1.forward(50)


def half_right():
    pen1.right(90)
    pen1.forward(60)

def half_left():
    pen1.left(90)
    pen1.forward(60)


def H_half_part():
    weight_left()
    half_left()
    weight_right()
    half_right()
    weight_left()

pen1.fillcolor("#6568fa")
pen1.begin_fill()

height_right()

H_half_part()

height_left()

H_half_part()
pen1.end_fill()


#________________A_________________________


pen1.up()
pen1.goto( -360, 300)
pen1.down()


def A_height_120_right():
    pen1.right(120)
    pen1.backward(178)

def A_height_60_right():
    pen1.right(60)
    pen1.backward(178)


def weight_60_deg_right():
    pen1.right(60)
    pen1.forward(50)

def weight_60_deg_left():
    pen1.left(60)
    pen1.forward(50)

def weight_120_deg_right():
    pen1.right(120)
    pen1.forward(33)


def half_60_deg_left():
    pen1.left(60)
    pen1.forward(60)

def half_60_deg_right():
    pen1.right(60)
    pen1.forward(60)


pen1.fillcolor("#7476ff")
pen1.begin_fill()


A_height_120_right()
weight_60_deg_right()
half_60_deg_left()

weight_60_deg_right()
half_60_deg_right()
weight_60_deg_left()

A_height_60_right()
weight_120_deg_right()

# triangle inside "A"
pen1.up()
pen1.goto( -360, 230)
pen1.down()

for x in range(3):
    pen1.right(120)
    pen1.forward(30)

pen1.end_fill()

#________________First "P"________________________


pen1.penup()
pen1.goto(-220, 300)
pen1.down()

def P_width_right():
    pen1.right(90)
    pen1.forward(80)

def P_width_left():
    pen1.left(90)
    pen1.forward(100)

def P_upper_width():
    pen1.left(90)
    pen1.forward(130)

pen1.fillcolor("#8385f9")
pen1.begin_fill()

#___calling function__
height_left()
weight_left()
half_left()
P_width_right()
P_width_left()
P_upper_width()

pen1.end_fill()


#______square b/w "p"_______

pen1.fillcolor("black")
pen1.begin_fill()

pen1.penup()
pen1.goto(-170,270)
pen1.down()

for s in range(4):
    pen1.left(90)
    pen1.forward(35)

pen1.end_fill()


#________________second "P"________________________

pen1.penup()
pen1.goto(-50, 300)
pen1.down()

pen1.fillcolor("#8e8ff5")
pen1.begin_fill()

#___calling function__
height_left()
weight_left()
half_left()
P_width_right()
P_width_left()
P_upper_width()

pen1.end_fill()

#______square b/w "p"_______


pen1.fillcolor("black")
pen1.begin_fill()

pen1.penup()
pen1.goto(-0,270)
pen1.down()

for y in range(4):
    pen1.left(90)
    pen1.forward(35)

pen1.end_fill()


#________________"Y"________________________


pen1.penup()
pen1.goto(110, 300)
pen1.down()


def Y_half_120_deg_left():
    pen1.left(120)
    pen1.forward(120)

def Y_half_30_deg_right():
    pen1.right(30)
    pen1.forward(120)

def Y_half_120_deg_right():
    pen1.right(120)
    pen1.forward(75)


def Y_60_deg_left():
    pen1.left(60)
    pen1.forward(75)

def Y_base_30_deg():
    pen1.right(30)
    pen1.forward(60)

def Y_base_90_deg():
    pen1.left(90)
    pen1.forward(60)

def Y_weight_120_deg_left():
    pen1.left(120)
    pen1.forward(50)


def Y_weight_60_deg_left():
    pen1.left(60)
    pen1.forward(45)


pen1.fillcolor("#9293ec")
pen1.begin_fill()

#____down________
Y_half_120_deg_left()
Y_base_30_deg()
weight_left()
#____top_______
Y_base_90_deg()
Y_half_30_deg_right()
Y_weight_120_deg_left()

#_____mid_down_____
Y_60_deg_left()
Y_half_120_deg_right()
Y_weight_60_deg_left()

pen1.end_fill()


#-------HAPPY ** (DONE)-----------

#------NEW ** (Started)--------

pen1.up()
pen1.goto(-620,100)
pen1.down()

#----------------------N-------------------

def N_side_90_left():
    pen1.left(90)
    pen1.forward(110)


def N_side_90_left_top():
    pen1.left(90)
    pen1.forward(90)

def N_30_left():
    pen1.right(150)
    pen1.forward(126)

def N_60_deg_left():
    pen1.left(60)
    pen1.forward(50)

def N_60_deg_right():
    pen1.right(150)
    pen1.forward(105)


def N_weight_60_deg_left():
    pen1.left(60)
    pen1.forward(62)

pen1.fillcolor("#ff6666")
pen1.begin_fill()
#---down----
height_left()
weight_left()
N_side_90_left()

#___Up_____
N_30_left()
N_60_deg_left()
height_left()

#_____TOP____
weight_left()
N_side_90_left_top()
N_60_deg_right()
N_weight_60_deg_left()

pen1.end_fill()

#----------------------"E"-------------------------

pen1.up()
pen1.goto(-420,100)
pen1.down()


def E_weight_left():
    pen1.left(90)
    pen1.forward(100)

def E_mid_width_left():
    pen1.left(90)
    pen1.forward(60)

def E_mid_width_right():
    pen1.right(90)
    pen1.forward(60)

def E_mid_weight_left():
    pen1.left(90)
    pen1.forward(32)

def E_mid_weight_right():
    pen1.right(90)
    pen1.forward(32)


pen1.fillcolor("#ff8080")
pen1.begin_fill()

height_left()
E_weight_left()

for x in range(2):
    E_mid_weight_left()
    E_mid_width_left()
    E_mid_weight_right()
    E_mid_width_right()

E_mid_weight_left()
E_weight_left()

pen1.end_fill()

#----------------"W"-----------------------

pen1.up()
pen1.goto(-290,100)
pen1.down()



def W_side_120_deg_left():
    pen1.left(110)
    pen1.forward(170)

def W_side_70_deg_left():
    pen1.left(70)
    pen1.forward(170)



def half_60_deg_left():
    pen1.left(70)
    pen1.forward(120)


def W_weight():
    pen1.left(70)
    pen1.forward(50)

def half_60_deg_right():
    pen1.right(140)
    pen1.forward(120)


def W_weight_120_deg_left():
    pen1.left(110)
    pen1.forward(50)


def W_half_140_deg_right():
    pen1.right(140)
    pen1.forward(100)


def W_70_deg_left():
    pen1.left(70)
    pen1.forward(100)


def W_weight_70_deg_left():
    pen1.left(70)
    pen1.forward(56)


pen1.fillcolor("#ff9999")
pen1.begin_fill()

W_side_120_deg_left()
W_weight()
half_60_deg_left()
half_60_deg_right()
W_weight()

W_side_70_deg_left()
W_weight_120_deg_left()

for w in range(2):
    W_70_deg_left()
    W_half_140_deg_right()
    W_weight_70_deg_left()

pen1.end_fill()

#----------------YEAR-----------------------

pen1.up()
pen1.goto( -620, -100)
pen1.down()

#----------------"Y"-----------------------

pen1.fillcolor("#4dff88")
pen1.begin_fill()

#____down________
Y_half_120_deg_left()
Y_base_30_deg()
weight_left()
#____top_______
Y_base_90_deg()
Y_half_30_deg_right()
Y_weight_120_deg_left()

#_____mid_down_____
Y_60_deg_left()
Y_half_120_deg_right()
Y_weight_60_deg_left()

pen1.end_fill()

#----------------"E"-----------------------

pen1.up()
pen1.goto( -430, -100)
pen1.down()


pen1.fillcolor("#66ff99")
pen1.begin_fill()

height_left()
E_weight_left()

for x in range(2):
    E_mid_weight_left()
    E_mid_width_left()
    E_mid_weight_right()
    E_mid_width_right()

E_mid_weight_left()
E_weight_left()

pen1.end_fill()


#----------------"A"-----------------------

pen1.up()
pen1.goto( -220, -100)
pen1.down()


def A_height_120_right():
    pen1.right(120)
    pen1.backward(178)

def A_height_60_right():
    pen1.right(60)
    pen1.backward(178)

def weight_60_deg_right():
    pen1.right(60)
    pen1.forward(50)

def weight_60_deg_left():
    pen1.left(60)
    pen1.forward(50)

def weight_120_deg_right():
    pen1.right(120)
    pen1.forward(33)


def half_60_deg_left():
    pen1.left(60)
    pen1.forward(60)

def half_60_deg_right():
    pen1.right(60)
    pen1.forward(60)


pen1.fillcolor("#80ffaa")
pen1.begin_fill()


A_height_120_right()
weight_60_deg_right()
half_60_deg_left()

weight_60_deg_right()
half_60_deg_right()
weight_60_deg_left()

A_height_60_right()
weight_120_deg_right()


# triangle inside "A"
pen1.up()
pen1.goto( -220, -170)
pen1.down()

for x in range(3):
    pen1.right(120)
    pen1.forward(30)

pen1.end_fill()


#----------------"R"-----------------------

pen1.up()
pen1.goto( -70, -100)
pen1.down()

def R_half_140_deg_right():
    pen1.right(140)
    pen1.forward(80)


def weight_50_deg_left():
    pen1.left(50)
    pen1.forward(50)

def R_height_60_right():
    pen1.right(50)
    pen1.backward(80)

def R_mid_left():
    pen1.left(50)
    pen1.forward(30)


pen1.fillcolor("#99ffbb")
pen1.begin_fill()

height_left()
weight_left()
half_left()
R_half_140_deg_right()
weight_50_deg_left()

R_height_60_right()
R_mid_left()
P_width_left()
P_upper_width()

pen1.end_fill()

#______square b/w "R"_______

pen1.penup()
pen1.goto( -20, -135)
pen1.down()

pen1.fillcolor("black")
pen1.begin_fill()

for y in range(4):
    pen1.left(90)
    pen1.forward(35)

pen1.end_fill()


#------------------------============::--:HAPPY NEEW YEAR:--::==============------------------------------

#------------------------2024------------------------------

#__________________2___________________
pen1.penup()
pen1.goto( 140, -110)
pen1.down()
pen1.width(25)
pen1.color("red")

pen1.left(180)
def make2():
    for x in range(3):
        pen1.forward(65)
        pen1.right(90)

    pen1.left(180)
    for x in range(2):
        pen1.forward(65)
        pen1.left(90)

make2()

#__________________0___________________
pen1.penup()
pen1.goto( 250, -110)
pen1.down()

for x in range(2):
    pen1.right(90)
    pen1.forward(65)
    pen1.right(90)
    pen1.forward(130)


#__________________2___________________
pen1.penup()
pen1.goto( 360, -110)
pen1.down()

pen1.right(90)
#_________function call________________
make2()


#__________________4___________________
pen1.up()
pen1.goto(480,-110)
pen1.down()

pen1.left(180)
for x in range(3):
    pen1.forward(65)
    pen1.left(90)

pen1.left(90)
pen1.forward(130)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BORDER DESIGN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-----------------Upper--------------
border=turtle.Turtle()

border.up()
border.goto( -675, 360)
border.down()
border.speed(0)


def design():
    border.right(60)
    border.forward(50)
    border.left(120)
    border.forward(50)
    border.right(60)
    border.forward(50)

for d in range(7):
    border.fillcolor("red")
    border.begin_fill()
    design()
    border.end_fill()
    border.fillcolor("white")
    border.begin_fill()
    design()
    border.end_fill()

border.width(2)
border.color("white")

border.left(180)
border.forward(1450)

#-----------------lower--------------
border.up()
border.goto( -680, -300)
border.down()
border.speed(0)

border.color("black")
border.width(1)
border.left(180)

def down_design():
    for down in range(70):
        border.left(60)
        border.forward(10)
        border.right(120)
        border.forward(10)
        border.left(60)
        border.forward(10)


def down_border_weight():
    border.right(90)
    border.forward(20)

border.fillcolor("yellow")
border.begin_fill()

down_design()
down_border_weight()
border.right(90)
down_design()
down_border_weight()
border.end_fill()
#-----------background color------------
screen.bgcolor("black")

#+++++++++++++++++++star++++++++++++++++++++++

star=turtle.Turtle()
star.speed(0)

def gold_star():
    star.fillcolor("gold")
    star.begin_fill()
    for l in range(5):
        star.forward(15)
        star.right(122)
        star.forward(15)
        star.left(50)
    star.end_fill()


star.up()
star.goto(400,250)
star.down()
gold_star()

star.up()
star.goto(550, 220)
star.down()
gold_star()

star.up()
star.goto(310, 110)
star.down()
gold_star()


star.up()
star.goto(600, 110)
star.down()
gold_star()


star.up()
star.goto(450, 100)
star.down()
gold_star()


star.up()
star.goto(400, -20)
star.down()
gold_star()

star.up()
star.goto(560, 10)
star.down()
gold_star()
#-----------hide_turtle------
star.hideturtle()
pen1.hideturtle()

screen.exitonclick()