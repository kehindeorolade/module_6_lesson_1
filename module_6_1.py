#running python codes using the lambda function

num_1 = [5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5]


#Using lambda function to count the odd numbers in the list
print('\Odd numbers in the list')
odd_num = list(filter(lambda x: x % 2 !=0, num_1))
print(odd_num)

#Using lambda function to count the even numbers in the list
print('\even numbers in the list')
even_num = list(filter(lambda x: x % 2 ==0, num_1))
print(even_num)


#Using lambda function to square every numbers on the list
print("\nSquare every number of the said list:")
square_of_num_1 = list(map(lambda x: x ** 2, num_1))
print(square_of_num_1)


#Using lambda function to cube every numbers on the list
print("\nCube every number of the said list:")
cube_of_num_1 = list(map(lambda x: x ** 3, num_1))
print(cube_of_num_1)