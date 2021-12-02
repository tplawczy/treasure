import numpy as np


class Position:
    def __init__(self):
        self.treasure_map = [[3, 0, 0, 1, 2],
                             [0, 1, 4, 0, 0],
                             [5, 0, 0, 3, 0]]
        self.visited = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.sum=0
        self.max=0

    def search(self):

        for z in range(0,len(self.treasure_map)):
            for v in range(0,len(self.treasure_map[z])):
                if self.treasure_map[z][v]!=0:
                     if self.visited[z][v]==0:
                        self.visited[z][v] = 1
                        self.sum = 0
                        self.sum = self.treasure_map[z][v]
                        self.treasure_value()
                        if self.sum > self.max:
                            self.max = self.sum
        print(self.max)
###############################################Resolved##########################
    def treasure_value(self):
        self.k = 0


        while self.k <= np.max(self.visited):

            self.k += 1
            self.make_step(self.k,self.sum)
# TODO musze zmienić sposób k
    def make_step(self, k, sum):
        for i in range(0, len(self.visited)):
            for j in range(0, len(self.visited[i]) ):
                if self.visited[i][j] == k:
                    if i > 0 and self.treasure_map[i - 1][j] != 0 and self.visited[i - 1][j] == 0:
                        self.visited[i-1][j ] = k+1
                        self.sum += self.treasure_map[i-1][j]
                        k+=1


                    if j > 0 and self.treasure_map[i][j - 1] != 0 and self.visited[i][j - 1] == 0:
                        self.visited[i][j - 1] = k+1
                        self.sum += self.treasure_map[i][j-1]
                        k += 1

                    if i < len(self.visited)-1 and self.treasure_map[i + 1][j] != 0 and self.visited[i + 1][j] == 0:
                        self.visited[i+1][j ] = k+1
                        self.sum += self.treasure_map[i+1][j]
                        k += 1

                    if j < len(self.visited[i])-1 and self.treasure_map[i][j + 1] != 0 and self.visited[i][j + 1] == 0:
                        self.visited[i][j + 1]= k+1
                        self.sum += self.treasure_map[i][j+1]
                        k += 1

#test
#TODO zmienić sposób dodawaninia



c = Position()
c.search()
