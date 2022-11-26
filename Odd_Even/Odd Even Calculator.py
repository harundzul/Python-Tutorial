while True:
    def odd_even_calculator(a,b):
        sum = a+b
        if(sum % 2 == 0):
            print(str(sum) +" is even")
        else:
            print(str(sum) +" is odd")

    a = input("Enter number 1:")
    a = int(a)
    b = input("Enter number 2:")
    b = int(b)

    odd_even_calculator(a, b)