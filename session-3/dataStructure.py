# data structure in python 

# list
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

# list of strings
string_list = ["apple", "banana", "cherry"]
print(string_list)
print(type(string_list))

# dynamic_list
dynamic_list = [1, "hello", 3.14, True]
print(dynamic_list)
print(type(dynamic_list))

# target my list by index
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Output: 10

#nested list by index
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0][1])  # Output: 2
print(nested_list[1][0])  # Output: 3
print(nested_list[2][1])  # Output: 6


#negative index
my_list = [10, 20, 30, 40, 50]
print(my_list[-1])  # Output: 50
print(my_list[-2])  # Output: 40


# in operator
my_list = [10, 20, 30, 40, 50]
print(20 in my_list)  # Output: True
print(60 in my_list)  # Output: False


#reverse list
my_list = [10, 20, 30, 40, 50]
my_list.reverse()
print(my_list)  # Output: [50, 40, 30, 20, 10]


#sorting a list
my_list = [30, 10, 50, 20, 40]
my_list.sort()
print(my_list)  # Output: [10, 20, 30, 40, 50]


#slicing a list
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[:3])   # Output: [10, 20, 30]
print(my_list[0 : : 2])  # Output: [10, 30, 50] 2 is skipping value 


#positive indexing
nums = [10, 20, 30, 40, 50]
print(nums[1])  # Output: 20

data = ["a", "b", "c", "d", "e"]
print(data[len(data) - 2]) # output: d

lst = [5, 10, 15, 20, 25, 30]

#write an expression using positive indexing to access 20.
print(lst[3])  # Output: 20
# write an expression to access the last element without using -1.
print(lst[len(lst) - 1])  # Output: 30

#negative indexing

num2 = [2, 4, 6, 8, 10]
print(num2[-2])  # Output: 8

#what elemmet does -3 refers to in the list num2
print(num2[-3])  # Output: 6


#predict the output

num3 = [10, 20, 30, 40, 50]
print(num3[1] + num3[3])  # Output: 60 (20 + 40)


#what element does -3 refer to in the list letters
letters = ["p", "q", "r", "s", "t", "u"]
print(letters[-3])  # Output: "s"

#Mixed positive and negative indexing
#identify the eroor (if any) and explain:
num4 = [5, 10, 15]
#print(num4[-4])  # This will raise an IndexError because -4 is out of range for the list num4, which has only 3 elements.

#write a single line of code to print the middle element of a list using indexing 20, 30, 40,50
l = [10, 20, 30, 40, 50, 60]
print(l[1:5])  # Output: [20, 30, 40, 50]



