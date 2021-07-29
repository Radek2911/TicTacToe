import atexit
import socket
import pygame
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 600))
# sockets
pygame.display.set_caption('Server')
screen.fill((0, 0, 0))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
turn = 0
host = ''
port = 12346
s.bind((host, port))
s.listen(5)
white = (255, 255, 255)
red=(255,0,0)
blue=()
print('Socket is Listening....')
conn, addr = s.accept()


def handle_exit():
    print('this runs after keyboard interrupt')
    conn.close()
    s.close()


atexit.register(handle_exit)
# sockets
while True:
    pygame.draw.line(screen, white, (225, 100), (225, 500), 2)
    pygame.draw.line(screen, white, (350, 100), (350, 500), 2)
    pygame.draw.line(screen, white, (100, 225), (500, 225), 2)
    pygame.draw.line(screen, white, (100, 350), (500, 350), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            conn.close()
            s.close()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and turn==0:
            time.sleep(0.2)
            turn = turn+1
            data = (str(event.pos[0])+','+str(event.pos[1]))
            conn.sendall(data.encode())
            pygame.draw.circle(
                screen, 'blue', (int(event.pos[0]), int(event.pos[1])), 30, 2)
            break
            
    pygame.display.update()

    if turn ==1:
        data = conn.recv(1024)
        data=data.decode()
        pygame.event.clear()


        test=data.split(',')
        pygame.draw.rect(
            screen,'red',(int(test[0]), int(test[1]), 30,30)
        )
        turn = 0
