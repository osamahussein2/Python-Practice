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