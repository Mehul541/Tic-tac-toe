from math import e
import random
import tkinter
import sys

root=tkinter.Tk()
root.geometry('400x400')
root.title("Tic tac toe")

board=[['X' if i==4 else '%s'%(i) for i in range(j-3,j)]  for j in range(3,10,3)]

def linegen():
    print("|           "*3+"|")
     
def display():
    print("+-----------"*3+"+")
    for i in board:
        linegen()
        for j in i:
            if j in ('X','O'):
                print("|    ",j,"    ",end="")
            else:
                print("|           ",end="")
        print("|")
        linegen()
        print("+-----------"*3+"+")
        

def user():
    i=j=0
    try:
        num=int(input("Enter a position:"))-1
        if num<3:
            i=0
            j=num
        elif num in range(3,6):
            i=1
            j=num-3
        elif num in range(6,9):
            i=2
            j=num-6
        else:
            print("Wrong position.\nPlease enter again.")
            user()
        if board[i][j] in ('X','O'):
            print("Position already occupied.\nPlease enter again.")
            user()
        else:
            board[i][j]='O'
        result()
        filled()
    except ValueError:
        print("Enter an integer")
        user()
        
def comp():
    i=j=0
    num=random.randint(0,10)
    if num<3:
        i=0
        j=num
    elif num in range(3,6):
        i=1
        j=num-3
    elif num in range(6,9):
        i=2
        j=num-6
    if board[i][j] in ('X','O'):
        comp()
    else:
        board[i][j]='X'
    result()
    filled()

def result():
    count=0
    for i in range(3):
        if board[i][i] in ('X'):
            count+=1
    if count==3:
        display()
        print("Computer won.")
        sys.exit()  

    count=0
    for j in range(3):
        if board[j][j] in ('O'):
            count+=1
    if count==3:
        display()
        print("You won.")
        sys.exit()


def filled():
    count=0
    for i in board:
        for j in i:
            if j in ('X','O'):
                count+=1 
    if count==9:
        display()
        print("Game over.")
        sys.exit()
    else:
        return False


def control():
    display()
    while(True):
        user()
        display()
        comp()
        display()

control()