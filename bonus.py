# get some info from user and display it
# first create an empty list to store multiple entries
userInfo = []

#convert the string input to a list and add input to the list 
userInfo += input("What was your first pet's name? ").split()
userInfo += input("What street did you grow up on? ").split()
userInfo += input("What is you favorite adjective? ").split()

#convert list items into strings separated with a space
userInfo = ' '.join(userInfo)

#display the formatted string to the user
print(f'Hello, the {userInfo}!')
