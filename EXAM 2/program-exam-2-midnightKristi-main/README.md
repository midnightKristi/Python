# program-exam-2
I am providing a partial solution. You need to provide the rest. 
This program evaluates prefix notation expressions. 
You need to provide code for is_float, apply, and parts of main

Use evaluator.py which is in this repository.

Submit evaluator.py to Code Post. There are several test files there for you to check your results with.

Here are several test inputs

```
+ 5 2
* 5 2
/ 5 2
% 5 2
- + * 2 3 * 5 4 9
+ - + * 2 3 * 5 8 9 % 5 3
quit
```

This is what your output should look like for the above sample input.
```
This program evaluates prefix expressions that
include the operators +, -, *, /, and %.

Expression? value = 7.0
Expression? value = 10.0
Expression? value = 2.5
Expression? value = 1.0
Expression? value = 17.0
Expression? value = 39.0
Expression? Exiting.
```
Here's another sample input
```
+ .5 .5
* .5 .5
/ .5 .5
% .5 .5
+ 24.5 74.2
- 24.5 74.2
* 24.5 74.2
/ 24.5 74.2
+ - + * 2.5 3.25 * 5 8.343 9.76 % 5.6 3.3
+ - + * 2.5 3.25 * 45 / 8.343 56 9.76 % 5.6 3.3
quit
```
Results
```
This program evaluates prefix expressions that
include the operators +, -, *, /, and %.

Expression? value = 1.0
Expression? value = 0.25
Expression? value = 1.0
Expression? value = 0.0
Expression? value = 98.7
Expression? value = -49.7
Expression? value = 1817.9
Expression? value = 0.33
Expression? value = 42.38
Expression? value = 7.37
Expression? Exiting.
```
