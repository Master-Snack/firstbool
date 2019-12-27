n = int(input('Enter number of size:'))
dx, dy = 1, 0
x, y = 0, 0
matrix = [[None] * n for j in range(n)]
for i in range(n ** 2): # (** = bình phương)
    matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == None:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy

for x in range(n):
    for y in range(n):
        print('%02i' % matrix[x][y], end=' ')
    print()

#print()