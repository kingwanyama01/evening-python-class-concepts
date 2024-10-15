# A function is a block of code that only runs when it is called
# It is designed to perform a specific task
# It returns data as a result
# CUSTOM FUNCTIONS
def motto():
    my_motto = "Education is the key to success"
    return my_motto

print(motto())
print(motto())

myMotto = motto()
print(myMotto)

def addition():
    x = 10
    y = 20
    z = x + y
    return z

answer = addition()
print(answer)

def addition_two(x,y):
    z = x + y
    return z
answerTwo = addition_two(30,76)
print(answerTwo)

def average(first_number, second_number, third_number):
    result = (first_number + second_number + third_number)/ 3
    return result

myAverage = average(10,20,30)
print(myAverage)

# INBUILT FUNCTIONS
jina = "king wanyama"
print(jina.upper())
print(jina.lower())
print(jina.title())

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, your age is {age}")
