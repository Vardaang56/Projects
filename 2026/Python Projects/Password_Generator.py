import random
import string
# for generating Password
def Password(length=8):#Lenth of the Password (Default Length is 8)

    characters = string.ascii_letters + string.digits + string.punctuation       #Give Letters A-Z and a-z and give digits 0-9 and Special characters
    random_password = ''.join(random.choice(characters) for _ in range(length))     #Select Letters and Digits Randomly from "characters"
    return random_password
# Now making a code to Execute "Password" Function With Some Details
Platform_Name = input("Enter Platform Name => ")     #to know where to login?
Username = input("Enter Your Username/Email/Phone No. => ")     #For Which Account *Because i have many Accouts on the Same platform*
password = Password(int(input("Enter the Length Of The Password => ")))      #You can adjust the length of the password as you want

print(f"Platform: {Platform_Name}\nUsername: {Username}\nPassword: {password}")     #You Can check Platform and Username Before Saving this into The Computer

#Code For saving These Details And Password

Ask = input("Do You Wanna Save This File? Answer In Y/N Only => ")      #To Confirm Before Saving

if(Ask == "Y" or Ask == "y"):
    with open(f"{Platform_Name}_{Username}.txt", "w") as file: # it will Make a .txt file to write this data
        file.write(f"Platform: {Platform_Name}\nUsername: {Username}\nPassword: {password}") # to write Data in file
        print("Saved!")
elif(Ask == "N" or Ask == "n"):
    print("Not Saving This Data!") #Just Don't Save the Data and print This Line



