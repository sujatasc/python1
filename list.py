my_list = [1, 2, 3, 'apple', 'banana', True]


print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True


my_list[3] = 'cherry'
print(my_list)  # Output: [1, 2, 3, 'cherry', 'banana', True]


my_list.append('orange')
print(my_list)  # Output: [1, 2, 3, 'cherry', 'banana', True, 'orange']

my_list.remove('banana')
print(my_list)  # Output: [1, 2, 3, 'cherry', True, 'orange']