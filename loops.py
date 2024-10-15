# A loop is a piece of code designed to run repetitively until a specified
# condition becomes false

# 1. While loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Second example with while loop
countTwo = 1
stringToPrint = "r"
while countTwo <= 5:
    print(stringToPrint*countTwo)
    countTwo+=1

# 2. For loop
# range(start, stop, step)
numbers = range(1,6,1)
for number in numbers:
    print(number)

myNames = ["Daniel","Munene","Owade","Marvin","Judy","Ian","Benjamin"]
for name in myNames:
    print(name)

students = {"adm1":"Grace", "adm2":"Munene","adm3":"Judy"}
for admissionNumber, studentName in students.items():
    print(studentName)

wanafunzi = {
    "mwanafunzi1":{"name":"John","adm":"176","yearOfStudy":"Fourth"},
    "mwanafunzi2":{"name":"Mike","adm":"500","yearOfStudy":"Second"},
    "mwanafunzi3":{"name":"Judy","adm":"356","yearOfStudy":"First"},
    "mwanafunzi4":{"name":"Munene","adm":"96","yearOfStudy":"Third"}
}
for k,v in wanafunzi.items():
    print(v["name"])
    print(v["adm"])
    print(v["yearOfStudy"])