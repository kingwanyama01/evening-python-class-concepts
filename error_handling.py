try:
    x = 10
    y = 0
    z = x / y
    print(z)
except ZeroDivisionError:
    print("ERROR: Division by zero")