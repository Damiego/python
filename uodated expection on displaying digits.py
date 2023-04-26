try: 
    number = int(input("Enter a number: "))
except ValueError as e:
    print(e)
    print("Invalid Number")
else: 
    print("This is your orignal number {} ".format(number))
    print("This number is in  binary  {:b} ".format(number))
    print("This number is in octal  {:o} ".format(number))
    print("This number is in hexadecimal  {:X} ".format(number))
    print("This number is in scientific notation {:E} ".format(number))
