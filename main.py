import numpy as np


class Position:
    def __init__(self):
        self.treasure_map = [[4, 0, 0, 1, 2], [1, 2, 5, 0, 0], [4, 0, 3, 4, 3]]
        self.visited = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.k =0

    def search(self):
        for z in range(0,len(self.treasure_map)-1):
            for v in range(0,len(self.treasure_map[z])-1):
                if self.treasure_map[z][v]!=0:
                    self.visited[z][v] = 1
                    self.treasure_value()

        print(self.sum_of_treasures())

    def treasure_value(self):


        while self.k < len(self.visited)*len(self.visited[0]):
            self.k += 1
            self.make_step(self.k)
# TODO musze zmienić sposób k
    def make_step(self, k):
        for i in range(0, len(self.visited) ):
            for j in range(0, len(self.visited[i]) ):
                if self.visited[i][j] == k:
                    if i > 0 and self.treasure_map[i - 1][j] != 0 and self.visited[i - 1][j] == 0:
                        self.visited[i-1][j ] = k+1
                        k+=1

                    if j > 0 and self.treasure_map[i][j - 1] != 0 and self.visited[i][j - 1] == 0:
                        self.visited[i][j - 1] = k+1
                        k += 1

                    if i < len(self.visited)-1 and self.treasure_map[i + 1][j] != 0 and self.visited[i + 1][j] == 0:
                        self.visited[i+1][j ] = k+1
                        k += 1

                    if j < len(self.visited[i])-1 and self.treasure_map[i][j + 1] != 0 and self.visited[i][j + 1] == 0:
                        self.visited[i][j + 1]= k+1
                        k += 1


#TODO zmienić sposób dodawaninia
    def sum_of_treasures(self):
        sum=0
        for i in range(0, len(self.visited) ):
            for j in range(0, len(self.visited[i]) ):
                if self.treasure_map[i][j]>sum:
                    sum=self.treasure_map[i][j]
        return sum



c = Position()
c.search()
