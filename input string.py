input_string = input("enter the string")
char_to_remove = input("enter the character")
newStr = ""
for character in input_string:
    if character != char_to_remove:
        newStr += character

print("The input string is:", input_string)
print("The character to delete is:", char_to_remove)
print("The output string is:", newStr)
OUTPUT:
enter the stringHello world
enter the character1
The input string is: Hello world
The character to delete is: 1
The output string is: Hello world
