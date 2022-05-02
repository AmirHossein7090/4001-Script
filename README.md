# 4001-Script
A programming language that written in python, just for fun :)

## Two program execution modes
- In this case, your application displays a '>' sign, which means that it is ready to receive the command from the user, and after executing the command, shows the result to the user.
- In the other case, it gives a file to the program and the actions are performed line by line in the written file and the results appear on the page one after another.

## Syntax
Language 4001 is a function-based language and a function is called for each command and different parameters are sent to it depending on the need of the command.

## `echo` function
#### `syntax: echo <params>`
When displaying output, a character is spaced between any number of parameters given to display the sentence correctly.
This function receives and displays countless parameters as snippets.
For example,
```
> echo hello world
hello world
```
```
> echo hello this is an example
hello this is an example
```

## Variables
In the 4001 language, variables can store numbers (they can be integers or decimals). Variable names can include uppercase and lowercase letters and numbers. All signs except the **'\_'** sign are not allowed. When using a variable in the code, the **%** sign remains on both sides of it.
For example,
If we had a variable named test_2 in which the value 7 was stored then we would have:
```
> echo value is %test_2%
value is 7
```

## `pause` function
#### `syntax: pause`
This function does not receive any parameters and is generally used to interrupt the program after displaying a result to the user. When this function is called, the program must display a specific and fixed message to the user and ask him to press the Enter key to continue the process. This message is in the following example:
```
> pause
Please press ENTER to continue...
```
**Important Note:** Since Python is not able to receive a single key, the user may press other keys and then press the enter key or, for example, send a sentence to your program. These cases do not need to be investigated and do not matter. This means, for example, that situations may occur that do not matter in this project:
```
> pause 
Please press ENTER to continue...user input before enter
```
The text that comes after **"..."** is the user input before the enter key. The only key that is effective is the enter key.

## `calc` function
#### `syntax: calc <variable name> <expression>`
This function is used for mathematical calculations and must be able to calculate a prefix mathematical expression.
Mathematical operations include four basic operations, namely +, -, \*, / (addition, subtraction, multiplication and division) as well as the operator ^ for power and # for remainder (modulus) and \ for correct division. (7 operators in total)

**Note** that the input must be controlled. Wrong operators or entering letters instead of numbers should be alerted to the user. Also note that numbers can have both positive and negative signs.
```
> calc <variable name> <expression>
```
In this case, the first parameter is the name of the variable in which the result must be stored, and the next parameters are the sections of the expression. After calculating the expression, this function stores the result in the variable and nothing is displayed.
