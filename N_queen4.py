# put any N for a NxN matrix to fit N number of Queens 
N= 4
#print board

board=[[0]*N for i in range(N)]


#define isAttack Function

def isSafe(i,j):

	#for row and column check
	for k in range(0,N):
		if board[i][k] == 1 or board[k][j] == 1:
			return False
	#for diagonal
	for k in range(0,N):
		for l in range(0,N):
			if (l+k == i+j) or (l-k == i-j):
				if board[k][l] == 1:
					return False
	return True

# main decission function 
def N_Queen(n):
	if n == 0:
		return True
	
	for i in range(0,N):
		for j in range(0,N):
			if (isSafe(i,j) and board[i][j]!=1):

				# Queen is placed 
				board[i][j]=1

				# Here we call the decision again until n=0 and function returns True
				if N_Queen(n-1)==True:

					return True
				# Here Queen is removed
				board[i][j]=0
	return False

N_Queen(N)
for i in board:
	print(i)