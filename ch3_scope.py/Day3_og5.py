# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

input_pwd = "ABd1234@1,a F1#,2w3E*,2We3345"
input_pwd_list = input_pwd.split(',')
cnt = 0
isPwd = False
for item in input_pwd_list:
    isPwd = (6 <= len(item) and len(item) <= 12)
    if(isPwd):
        for i in item:
            if i.isupper():
                cnt += 1
                break
        for i in item:
            if i.islower():
                cnt += 1
                break
        for i in item:
            if i.isnumeric():
                cnt += 1
                break
        for i in item:
            if (i == '@' or i == '#' or i == '$'):
                cnt += 1
                break
    if isPwd and cnt == 4:
        print(item)
isPwd = False
