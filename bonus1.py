# get some info from user and display it
# first create an empty list to store multiple entries
user_info = []

#convert the string input to a list and add input to the list 
user_info += input("What was your first pet's name? ").split()
user_info += input("What street did you grow up on? ").split()
user_info += input("What is you favorite adjective? ").split()

#convert list items into strings separated with a space
user_info = ' '.join(user_info)

#display the formatted string to the user
print(f'Hello, the {user_info}!')
