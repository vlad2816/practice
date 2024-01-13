# first of all list are mutable, tuples are immutables 

fruits = ['apple', 'orange', 'pear']
for x in fruits:
    print(x)
fruits[1] = 'another_fruit'
fruits.append('strawberry')
print(fruits)
print(type(fruits))
# this is why list are mutable, we can add/remove data 

tupleees = ('apple', 'orange', 'pear')

print([x for x in tupleees])
print(type(tupleees))
# we cant add/remove change the tuple but its more faster than the list 