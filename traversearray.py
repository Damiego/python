def traverse_array(arr): #traverse_array that takes a single parameter arr
    for num in arr:  #terates over each element in the input array arr.
        print(num)

if __name__ == "__main__": #Python idiom that checks whether the script is being run as the main program or if it's being imported as a module into another script. 
    array = [1, 9, 4, 7, 20, 25, 3]
    traverse_array(array)

#Each element of the array is printed on a separate line,as the traverse_array function iterates through the array using the for loop