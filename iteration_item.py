# for loop advance

fruits = ['apple', 'pears', 'strawberry', 3, 5, 6]

for fruit in fruits:
    print(fruit)
print([x for x in fruits]) 

for x in fruits:
    if x == 'pears':
        print(x)
    else:
        print('we dont have pears at this index')

