import sys

# Gets the length of the log 
def piecesOfList(i,j):
   x = i
   listSum = 0
   while (x < j+1):
    listSum = listSum + n[x]
    x = x + 1
   return listSum

# Recursive Program to get optimal combined length of all logs.
def timber(i, j):
   if (i == j):
    return n[i]

   return piecesOfList(i,j) - min(timber(i + 1,j),timber(i, j - 1))

inputFile = sys.argv[1]
file = open(inputFile)
n = file.readline().split()

for g in range(0, len(n)):
   n[g] = int(n[g])

print(timber(0, len(n) - 1))
