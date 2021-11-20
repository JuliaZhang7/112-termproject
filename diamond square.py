import random
from cmu_112_graphics import *
def diamond_square(n):
    height_map_size=2**n+1
    height_map=[ ([0] * height_map_size) for row in range(height_map_size) ]
    height_map[0][0]=random.randint(0,20)
    height_map[0][len(height_map[0])-1]=random.randint(0,20)
    height_map[len(height_map)-1][0]=random.randint(0,20)
    height_map[len(height_map)-1][len(height_map[0])-1]=random.randint(0,20)
    chunk_size=height_map_size-1
    roughness=3
    while chunk_size>1:
        half=chunk_size//2
        for row in range(0,len(height_map)-1,chunk_size):
            for col in range(0,len(height_map[0])-1,chunk_size):
                print((row,col),(row+half,col+half))
                height_map[row+half][col+half]=(height_map[row][col]+height_map[row][col+chunk_size]+height_map[row+chunk_size][col]+height_map[row+chunk_size][col+chunk_size])//4+random.randint(-roughness,roughness)
                print('chunk:',chunk_size,'half',half)
        for row in range(0,len(height_map),half):
            for col in range((row+half)%chunk_size,len(height_map[0]),chunk_size):
                print((row,col),(row+half,col+half))
                if row==0:
                    height_map[row][col]=(height_map[row][col-half]+height_map[row][col+half]+height_map[row+half][col])//3+random.randint(-roughness,roughness)
                elif row==len(height_map)-1:
                    height_map[row][col]=(height_map[row][col-half]+height_map[row][col+half]+height_map[row-half][col])//3+random.randint(-roughness,roughness)
                elif col==0:
                    height_map[row][col]=(height_map[row][col+half]+height_map[row-half][col]+height_map[row+half][col])//3+random.randint(-roughness,roughness)
                elif col==len(height_map[0])-1:
                    print('oh, we are at left edge!')
                    height_map[row][col]=(height_map[row][col-half]+height_map[row-half][col]+height_map[row+half][col])//3+random.randint(-roughness,roughness)
                else:
                    height_map[row][col]=(height_map[row][col-half]+height_map[row][col+half]+height_map[row-half][col]+height_map[row+half][col])//4+random.randint(-roughness,roughness)
        chunk_size//=2
    return height_map

def diamond_step(height_map,chunk_size,half):
    for row in range(0,len(height_map)-1,chunk_size):
        for col in range(0,len(height_map[0])-1,chunk_size):
            print((row,col),(row+half,col+half))
            height_map[row+half][col+half]=(height_map[row][col]+height_map[row][col+chunk_size]+height_map[row+chunk_size][col]+height_map[row+chunk_size][col+chunk_size])//4
            print((height_map[row][col]+height_map[row][col+chunk_size]+height_map[row+chunk_size][col]+height_map[row+chunk_size][col+chunk_size]))
            print('chunk:',chunk_size,'half',half)
    return height_map
def square_step(height_map,chunk_size,half):
    for row in range(0,len(height_map),half):
        for col in range((row+half)%chunk_size,len(height_map[0]),chunk_size):
            print((row,col),(row+half,col+half))
            if row==0:
                height_map[row][col]=(height_map[row][col-half]+height_map[row][col+half]+height_map[row+half][col])//3
            elif row==len(height_map)-1:
                height_map[row][col]=(height_map[row][col-half]+height_map[row][col+half]+height_map[row-half][col])//3
            elif col==0:
                height_map[row][col]=(height_map[row][col+half]+height_map[row-half][col]+height_map[row+half][col])//3
            elif col==len(height_map[0])-1:
                print('oh, we are at left edge!')
                height_map[row][col]=(height_map[row][col-half]+height_map[row-half][col]+height_map[row+half][col])//3
            else:
                height_map[row][col]=(height_map[row][col-half]+height_map[row][col+half]+height_map[row-half][col]+height_map[row+half][col])//4
            #print((height_map[row][col]+height_map[row][col+chunk_size]+height_map[row+chunk_size][col]+height_map[row-chunk_size][col+chunk_size]))
            print('chunk:',chunk_size,'half',half)
    return height_map

map=[[7, 8, 9, 9, 9], 
    [9, 9, 10, 10, 10],
    [11, 11, 12, 12, 13],
    [13, 13, 13, 14, 15],
    [15, 14, 15, 16, 19]]
print(diamond_square(4))
[   [14, 11, 12, 8, 12, 10, 13, 9, 12, 7, 7, 5, 9, 10, 7, 10, 10],
    [14, 15, 13, 7, 8, 13, 7, 7, 10, 8, 11, 9, 10, 7, 11, 7, 5],
    [11, 12, 12, 5, 7, 13, 9, 6, 7, 9, 10, 8, 8, 11, 11, 7, 7],
    [9, 13, 10, 9, 9, 11, 10, 9, 8, 10, 6, 6, 4, 6, 10, 8, 5],
    [10, 12, 8, 8, 10, 7, 12, 13, 11, 10, 6, 4, 7, 7, 10, 10, 7], 
    [10, 10, 6, 6, 8, 5, 7, 12, 9, 12, 5, 7, 9, 7, 11, 10, 12],
    [6, 6, 8, 9, 7, 4, 6, 11, 10, 7, 10, 7, 7, 6, 9, 8, 10],
    [10, 9, 7, 6, 4, 6, 6, 9, 8, 9, 11, 8, 6, 7, 8, 5, 10],
    [11, 11, 8, 6, 8, 5, 9, 6, 9, 8, 9, 11, 7, 5, 7, 8, 8],
    [6, 7, 8, 8, 3, 5, 8, 5, 6, 11, 9, 10, 7, 5, 5, 5, 9],
    [7, 4, 4, 8, 3, 3, 5, 10, 11, 12, 10, 5, 6, 9, 9, 9, 7],
    [7, 6, 5, 8, 9, 7, 6, 10, 8, 8, 9, 8, 5, 5, 7, 5, 8], 
    [4, 2, 6, 7, 7, 6, 8, 8, 8, 8, 10, 5, 6, 7, 5, 5, 8],
    [1, 7, 8, 6, 2, 4, 10, 10, 10, 7, 4, 4, 8, 7, 6, 9, 7], 
    [3, 2, 4, 6, 5, 6, 10, 12, 9, 8, 10, 8, 4, 4, 7, 9, 7],
    [1, 2, 5, 4, 3, 8, 8, 8, 9, 7, 8, 7, 4, 6, 5, 9, 6], 
    [1, 5, 6, 4, 4, 5, 6, 4, 9, 11, 11, 9, 8, 7, 11, 7, 11]]