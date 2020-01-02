from threading import Thread,Lock
import time
import os
import keyboard
from random import randint

input("Use w,s,a,d to play \npress enter to continue\n")

class globalVars():
    pass

G = globalVars() #empty object to pass around global state
G.lock = Lock() #not really necessary in this case, but useful none the less
G.value = 0
G.kill = False

G.b=21

G.board=[['0' for _ in range(G.b)]for __ in range(G.b)]

G.dx=1
G.dy=0

G.gameover=False

G.snake=[]

G.food=[]

# for _ in range(6):
#     G.snake.append([10,_+2])
G.snake.append([10,2])

def foodgen():
    f=[randint(0,G.b-1),randint(0,G.b-1)]
    if f in G.snake:
        foodgen()
    else:
        return f


def draw_snake():
    while True:
        if G.gameover:
            break
            # print("EXIT")
        else:
            G.board=[[' ' for _ in range(G.b)]for __ in range(G.b)]

            s=G.snake[0]
            # if [s[0]+G.dy,s[1]+G.dx] in G.snake:
            #     G.gameover=True

            # if G.snake[0] in G.snake[3:]:
            #     print("exit")
            #     G.gameover=True

            G.snake.insert(0,[s[0]+G.dy,s[1]+G.dx])
            G.snake=G.snake[:-1]

            if not len(G.food):
                G.food=foodgen()

            # G.snake[0][0]+=G.dy
            # G.snake[0][1]+=G.dx

            G.snake[0][0]=(0 if G.snake[0][0]==G.b else G.snake[0][0])
            G.snake[0][0]=(G.b-1 if G.snake[0][0]==-1 else G.snake[0][0])
            G.snake[0][1]=(0 if G.snake[0][1]==G.b else G.snake[0][1])
            G.snake[0][1]=(G.b-1 if G.snake[0][1]==-1 else G.snake[0][1])

            if G.snake[0]==G.food:
                G.food=foodgen()
                G.snake.append(G.snake[0])

            for s in G.snake:
                G.board[s[0]][s[1]]='█'
                # G.board[s[0]][s[1]]='*'

            try:
                G.board[G.food[0]][G.food[1]]='+'
            except:
                G.food=foodgen()
            os.system('cls')
            
            for _ in G.board:
                for __ in _:
                    print(__,end="")
                    #print(" ",end="")
                print()
                
            # print(G.snake)
            time.sleep(0.05)
            print("\n")
    
    print("Exit")

t = Thread(target=draw_snake)
t.start()

def askinput():
    try:
        if keyboard.is_pressed('w') and G.dy!=1:
            with G.lock:
                G.dy=-1
                G.dx=0
        elif keyboard.is_pressed('s') and G.dy!=-1:
            with G.lock:
                G.dy=1
                G.dx=0
        elif keyboard.is_pressed('a') and G.dx!=1:
            with G.lock:
                G.dy=0
                G.dx=-1
        elif keyboard.is_pressed('d') and G.dx!=-1:
            with G.lock:
                G.dy=0
                G.dx=1
    except:
        return 0
    return 1

while askinput():
    pass