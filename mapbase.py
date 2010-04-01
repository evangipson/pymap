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
from pygame.locals import *
import sys

n = input("how big do you want the screen? ")
m = input("how many islands do you want? ")

#the actual thing to modify the graph
def LandExpand(graph,n,x,y):
        if (x > n-2 or x < 1 or y > n-2 or y < 1):
            pass
        elif graph[x][y] == 1:
            graph[x+1][y] = 1
            graph[x-1][y] = 1
            graph[x][y+1] = 1
            graph[x][y-1] = 1
            graph[x+1][y+1] = 1
            graph[x-1][y-1] = 1
            graph[x-1][y+1] = 1
            graph[x+1][y-1] = 1

#to modify the matrix
def RuleExpand(graph,n):
    #modify x and y here       
    #set the rules for advanced
    #map design here, aka
    #if so much land, build land, etc.
    #if too much water, more land.
    #
    #want the land to stop growing if there is too much
    #if the pixel selected is land, do something.
    #for as many rows in graph
    #    for as many columns in graph
    for row in range(n):
        for col in range(n):
            #try used because out of range of graph
            #if graph[row][col] == 1:
            #if graph[row+4][col] == 1 or graph[row-4][col] == 1:
            #iterate over and make sure every entry is a 1 on the way, otherwise, connect
            #if the island is huge, quit.
            try:
                addition = AddGraph(graph, row, col)
            except:
                pass
            else:
                if addition > 5:
                    graph[row][col] = 0
                elif addition <= 3:
                    graph[row][col] = 1
                else:
                    pass
            #elif graph[row][col+4] == 1 or graph[row][col-4] == 1:
            #iterate over and make sure every entry is a 1 on the way, otherwise, connect
            #if the island is huge, quit
            #   addition = AddGraph(graph, row, col)
            #  if addition >= 5:
            #     graph[row][col] = 0
            #elif addition <= 3:
            #    graph[row][col] = 1
            #else:
            #    pass
            #else:
            #    LandExpand(graph, row, col)
            #if you hit out of range, do nothing
            #don't care about water

def AddGraph(graph,x,y):
    counter = 0
    if graph[x+1][y] == 0:
        counter = counter + 1
    if graph[x-1][y] == 0:
        counter = counter + 1
    if graph[x][y+1] == 0:
        counter = counter + 1
    if graph[x][y-1] == 0:
        counter = counter + 1
    if graph[x+1][y+1] == 0:
        counter = counter + 1
    if graph[x-1][y-1] == 0:
        counter = counter + 1
    if graph[x-1][y+1] == 0:
        counter = counter + 1
    if graph[x+1][y-1] == 0:
        counter = counter + 1
    return counter
            
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
#list for keeping random numbers, for growth later
list_random = []

#get the dimensions for that first seed
for i in range(m):
    x = random.randrange(2,n-1)
    y = random.randrange(2,n-1)
    print x, y
    graph[x][y] = 1
    list_random.append([x,y])
#call expansion once for whole graph
#and use rules to expand land
#RuleExpand2(graph, n)

running = 1

for i in graph:
    print i

screen = pygame.display.set_mode((n*20,n*20))


def main():
    pygame.init()
    screen.fill((0,0,0))
    DrawMap(graph)
    while 1:
        for event in pygame.event.get(): 
            if event.type == QUIT:
                sys.exit()
                return
            #show initial pixel >> island with spacebar interval
            if event.type == pygame.KEYUP:
                if event.key == K_e:
                    for item in list_random:
                        LandExpand(graph, n, item[0], item[1])
                    DrawMap(graph)
                if event.key == K_SPACE:
                    RuleExpand(graph, n)
                    DrawMap(graph)
        #refine map after drawing, hopefully states shown by spacebar
        pygame.display.update()

if __name__ == '__main__': main()  
