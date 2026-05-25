# For Checking The strength of Password We will Give Points to Password
# If Password Get More Points it is Stong If it get less points its Weak
import string

def Strength(Password):
    Points = 0      #Points

    # This For Checking that The Password has More then 0 Uppercase/Lowercase/Digits/Specialcharacters
    Number_of_Upercase = 0
    Number_of_Lowercase = 0
    Number_of_Digits = 0
    Number_of_specialCh = 0

    #Checking For Uppercase    
    for Character in Password:
        if(Character.isupper()):
            Number_of_Upercase += 1

    if(Number_of_Upercase > 0):
        Points += 1
        print(f"it has Uppercase letter(s)")

    #Checking For Lowercase
    for Character in Password:
        if(Character.islower()):
            Number_of_Lowercase += 1

    if(Number_of_Lowercase > 0):
        Points += 1
        print(f"it has Lowercase letter(s)")

    #Checking For Digits
    for Character in Password:
        if(Character.isdigit()):
            Number_of_Digits += 1

    if(Number_of_Digits > 0):
        Points += 1

    #Checking For Special Characters
    for Character in Password:
        if not Character.isalpha() and not Character.isdigit():
            Number_of_specialCh += 1

    if(Number_of_specialCh > 0):
        Points += 1

    #Checking For Length, is it More Then 8 and 12 Characters Or Not
    if(len(Password) >= 8 and len(Password) < 12):
        Points += 1
    
    elif(len(Password) >= 12):
        Points += 2

    #Final Output
    if(Points >=0 and Points <= 2):
        print("Password is weak!")
    if(Points >=3 and Points <= 4):
        print("Password is Moderate!")
    if(Points >=5 and Points <= 6):
        print("Password is Strong!")
    

#To Execute
Strength(input("Enter password Here => "))
    

    



