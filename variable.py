one = 2
two = 1
temp_init = 0
temp = temp_init

temp = one
one = two
two = temp
temp = temp_init

print('one: ', one)
print('two: ', two)