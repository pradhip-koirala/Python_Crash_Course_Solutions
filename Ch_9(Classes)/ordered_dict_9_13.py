from collections import OrderedDict

glossary = OrderedDict()

glossary = {
    "variable": "A name used to store a value in memory",
    "data type": "The type of data a variable holds, such as int, float, string, or boolean",
    
    "list": "An ordered and changeable collection of elements stored inside square brackets []",
    "tuple": "An ordered but unchangeable collection of elements stored inside parentheses ()",
    "set": "An unordered collection of unique elements stored inside curly braces {}",
    "dictionary": "A collection of data stored in key : value pairs using curly braces {}",

    "if statement": "Used to check a condition and execute code only if the condition is true",
    "elif": "Used to check another condition if the previous if condition is false",
    "else": "Executes code when all if and elif conditions are false",

    "for loop": "Used to repeat a block of code for a specific number of times or over a sequence",
    "while loop": "Repeats a block of code as long as a condition remains true",

    "function": "A block of reusable code that performs a specific task",
    "parameter": "A variable used when defining a function",
    "argument": "A value passed to a function when calling it",

    "input": "Takes data from the user",
    "output": "Displays data to the user using print()",

    "operator": "A symbol used to perform operations like +, -, *, /, ==, >, <",
    "logical operator": "Used to combine conditions such as and, or, not",

    "index": "The position number of an element in a list or string, starting from 0",
    "slice": "Used to extract a part of a list or string",

    "string": "A sequence of characters enclosed in quotes",
    "integer": "A whole number without a decimal",
    "float": "A number with a decimal point",
    "boolean": "A data type that has only two values: True or False"
}


for k, v in glossary.items():
    print("Key:",k)
    print("Values:",v)
