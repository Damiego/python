#scope 
name = "jane"            # global scope available outside and inside a funtion 
def display_name():
    name = "willams"      # local scope only available inside this function 
    print(name)
display_name()
print(name)
