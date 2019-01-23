K = [[0,0,0],[1,1,0],[1,0,0],[1,0,0]]

distance = [ [len(K)*len(K[0]) for col in range(len(K[0]))] for row in range(len(K))]
flag = [ [-1 for col in range(len(K[0]))] for row in range(len(K))]


print(len(K))

a=0
b=0

c,d = 3,1

distance[a][b] = 0



flag[a][b] = 1
for i,j in [(0,1),[0,-1],(1,0),(-1,0)]:
		s1 = a+i 
		s2 = b+j 
		if (K[s1][s2] ==0) and (s1>=0) and (s1 < len(K)) and (s2>=0) and (s2 < len(K[0])):
			flag[s1][s2] = 0


while distance[c][d] == 12:
# for n in range(6):
	for i in range(len(K)):
		for j in range(len(K[0])):
			if flag[i][j] == 0:
				# update distance
				dis = []
				for m,n in [(0,1),[0,-1],(1,0),(-1,0)]:
					s1 = i+m 
					s2 = j+n
					if (s1>=0) and (s1 < len(K)) and (s2>=0) and (s2 < len(K[0])):
						dis.append(distance[s1][s2]+1)
				distance[i][j] = min(dis)

				# update flag
				flag[i][j] = 1
				for m,n in [(0,1),[0,-1],(1,0),(-1,0)]:
					s1 = i+m 
					s2 = j+n
					# print(s1,s2,K[s1][s2],distance[s1][s2])
					if (s1>=0) and (s1 < len(K)) and (s2>=0) and (s2 < len(K[0])):
						if (K[s1][s2] ==0) and (flag[s1][s2] == -1):
							flag[s1][s2] = 2
	for i in range(len(K)):
		for j in range(len(K[0])):
			if flag[i][j] == 2:
				flag[i][j] = 0

path = []
path.append([c,d])

marching = distance[c][d] -1

[p1,p2] = [c,d]


print(d)
print(p1,p2)
while marching >= 0:
	for m,n in [(0,1),[0,-1],(1,0),(-1,0)]:
		s1 = p1+m 
		s2 = p2+n
		if (s1>=0) and (s1 < len(K)) and (s2>=0) and (s2 < len(K[0])):
			if(distance[s1][s2]) == marching:
				p1,p2 = s1,s2
				print(p1,p2)

	path.append([p1,p2])
	marching = marching-1

print(path)

path2 = []

print(len(path))

for i in range(len(path)):
	path2.append(path[len(path)-i-1])

print(path2)