try:
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    result = num1*num2
    print("Результат множення чисел: ",result)
except ValueError:
    print("You entered something else instead of number")
