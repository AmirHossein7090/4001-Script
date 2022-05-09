# 4001-Script
A programming language that written in python, just for fun :)

## Two program execution modes
- In this case, your application displays a '>' sign, which means that it is ready to receive the command from the user, and after executing the command, shows the result to the user.
- In the other case, it gives a file to the program and the actions are performed line by line in the written file and the results appear on the page one after another.

## Syntax
Language 4001 is a function-based language and a function is called for each command and different parameters are sent to it depending on the need of the command.

## `echo` function
#### `syntax: echo <params>`
When displaying output, a character is spaced between any number of parameters given to display the sentence correctly.<br />
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
For example,<br />
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
Mathematical operations include four basic operations, namely +, -, \*, / (addition, subtraction, multiplication and division) as well as the operator ^ for power and # for remainder (modulus) and \ for correct division. (7 operators in total)<br />
**Note:** that the input must be controlled. Wrong operators or entering letters instead of numbers should be alerted to the user. Also note that numbers can have both positive and negative signs.
```
> calc <variable name> <expression>
```
In this case, the first parameter is the name of the variable in which the result must be stored, and the next parameters are the sections of the expression. After calculating the expression, this function stores the result in the variable and nothing is displayed. For example:
```
> calc test + 1 2 
> echo %test% 
3
```
Variables can also be used in mathematical expressions. The following is an example above:
```
> calc test * %test% 2 
> echo %test% 
6
```
This function can also be used to store a numeric value in a variable. In the following example, the value of the test variable is equal to 5:
```
> calc test 5
```
All parameters are functions of mathematical expression sections and after calculating the resulting expression is displayed to the user:
```
> calc + - * 2 3 4 5 
7
```
**Note:** Supports positive and negative decimal numbers (input controlled)

## `get` function
#### `syntax: get <variable name> <prompt>`
This function displays a message to the user and takes a numeric value (which can be a decimal or integer like the calc command) from the user and stores it in the variable. Note that this function must also have input control. Numbers can also be positive or negative.<br />
Example:
```
> get n 3
n=3
```

## `prims` function
#### `syntax: prims <n>`
This function is to display all prime numbers from 0 to n itself and each number is separated by a **","** sign:
```
> prims 7 
2, 3, 5, 7
```
This function can also take a variable as a parameter:
```
> calc b 5 
> prims %b% 
2, 3, 5
```

## `do` function
#### `syntax: do <n> <command>`
OR:
```
do <n> 
> <command 1> 
> <command 2> 
> ...
```
The do command is a repeating loop. This loop executes one or more commands n times. There are two ways to write a loop. In the first way to execute a command, the command can be written in the second parameter of the do function (the text of the command can also be spaced). In the second case, to execute several commands, the loop is defined first and then executed. In this case, the do function and the number of repetitions (n) are written in the first line. Your application then displays a **':'** character (expression point) to the user, which means that it is waiting to receive commands.<br />
Each command is then entered in a line until a line is left blank, which means the end of the loop, and the loop must be executed. If the entered command is invalid, an error message will be displayed to the user and the loop will be deleted.<br />
Example for a command:
```
> do 3 echo hello 
hello 
hello 
hello
```
Example of some commands:
```
> do 3 
: calc + 2 3 
: prims 9 
: 
5 
2, 3, 5, 7 
5 
2, 3, 5, 7 
5 
2, 3, 5, 7
```
The do function can get the number of repetitions from the variable. A command or commands can also contain variables as usual. Example:
```
> get n 5
n=5
> calc a 0 
> do %n% 
: calc a + %a% 1 
: echo %a% 
: 
1 
2 
3 
4 
5
```
Example 2:
```
> calc i 3 
> calc ii 4 
> do %i% echo %ii% 
4 
4 
4
```

## `open` & `close` function
#### `open syntax: open <file>`
#### `close syntax: close`
The open command causes your program to store all subsequent outputs in a file specified by the user until the user enters the close command; That is, by executing the close command, other outputs are not saved in the file. Note that the file name can also contain a space letter. After executing the open and close commands, the following messages should be displayed, respectively. In both of these messages, \<file\> is the name of the file specified by the user.
```
File "<file>" opened 
File "<file>" closed
```
Example:
```
> open test file.txt 
File "test file.txt" opened 
> echo hello 
hello 
> prims 10 
2, 3, 5, 7 
> calc + + + + 1 2 3 4 5 
15 
> echo end 
end 
> close 
File "test file.txt" closed
```
The contents of the "test file.txt" file are as follows:
```
hello 
2, 3, 5, 7 
15 
end
```
Note that blank lines are not written in the file.<br />
Also, all or part of the file name can be variable. Example:
```
> calc i 0 
> do 5 
: calc i + %i% 1 
: open test%i%.txt 
: echo hi file %i% 
: close 
: 
hi file 1 
hi file 2 
hi file 3 
hi file 4 
hi file 5
```
As a result of executing the above code, five files named *test1.txt* to *test5.txt* are created.

## `read` function
#### `syntax: read <file>`
This function is used to display a file. Here, too, filenames can also contain spaces. for example:
```
> read test file.txt 
hello 
2, 3, 5, 7 
15 
end
```
In this function, part of the file name can also be variable.

## `run` function
#### `syntax: run <file>`
This command is to open a script in **4001 language**. :)<br />
Your program must be able to execute the file received in the parameter. The commands in this file are written line by line. As with previous functions, part of the script file name can be variable.<br />
Example of a script and its execution (without variables):
```
echo hello this is test script 
calc - # ^ 5 2 11 3 
prims 7 
open output.txt 
echo output file begins 
calc + 2 3 
close 
echo file closed 
pause
```
Now, we run it:
```
> run test.script 
hello this is test script 
0 
2 3 5 7 
File "output.txt" opened 
output file begins 
5 
file "output.txt" closed 
file closed 
Please press ENTER to continue...
```
This function can also read and execute **do commands**. (Plz see the "test.script" file in this repo)
<br />
<br />
*Thank you for your look.*
