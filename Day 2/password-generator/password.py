import string
# string module for special characters
import random
# random module for random generation

"""Simple password generator program that ask for user input and generates the length of password entered """

# Function
def gen_password(userInput):
    # combination of special character symbols 
    specialCharacter = [random.choice(string.punctuation) for character in range(userInput)]
    
    # lowercase characters a-z
    lowerCase = [random.choice(string.ascii_lowercase) for lower in range(userInput)]
    
    # upper case characters A-Z
    upperCase = [random.choice(string.ascii_uppercase) for upper in range(userInput)]
    
    # number characters 0-9
    numbers = [random.choice(string.digits) for number in range(userInput)]
    
    # join characters all lowerCase, upperCase, specialCharacter & number to form random output
    generatedPassword = ''.join(specialCharacter + lowerCase + upperCase + numbers)
    
    # generate random.choice() characters
    generatedPassword = ''.join(random.choice(generatedPassword) for value in range(userInput))
    
    # return 
    return generatedPassword

# request for user input
question = int(input('Please enter the password length: '))

# execute program
answer = gen_password(question)
print(answer)