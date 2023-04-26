try: 
    number = int(input("Enter a number: "))
    print("This your orignal number {} ".format(number))
    print("This number is binary  {:b} ".format(number))
    print("This number is in octal  {:o} ".format(number))
    print("This number is in hexadecimal  {:X} ".format(number))
    print("This number is in scientific notation {:E} ".format(number))
except:
    print("Invalid Number")

#displaying digits in different ways in py using the try and except method 
