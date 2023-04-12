def raise_power (base_number, power_number):
    result = 1
    for index in range(power_number):
        result = result * base_number
    return result
    
print(raise_power(3,4))