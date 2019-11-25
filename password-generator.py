#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("""Welcome to the Password Generator App!

The password generator is a program that will generate a random password
for the user. The user will be allowed to input how many upper case letters, 
special characters, and numbers/digits, he or she wants in a password. 
The minimum requirements for a password are that the user's password must be
between 8 and 94 characters long and have at least one of the following:
        -An upper case letter, 
        -A lower case letter,
        -A number, 
        -A special character.

Some features of this password generator include:
        -The password will be generated using ASCII printable characters.
        -The generated password is a permutation with repetition allowed.
""")


# In[ ]:


import random

def password_length():
    while True:
        pw_length = input("\nHow long do you want your password to be?\n ")
        if pw_length.isdigit():
            if 8 <= int(pw_length) <= 94:
                print(f"Thank you. Your password length is {pw_length}.")
                pw_length = int(pw_length)
                return pw_length
                break
            else: 
                print("""\tI'm sorry. Your password must be a 
                minimum of 8 characters and a maximum of 94 characters 
                (All ASCII printable characters except space)""")
                continue
        else:
            print("""\tI'm sorry. Your password must be a 
            minimum of 8 characters and a maximum of 94 characters 
            (All ASCII printable characters except space)""")
            continue


# In[ ]:


def choose_upper():
    while True:
        num_upper = input("\nHow many upper case letters would you like to have in your password?\n")
        if 1 <= num_upper.isdigit():
            if int(num_upper) <= 91:
                print(f"Thank you. You will have {num_upper} uppercase letter(s) in your password.")
                num_upper = int(num_upper)
                return num_upper
                break
            else: 
                print(f"""I'm sorry. Your password must have at least 1 upper
                case letter and a maximum of 91 upper case letters.""")
            continue
        else: 
            print("""Invalid input. Please include a number that is greater 
            than 1 and less than 91 inclusive.""")
            continue


# In[ ]:


def choose_special():
    while True:
        num_special = input("\nHow many special characters would you like to include in your password?\n")
        if num_special.isdigit():
            if 1 <= int(num_special) <= 91:
                print(f"Thank you. You will have {num_special} special character(s) in your password.")
                num_special = int(num_special)
                return num_special
                break
            else: 
                  print(f"""I'm sorry. Your password must have at least 1 
                  special character and a maximum of 91 special characters.""")
            continue
        else: 
            print("""Invalid input. Please include a number that is greater 
            than 1 and less than 91 inclusive.""")
            continue


# In[ ]:


def choose_digits():
    while True:
        num_digits = input("\nHow many numbers would you like to include in your password?\n")
        if num_digits.isdigit():
            if 1 <= int(num_digits) <= 91:
                print(f"Thank you. You will have {num_digits} number(s) in your password.")
                num_digits = int(num_digits)
                return num_digits
                break
            else: 
                print(f"""I'm sorry. Your password must have at least 1 number
                and a maximum of 91 special numbers.""")
            continue
        else: 
            print("""Invalid input. Please include a number that is greater 
            than 1 and less than 91 inclusive.""")
            continue


# In[ ]:


# This function checks to see if the user inputs will allow 
# the logic of this program to work while meeting the
# requirements.
def check_user_inputs(pw_length, num_lower, num_upper, num_special, num_digits):
    sum_pw_char = num_lower + num_upper + num_special + num_digits 
    if sum_pw_char == pw_length:
        if 8 <= sum_pw_char <= 94:
            print("Thank you for your inputs. Your password will be generated shortly.")
        else:
            print("""I'm sorry. There was an error with your inputs.
                  Please make sure that the number of upper case letters, 
                  special characters, and numbers are between 8 and 94 
                  inclusive and that your password is a minimum of 
                  8 characters long. These are the minimum 
                  requirements for a safe password.""")
    else:
        print("""I'm sorry. There was an error with your inputs. 
        The number of lower case letters, upper case letters, 
        special characters, and numbers in your password must 
        be equal to the length of your password and between 
        8 and 94 characters inclusive.""")


# In[ ]:


# A function to randomize characters. 
def randomize_characters(characters):
    random.shuffle(characters)


# In[ ]:


def characters_generator(num_upper, num_special, num_digits):
    randomize_characters(lower_case)
    randomize_characters(upper_case)
    randomize_characters(special)
    randomize_characters(digits)
    
    upper_slice = upper_case[:num_upper]
    special_slice = special[:num_special]
    digits_slice = digits[:num_digits]
    
    characters_list = list(lower_case + upper_slice + special_slice + digits_slice)
    return characters_list


# In[ ]:


def preliminary_password():
    while True:
        if len(prelim_password_list) < pw_length:
            try:
                prelim_list = characters_generator(num_upper, num_special, num_digits)
                randomize_characters(prelim_list)
                variable = prelim_list.pop()
                prelim_password_list.append(variable)
                prelim_list.append(variable)
                return prelim_password_list
            except: 
                print("There's an error in preliminary_password!")
                break
        else:
            print(f"""Error preliminary_password:
                  You limited your password to {pw_length} characters!""")
            break


# In[ ]:


def generate_prelim_password(prelim_password_list):
    while True:
        if len(prelim_password_list) < pw_length:
            try:
                for i in range(0, pw_length):
                    prelim_password_list = preliminary_password()
                return prelim_password_list
            except:
                print("There's an error in generate_prelim_password!")
                break
        else: 
            print(f"""Error generate_prelim_password: 
                You limited your password to {pw_length} characters!""")
            break


# In[ ]:


# editing copy
def password_character_check(characters_set, num_characters, prelim_password_list):
    # Note: characters_set <=> upper_case, special, or digits
    # Note: num_characters <=> num_upper, num_special, num_digits
    # Note: prelim_password_list <=> prelim_password_list from generate_prelim_password
    
    
    # Find the number of extra characters in prelim_password_list
    intersection_char = [char for char in prelim_password_list if char in characters_set]
    length_intersect_char = len(intersection_char)
    difference_char = abs(length_intersect_char - num_upper)
    intersection_lower = [char for char in prelim_password_list if char in lower_case]
    
    if length_intersect_char < num_characters: # Check against user input
        randomize_characters(characters_set) 
        prelim_password_list.extend(characters_set[:difference_char]) # Add extra char to prelim_password_list
        extra_lower = intersection_lower[:difference_char] # Find extra lower case characters
        for char in extra_lower:
            prelim_password_list.remove(char) # Remove extra lower case characters
        print("Added characters! Removed lower case letters!")
        return prelim_password_list
    elif length_intersect_char > num_characters:  # Check against user input
        randomize_characters(lower_case)
        extra_char = intersection_char[num_characters:] # Find extra characters
        for char in extra_char:
            prelim_password_list.remove(char) # Remove extra characters
        prelim_password_list.extend(lower_case[:difference_char]) # Add extra lower case to prelim_password_list
        print("Removed characters! Added lower case letters!")
        return prelim_password_list
    else:
        pass


# In[ ]:


def password_length_check(prelim_password_list):
    if len(prelim_password_list) > pw_length:
        return prelim_password_list[:pw_length]


# In[ ]:


# This function gets length of password and joins characters into a string. 
def password_string(prelim_password_list):
    new_password = "".join(prelim_password_list)
    return new_password


# In[ ]:


def password_character_check(characters_set, num_characters, prelim_password_list):
    # Note: characters_set <=> upper_case, special, or digits
    # Note: num_characters <=> num_upper, num_special, num_digits
    # Note: prelim_password_list <=> prelim_password_list from generate_prelim_password
    
    # Find the number of extra characters in prelim_password_list
    intersection_char = [char for char in prelim_password_list if char in characters_set]
    length_intersect_char = len(intersection_char)
    difference_char = abs(length_intersect_char - num_characters)
    intersection_lower = [char for char in prelim_password_list if char in lower_case]
    
    if length_intersect_char < num_characters: # Check against user input
        randomize_characters(characters_set) 
        prelim_password_list.extend(characters_set[:difference_char]) # Add extra char to prelim_password_list
        extra_lower = intersection_lower[:difference_char] # Find extra lower case characters
        for char in extra_lower:
            prelim_password_list.remove(char) # Remove extra lower case characters
        return prelim_password_list
    elif length_intersect_char > num_characters:  # Check against user input
        randomize_characters(lower_case)
        extra_char = intersection_char[num_characters:] # Find extra characters
        for char in extra_char:
            prelim_password_list.remove(char) # Remove extra characters
        prelim_password_list.extend(lower_case[:difference_char]) # Add extra lower case to prelim_password_list
        return prelim_password_list
    else:
        pass


# In[ ]:


def password_checks_loop(preliminary_password_list):
    while True:
        # Check preliminary password length with user input
        password_length_check(prelim_password_list)

        # Check to see if preliminary password meets minimum requirements
        # and create a new password if the preliminary password does not
        # meet the minimum requirements.
        password_character_check(upper_case, num_upper, prelim_password_list)
        password_character_check(special, num_special, prelim_password_list)
        password_character_check(digits, num_digits, prelim_password_list)
        
        # Find the number of lower_case characters in password
        intersection_lower = [char for char in prelim_password_list if char in lower_case]
        length_intersect_lower = len(intersection_lower)
        
        # Find the number of upper_case characters in password
        intersection_upper = [char for char in prelim_password_list if char in upper_case]
        length_intersect_upper = len(intersection_upper)
        
        # Find the number of special characters in password
        intersection_special = [char for char in prelim_password_list if char in special]
        length_intersect_special = len(intersection_special)
        
        # Find the number of digits characters in password
        intersection_digits = [char for char in prelim_password_list if char in digits]
        length_intersect_digits = len(intersection_digits)

        if len(intersection_upper) == num_upper:
              if len(intersection_special) == num_special:
                    if len(intersection_digits) == num_digits:
                        if len(intersection_lower) > num_lower:
                            randomize_characters(lower_case)
                            extra_lower = intersection_lower[num_lower:] # Find extra characters
                            for char in extra_lower:
                                prelim_password_list.remove(char) # Remove extra characters
                            return prelim_password_list
                            break
                            
                        elif len(intersection_lower) < num_lower:
                            randomize_characters(lower_case)
                            difference_lower = abs(length_intersect_lower - num_lower)
                            prelim_password_list.extend(lower_case[:difference_lower]) # Add extra char to prelim_password_list
                            return prelim_password_list
                            break
                        elif len(intersection_lower) == num_lower:
                            return prelim_password_list
                            break


# In[ ]:


# Lists of characters for passwords
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lower_case = letters.split()
upper_case = letters.upper().split()
digits = "0 1 2 3 4 5 6 7 8 9".split()
special = """! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~""".split()
characters_total = list(lower_case + upper_case + digits + special)


# In[ ]:


# User input functions:
pw_length = password_length()
# num_lower = choose_lower()
num_upper = choose_upper()
num_special = choose_special()
num_digits = choose_digits()

num_lower = (pw_length - num_upper - num_special - num_digits)

check_user_inputs(pw_length, num_lower, num_upper, num_special, num_digits)


# In[ ]:


# Generate a preliminary character list using user inputs
characters_list = characters_generator(num_upper, num_special, num_digits)
prelim_password_list = []
prelim_password_list

# Generate a preliminary password list using user inputs
prelim_password_list = generate_prelim_password(prelim_password_list)
prelim_password_list


prelim_password_list

# Run password checks until it meets criteria.
password_checks_loop(prelim_password_list)


# Shuffle updated characters one more time. 
randomize_characters(prelim_password_list)


# Combine password_list elements into a string. 
new_password = password_string(prelim_password_list)
print(f"""\nThank you for using the password generator app. 
      Your new password is:\n\n {new_password} \n\n Goodbye!""")


# In[ ]:


test = """hug,RSy9nfjP>aKlq5e(7a4cwzh>rlfu""".replace("", " ")
test = test.split()
test


# In[ ]:


len(test)


# In[ ]:


intersection_lower = [char for char in test if char in lower_case]
length_intersect_lower = len(intersection_lower)
length_intersect_lower


# In[ ]:


intersection_upper = [char for char in test if char in upper_case]
length_intersect_upper = len(intersection_upper)
length_intersect_upper


# In[ ]:


intersection_special = [char for char in test if char in special]
length_intersect_special = len(intersection_special)
length_intersect_special


# In[ ]:


intersection_digits = [char for char in test if char in digits]
length_intersect_digits = len(intersection_digits)
length_intersect_digits

