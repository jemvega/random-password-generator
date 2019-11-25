# Password Generator App

## Background
I was motivated to create this app out of curiosity and for fun. I was interested in creating a password generator that allowed permutations with repetitions of characters, creating a password that could be generated from user inputs, and checking whether the password that was generated fit the minimum requirements and the user defined criteria.

## Features of the Password Generator App
The password generator is a program that will generate a random password for the user. The user will be allowed to input how many upper case letters, special characters, and numbers/digits, he or she wants in a password. The minimum requirements for a password are that the user's password must be between 8 and 94 characters long and have at least one of the following:
        -An upper case letter, 
        -A lower case letter,
        -A number, 
        -A special character.

Features of this password generator include:
        -The password will be generated using ASCII printable characters.
        -The generated password is a permutation with repetition allowed.
		-Each password is generated randomly. 

### Prerequisites
This app was created using Jupyter Notebook for Python.

## Getting Started
This app requires Python. Simply run the code in an interactive development environment or Python interpreter.

## Tests
As of right now, I have only been manually testing the app. I created a few functions that would check whether the password fit the minimum requirements and the user defined criteria. I would like to create integration test checks and unit test checks. 

## Known Issues
There are no known issues with this app. 

## Future Features
Here are some features I would like to add in the future:
* As of right now, the password generator creates passwords from 8 to 94 characters, but this is arbitrary. Perhaps in the future I will change these requirements to be between 4 and 128 characters, but most passwords are required to be at least 6 or 8 characters. 
* It would be interesting to change the character set lists to be symbols different from the ASCII printable characters.  
* While adding more restrictions is not conducive to an increase in security, I may see if I limit repetions of consecutive letters, have a character position requirement, or remove repetitions altogether. 

## Built With

[Python] (https://www.python.org/downloads/) programming language
[Anaconda Navigator] (https://docs.anaconda.com/anaconda/navigator/) GUI
[Notepad++] (https://notepad-plus-plus.org/) for README.md and LICENSE.txt

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

* **Jem Vega** - *Initial work* - [JemVega](https://github.com/JemVega)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

