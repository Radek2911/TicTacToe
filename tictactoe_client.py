import pygame
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
####Sockets
import socket
import atexit
pygame.display.set_caption('Client')
screen.fill((0,0,0))
white=(255,255,255)
red=(255,0,0)
blue=(0,255,0)
turn=0
host='localhost'
port=12346
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print('connected')
def handle_exit():
    print('this runs after keyboard interrupt')
    s.close()
atexit.register(handle_exit)
####Sockets
tic={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
while True:
    pygame.draw.line(screen,white,(225,100),(225,500),2)
    pygame.draw.line(screen,white,(350,100),(350,500),2)
    pygame.draw.line(screen,white,(100,225),(500,225),2)
    pygame.draw.line(screen,white,(100,350),(500,350),2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            s.close()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and turn==1:
            time.sleep(0.2)
            turn=turn+1

            data=(str(event.pos[0])+','+str(event.pos[1]))
            pygame.draw.rect(
                screen,'red',(int(event.pos[0]), int(event.pos[1]), 30,30)
            )
            s.sendall(data.encode())
            break
            
    if turn==0:
        data=s.recv(1024)
        data=data.decode()
        pygame.event.clear()

        test=data.split(',')
        pygame.draw.circle(
            screen,'blue',(int(test[0]),int(test[1])),30,2)
        print(test)
        turn=1

    
