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
For example,
```
> echo hello world
hello world
```

## Variables
In the 4001 language, variables can store numbers (they can be integers or decimals). Variable names can include uppercase and lowercase letters and numbers. All signs except the **'\_'** sign are not allowed. When using a variable in the code, the **%** sign remains on both sides of it.
For example,
If we had a variable named test_2 in which the value 7 was stored then we would have:
```
> echo value is %test_2%
value is 7
```
