listA = [1,2,4,5]
listB = list(range(0,10,3))
listC = [listA,listB]
listD = listA + listB
print(listA)
print(listB)
print(listC)
print(listD)

print(listA[1:3])
listA[0:2] = [-1,-6]
print(listA)

listA.append(36)
print(listA)
listA.extend(listB)
print(listA)
listA.insert(0,56)
print(listA)
listA.remove(-6)
print(listA)
listA.pop()
print(listA)
print(listA.count(56))
print(listA.index(56))
listA.reverse()
print(listA)
listA.sort()
print(listA)



