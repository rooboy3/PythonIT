decimal_number = int(input("Number: "))
result = ""
binary_values = [128,64,32,16,8,4,2,1]
for item in range(len(binary_values)):
    if decimal_number >= binary_values[item]:
        result = result + "1"
        decimal_number = decimal_number - binary_values[item]
    else:
        result = result + "0"
print(result)