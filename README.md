# Random-Number-Generator-using-PI
Using values at indices of Pi and current Date/Time a 4-Digit random number is generated



In code_generator.py a method that will return a 4 digit random code.
Calculation of the code as the nth digit in pi based on the following 4 values:

Sum of the YY + DD + MM of “today’s” date (n_1)

Sum of the HH + MM + SS of the “current” time (n_2)

Sum of the first 5 digits (rounded) of the decimal portion of the seconds value from n_2 (n_3)

(n_1 + n_2 + n_3) mod 7 (n_4)

Clarification: nth value of pi indexed at zero from left to right.  i.e. n = 4 => 3.14159... => 5

In runner.py create a “main” that will call code_generator.py and print the resulting 4 digit random code.
