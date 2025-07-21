#Exercise 1
# for number in range(10, 0, -1):
#     print(number)

#Exercise 2
#print(sum(range(1,101)))

#Exercise 3
my_list = list(range(1, 21))
# print(my_list[1:20:3])

#Exercise 4
# prime = False
# n = 100

# while not prime:
#     if n % 2 == 0:
#          n += 1
#          print (n)
#     else:
#          prime = True

#Exercise 5
# i = 5
# while i > 0:
#     print(i)
#     i -= 1

#Exercise 6
# it = iter(my_list)
# print(next(it))

#Exercise 7
# my_nested_list=[("john",2),("stacy",4),("frank",6)]
# for students,grades in my_nested_list:
#     print (students,grades)

#8
# n = 0

# while n < 20:
#     print (n)
#     n += 1

#Skipping 9 & 10

#List comprehension exercise 11
# for x in my_list:
#     if x % 2 == 0:
#         print(x)
#         x*2

#Dictionary comprehension 12
# keys = [1,2,3,4,5]
# values = []

# myDict = {x : x**2 for x in keys}
# print (myDict)

#Set Comprehension 13
vowels = {char for char in input("type something: ") if char.lower() in 'aeiou'}
print("Extracted Vowels: " + ''.join(vowels))

