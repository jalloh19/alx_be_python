# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    for col in range(size):
        print("*", end="") 
    print()  
    row += 1
