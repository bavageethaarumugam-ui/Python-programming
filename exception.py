try:
    n=int(input("Enter a value:"))
    res=50/n
except ZeroDivisionError:
    print("It is division by zero error")
else:
    print(res)
finally:
    print("bye")
