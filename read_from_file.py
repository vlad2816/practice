read_file = open('read_from_this_file.txt', 'r')

f = read_file.readlines()

# iterating in the data file

new_list = []
for line in f:
    if line[-1] == '\n':
        new_list.append(line[0:-1])
    else:
        new_list.append(line)

# why i do this, because if we have text in diff lines python make \n too separate the lines, so i make
# a empty list, i append the text in that list without the last char that is \n
print(new_list)

# With the strip method we can actually remove \n more easy

new_list_strip_method = []
for x in f:
    new_list_strip_method.append(x.strip())

print(new_list_strip_method)