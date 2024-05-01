# I learned some Python code here: https://www.learnpython.org/

print("My name is Osama Hussein and I am practicing writing this script in Python language, while learning more about Python on the go!")

r = 2;

if r == 2:
    print("r is equal to 2!");

integerValue = 9;
print(integerValue);

floatValue = 9.2;
print(floatValue);

floatValue2 = float(9.55);
print(floatValue2);

hi = 'hi';
print(hi);

helloThere = "hello there"
print(helloThere);

# So using double quotations inside a string makes it easier to this program that apostrophes are included
# inside the string compared to single quotations where using apostrophes would not be detected inside the string

six = 6;
four = 4;
sumOfNumbers = four + six;

print(sumOfNumbers);

welcome = "Welcome";
to = "to";
python = "the Python language!"

pythonString = welcome + " " + to + " " + python;
print(pythonString);

two, four = 2, 4;
print(two, four);

# If there is a number variable and a string inside the print function, the program will print an error since
# the program cannot convert a number variable to a string, and vice versa

arrayOfList = [];
arrayOfList.append(4);
arrayOfList.append(12);
arrayOfList.append(9);

# Print the list seperately each time
print(arrayOfList[0]);
print(arrayOfList[1]);
print(arrayOfList[2]);

# Print the list all at once
for listsDeclared in arrayOfList:
    print(listsDeclared);

arithmeticNumber = 3 + 4 * 5 / 4.0;
print(arithmeticNumber);

remainder = 47 % 4;
print(remainder);

powerOfTwo = 6 ** 2;
print(powerOfTwo);

powerOfFive = 6 ** 5;
print(powerOfFive);

# Using operators with strings

hiThere = "Hi" + " " + "there!";
print(hiThere);

# Multiplying a string by any number will repeat that string to the console at that number

repeatOsama = "Osama! " * 6;
print(repeatOsama);

# Making an operator of lists

codingLanguages = ["C++ ", "C# ", "Python ", "Javascript "];
number = [7, 4, 5, 9];

stringNumbers = codingLanguages + number;
print(stringNumbers);

# Initializing a new list of repeating sequences

repeatList = ["What? ", "Who? ", "Where? ", "Why? ", "How? "];
print(repeatList * 4);

myName = "Osama"
introduceName = "This is %s"

print(introduceName % myName); # The % is for correctly formatting a string to the console

# Using two or more argument specifiers to format strings and numbers (requires the use of parentheses)

batmanArkhamSeries = "The Batman Arkham series has released";
numberOfGames = 4;
batmanArkhamGames = "Including Batman Arkham Asylum, Batman Arkham City, Batman Arkham Origins, and Batman Arkham Knight!"

print("%s %d games. %s" % (batmanArkhamSeries, numberOfGames, batmanArkhamGames));

# An object that isn't a string can be formatted using %s

numbers = [];

numbers.append(3);
numbers.append(5);
numbers.append(8);

for counter in numbers:
    print("Numbers list: %s" % counter)

welcomeBack = "Welcome back to programming Python!";

print(len(welcomeBack)); # len function counts how many characters there are in a string, including spaces
print(welcomeBack.index("p")); # The index of this string finds where the character of the p letter first occurs at
print(welcomeBack.count("o")); # The count function counts the number of o's in this string
print(welcomeBack[10:18]); # Prints this string at the first index I defined to the last index I defined
print(welcomeBack[20:34:3]); # Prints this string at the first index to last index but will skip 3 characters inside those indexes
print(welcomeBack[::-1]); # Prints the reversed version of this string
print(welcomeBack.upper()); # Prints the whole string using capital(uppercase) letters
print(welcomeBack.lower()); # Prints the whole string using lowercase letters
print(welcomeBack.startswith("Welcome")); # Checks if my string starts with a certain string (prints true or false)
print(welcomeBack.endswith("py")); # Checks if my string end with a certain string (prints true or false)

splitWelcomeBack = welcomeBack.split(); # Splits the string to a list of grouped characters
print(splitWelcomeBack);