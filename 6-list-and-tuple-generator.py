userInput = input("Enter numbers here, seperated by a comma: ")

userList = [userNumber.strip() for userNumber in userInput.split(',')]
userTuple = tuple(userList)

print(userList)
print(userTuple)