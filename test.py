from collections import defaultdict
board = [0,0,0,0]
visit = [[0] * len(board) for x in range(len(board))]
visit[0][0]=1
print(visit)