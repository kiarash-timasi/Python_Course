basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana', 'tomato'}
basket2= {'apple', 'orange', 'apple', 'cherry', 'strawberry', 'strawberry', 'strawberry'}
print(basket2)
print(basket)
print('orange' in basket)
print('cherry' in basket)

#set methods
print(basket2-basket)
print(basket2|basket)
print(basket2&basket)
print(basket2^basket)

#access to sets item
basket3= (basket2|basket)
for i in basket3:
    print(i)
basket_list = list(basket3)
print(basket_list)

#Add item to set
S_set = {'A','B','C'}
F_set = {1,2}
F_set.add(3)
F_set.update(['a','b'])
F_set.update(S_set)
print(F_set)
#remove item from set
F_set.remove(3)
F_set.discard(1)
#F_set.clear()
#del F_set
print(F_set)

#Loop sets
numbers_sets = {1,2,3,4,5,6}
squared_sets = {i**2 for i in numbers_sets}
print(squared_sets)

#join sets
join_set = numbers_sets|squared_sets
print(join_set)

print(basket2-basket)
print(basket2|basket)
print(basket2&basket)
print(basket2^basket)
