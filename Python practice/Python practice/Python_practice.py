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

# Boolean logic to determine if a variable expression will return true or false

osamaNumber = 16;

print("Does osama's number return 16? " + str(osamaNumber == 16)); # str converts an int variable to a string
print("Does osama's number return greater than 20? " + str(osamaNumber > 20));

firstPlayingBatmanArkhamGame = "Batman Arkham Asylum";
secondPlayingBatmanArkhamGame = "Batman Arkham City";

# Boolean operators inside the if statement, using and/or conditionals

if firstPlayingBatmanArkhamGame == "Batman Arkham Asylum" and secondPlayingBatmanArkhamGame == "Batman Arkham City":
    print("You're playing Batman Arkham Asylum and Batman Arkham City!")

if firstPlayingBatmanArkhamGame == "Batman Arkham Asylum" or firstPlayingBatmanArkhamGame == "Batman Arkham City":
    print("Using the or operator: you're either playing Batman Arkham Asylum or Batman Arkham City!")

# The in operator checks if the object exists in the list

if firstPlayingBatmanArkhamGame in ["Batman Arkham Asylum", "Batman Arkham City"]:
    print("Using an iterator list: you're either playing Batman Arkham Asylum or Batman Arkham City!");

# Python's conditional statements don't require open brackets, only code blocks

if secondPlayingBatmanArkhamGame == "Batman Arkham City":
    print("You ARE playing Batman Arkham City after Batman Arkham Asylum!")

else:
    print("You are NOT playing Batman Arkham City after Batman Arkham Asylum!")

win1 = ["win"];
win2 = ["win"];

print(win1 == win2);

# The is operator doesn't match the values of the variables but only the instances of the variables
print(win1 is win2); # Prints false because the instance of win1 doesn't equal to win2

# The not operator is the opposite of the double equal operator, meaning that it makes a statement false or inverts it
print(not False);

playingBatmanArkhamGame = "";

if not playingBatmanArkhamGame:
    print("You're NOT playing the Batman Arkham games");

# Prints the numbers randomized from 12 to 26
for number in range(12, 27):
    print(number);

# Prints the numbers randomized from 10 to 19 but will increment by 3 each time instead of one by one
for number2 in range(10, 20, 3):
    print(number2);

counter = 0;

while counter < 10:
    counter += 2;
    print(counter);

playerMoves = 0;

while playerMoves >= 0:
    playerMoves += 1;
    print(playerMoves);

    if playerMoves >= 5:
        break;

for num in range(7):

    # If num is an odd number, then continue looping through the numbers
    if num % 1 == 0:
        continue;

    print(num);

# Else when this for loop above has finished, print to the console that we reached the final number in the loop
else:
    print("We reached the maximum number at " + str(num) + "!");

def decrementNumbers():
    
    number = 12;
    
    while number <= 12:
        
        number -= 2;
        print(number);
        
        if number <= 0:
            break;

def SpiderManGamesYouLike(gameName, releaseMonth, releaseDay, releaseYear):

    print("My favourite Spider-Man game was %s, which was released on %s %d, %d!" % (gameName, releaseMonth, releaseDay, releaseYear));

def SubtractVector2(Vector2ax, Vector2ay, Vector2bx, Vector2by):

    print("(" + str(Vector2ax) + "-" + str(Vector2bx) + ", " + str(Vector2ay) + "-" + str(Vector2by) + ")" +
          " = (" + str(Vector2ax - Vector2bx) + ", " + str(Vector2ay - Vector2by) + ")");
    return Vector2ax - Vector2bx, Vector2ay - Vector2by;

decrementNumbers();
SpiderManGamesYouLike("Spider-Man 2", "June", 29, 2004);
SubtractVector2(7, 6, 2, 3);

class Osama:
    good = "Good";

    def GetYourOwnLife(self):
        print("Get your own life!");

osamaObject = Osama();
print(Osama.good);

osamaObject2 = Osama();
osamaObject2.good = "Bad"; # Add another instance of the class and change its original string variable
print(osamaObject2.good);

osamaObject.GetYourOwnLife(); # Calling a function inside my class object

class WriteStrings:

    def __init__(self, string):
        self.string = string;
        
    def returnWrittenString(self):
        return self.string;

writeSomethingHere = WriteStrings("The more I learn Python, the better!");
print(writeSomethingHere.returnWrittenString());

# Dictionaries in Python allows you to store keys and values inside the square brackets instead of indexes

ps2GamesPlayed = {
    "Crash 'n' Burn" : "Released on November 15th, 2004!", 
    "Crash Bandicoot: Wrath of Cortex" : "Released on October 30th, 2001!",
    "Crash Twinsanity" : "Released on September 28th, 2004!"
    }

# Iterating over the dictionary, which doesn't keep the stored values in order (but iterates over key pairs)
for gameName, releaseDate in ps2GamesPlayed.items():
    print("PS2 games I played include %s. %s" % (gameName, releaseDate));

# Delete some of my stored keys inside the dictionary
del ps2GamesPlayed["Crash 'n' Burn"];
ps2GamesPlayed.pop("Crash Bandicoot: Wrath of Cortex");

# Print the PS2 games I played, including me deleting some keys from my defined dictionary
print(ps2GamesPlayed);

if "Crash 'n' Burn" not in ps2GamesPlayed:
    print("I have removed Crash 'n' Burn from my PS2 games played list!");

