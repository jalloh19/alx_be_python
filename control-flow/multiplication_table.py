
# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to print the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
