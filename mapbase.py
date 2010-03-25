#Map Generator 1.0
#Programmer: Evan Gipson
#Date: 03-19-2010

#carry a counter and have a rule, like
#until land touches other land,
#don't stop
#so land can connect, if they prefer a landy map
#if they prefer a islandy map
#look up, down, right, and left ahead a couple squares for land
#if you see it, do not grow anymore.
#
#also, figure out a better algorithm for growth.

import pygame
import random

n = input("how big do you want the screen? ")
m = input("how many islands do you want? ")

#the actual thing to modify the graph
def LandExpand(x, y, n):
    graph[x][y] = 1
    graph[x+1][y] = 1
    graph[x-1][y] = 1
    graph[x][y+1] = 1
    graph[x][y-1] = 1
    graph[x+1][y+1] = 1
    graph[x-1][y-1] = 1
    graph[x-1][y+1] = 1
    graph[x+1][y-1] = 1

#to modify the matrix
def RandomExpand(x, y, n):
    #grow the 1's
    #don't go over the edge!
    if (x > n-2 or x < 1 or y > n-2 or y < 1):
        pass
    else:
        #modify x and y here       
        LandExpand(x,y,n)
        #set the rules for advanced
        #map design here, aka
        #if so much land, build land, etc.
        #if too much water, more land.
        #if ( x % 2 != 0):
        #    x = x + 1
        #    y = y - 1
        #elif ( y % 2 != 0):
        #    x = x - 1
        #    y = y + 1
        #else:
        #    x = x + 1
        #    y = y + 1
        #recursion
        #RandomExpand(x,y,n)
#to draw the actual map
def DrawMap(graph):
    for row in range(n):
        for col in range(n):
            if (graph[col][row] == 1):
                pixel = pygame.Rect(row*20, col*20, 100, 100)
                pygame.draw.rect(screen, (0,255,0), pixel)
            else:
                pixel = pygame.Rect(row*20, col*20, 100, 100)
                pygame.draw.rect(screen, (0,0,255), pixel)
                
graph = [[0 for col in range(n)]for row in range(n)]

#get the dimensions for that first seed
for i in range(m):
    x = random.randrange(2,n-1)
    y = random.randrange(2,n-1)
    print x, y
    RandomExpand(x,y,n)
    RandomExpand(x+1,y+1,n)
    RandomExpand(x-1,y-1,n)
    RandomExpand(x+1,y,n)
    RandomExpand(x,y+1,n)
    

screen = pygame.display.set_mode((n*20,n*20))
running = 1

for i in graph:
    print i

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0,0,0))
    DrawMap(graph)
    pygame.display.flip()

