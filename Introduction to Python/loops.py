listA = [x**2 for x in range(50, 100)]
listB = [y**2 for y in range(80, 130)]
listC = []
for i in listA:
    for j in listB:
        if i < 8100 and j < 8100:
            if i == j:
                listC.append((i, j))

print(listC)
#----------------------------------------------------------

num = [x for x in range(0, 100, 2)]
x = 0
for i in num:
    x +=1
print(x)
#----------------------------------------------------------
def star (n):
    for i in range(1, n + 1):
        print('* ' * i)
star(5)

def star2 (n):
    for i in range(n, 0, -1):
        print('* ' * i)
star2(6)

def star3 (n):
    for i in range(1, n + 1):
        print(' '*(n-i) + '* ' * i)
star3(5)

def star4 (n):
    for i in range(1, n + 1):
        print(' '*(n-i) + '* ' * i)
    for i in range(n-1, 0, -1):
        print(' ' * (n - i) + '* ' * i)
star4(5)
#----------------------------------------------
count = 1
while count <= 5:
    print(count)
    if count == 3:
        break
    count += 1

