# 1. Write a python logic to calculate the area of any circle.
myPi = 3.142
radius = 14
area = myPi * radius * radius
print(f"Your area is {area}")
# 2. Write a python logic to calculate the grades of a certain subject marks
# N/B: Use scale - marks below 40 = Fail
#                - marks between 40 and 50 = Pass
#                - marks between 50 and 60 = Average
#                - marks equal or above 60 = Excellent
marks = 90
if marks < 40:
    print("Fail")
elif marks < 50:
    print("Pass")
elif marks < 60:
    print("Average")
else:
    print("Excellent")
# 3. Given a list of integers, calculate their total with use of a loop.
myIntegers = [100,245,563,984,345,526,867,928,359]
total = 0
for number in myIntegers:
    total += number
print(total)