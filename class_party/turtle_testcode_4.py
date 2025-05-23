#test code of MollyAredtana
import turtle
import random;
import math;


def tree(branchLen, t):
    if branchLen > 5:


# BranchWidth
        width = branchLen / 10;
        t.width(width);

# Branch Color
        t.pencolor(0, 1.0 / math.pow(width + 1, 1.0 / 3), 0);# why it used the parameter 0 here? IF we use 0, will the whole function
            # is 0, 1.0 is the number of the color?                                                #be 1.0 directly?

# branchAngles
        right_angle = random.randrange(15, 45);# 如果是高于45度那树枝就向下长了
        left_angle = random.randrange(15, 45);

# Branch lengths
        leftLen = random.randrange(5, 15);
        rightLen = random.randrange(5, 15);

        t.forward(branchLen)
        t.right(right_angle);
        tree(branchLen - leftLen, t)
        t.left(right_angle + left_angle)
        tree(branchLen - rightLen, t)
        t.right(left_angle)

        t.penup();
        t.backward(branchLen)
        t.pendown();


def main():
    t = turtle.Turtle()

    t.speed(200)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()


    tree(75, t)
    myWin.exitonclick()

main()
