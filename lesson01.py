# define a function to do the work for us
def count_words(input_str: str) -> dict[str, int]:
    cleaned_list = input_str.replace(",", "").lower().split()
    result = {}
    for word in cleaned_list:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result


# call the function below
input_str = "mary had a little lamb, little lamb, little lamb"
word_counts = count_words(input_str)
print(word_counts)


def count_words_two(input_str: str) -> dict[str, int]:
    cleaned_list = input_str.replace(",", "").lower().split()

    unique_words = set(cleaned_list)
    word_counts = {}

    for word in unique_words:
        word_counts[word] = cleaned_list.count(word)

    return word_counts


word_counts = count_words_two(input_str)
print(word_counts)


def count_words_four(input_str: str) -> tuple[list[str], list[int]]:
    cleaned_list = input_str.replace(",", "").lower().split()
    words = []
    counts = []

    for word in cleaned_list:
        if word not in words:
            words.append(word)
            counts.append(1)
        else:
            counts[words.index(word)] = counts[words.index(word)] + 1
    return words, counts


word_counts = count_words_four(input_str)
print(word_counts)


from collections import Counter


def count_words_three(input_str: str) -> dict[str, int]:
    cleaned_list = input_str.replace(",", "").lower().split()
    return dict(Counter(cleaned_list))


def count_words_five(input_str):
    cleaned_list = input_str.replace(",", "").lower().split()

    unique_words = set(cleaned_list)
    result = {}

    # initialize dict
    for word in unique_words:
        result[word] = 0

    for word in cleaned_list:
        result[word] += 1
    
    return result

word_counts = count_words_three(input_str)
print(word_counts)

# Optional: clone from github
# git clone https://github.com/shafe123/AI2C-Prereqs.git
# online: https://github.com/shafe123/AI2C-Prereqs/blob/main/lesson01.py

# Create and use a string called my_str with any value
my_str = "hello world"

# Print out the third letter of the string (using an index)
print(my_str[2])
print(my_str[2])
# Print out the last word of the string using index slicing
print(my_str[-1])

# Find two string methods besides split from the python documentation
# and use them on your string

print(my_str.count("l"))
print(my_str.center(20))


# Convert the string to a list and store it in a variable, my_list
# (Look at the slides for an example)

my_list = my_str.split()
print(my_list)

# Research two list methods from the python documentation and experiment
# with their use.  NOTE! Some list methods will give you a new list,
# but other list methods operate on the current list.

my_list.append("new")
print(my_list)

my_list.reverse()
print(my_list)

# Print out the third letter of the list
print(new_list[2])
# Print out the list in reverse order using index slicing
print(my_list[2])
print(my_list[::-1])


# Use the dictionary below for the following problems:
my_dict = {"dogs": 3, "cats": 4, "alpacas": 100}

# Add a new item to the dictionary using the assignment operator '='
my_dict["frank"] = 33

# Add a new item to the dictionary using a dictionary method
my_dict.update() == {"George":5}

# Print out only how many dogs there are
print(my_dict.fromkeys("dogs"))
# Write a function that always returns 10
def always_return_ten() -> int:
    return 10

print(always_return_ten())

# Write a function that returns the cube of a value
def cube(value:int) -> int:
    return value * 3
print(cube(5))

# Write a function that calculates the hypotenuse of a triangle
def my_hyp(a:int,b:int) -> int:
    hypotenuse = (a*a) + (b*b)
    return hypotenuse/hypotenuse

print(my_hyp(3,4))

# hint: remember the Pythagorean theorem, given a and b, calculate c
# Write a function that creates and returns a list from the values 
# of a dictionary that is passed in as an argument

def my_func(Dict):
    my_second_list = []
    my_second_list.extend(Dict.values())
    return my_second_list

print(my_func(my_dict))

