#updating tuples
#tuples are immutable , so fo updating Tuples :
#convert to list:
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_list[0]=0
my_tuple = tuple(my_list)
print(my_tuple)

#concatenate tuples
your_tuple = (1, 2, 3)
new_value_tuple = (4,)
your_tuple = your_tuple + new_value_tuple
print(your_tuple)

my_tuple2 = ('a', 'b', 'c', 'd', 'e')
#Access Tuple Items
my_tuple2[4]
print(my_tuple2[4])

#Unpack Tuples
(A,B,C,*D) = my_tuple2
print(A)
print(B)
print(C)
print(D)

#loop tuples
my_list2=[]
for i in my_tuple2:
    my_list2.append(i)
print(my_list2)

#Joining
first_tuple = (1,2)
second_tuple = (3,4)
third_tuple = first_tuple + second_tuple
print(third_tuple)
first_tuple += (5,)
print(first_tuple)

#tuples method
ex_tuple = (1,1,'one',2,2,'two',3,3,4,4,5,5,6,6,6)
print(ex_tuple.count(6))
print(ex_tuple.index('one',0,8))




