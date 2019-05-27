"""
week 4 - testing and debugging

- defensive programming
	- write specifications for functions
	- modularize programs
	- check conditions on inputs / outputs (assertions)

- testing
	- compare input / output pairs to specification
	- its not working!
	- how can i break my program? 

- eliminate source of bugs - debugging 
	- study events - leading up to an error
	- why is it not working?
	- how can I fix my program?

CLASS OF TESTS
- from the start, design code to ease this part
- break program into modules that can be tested and debugged individually
- document constraints on modules
	- what do you expect the input to be? the output to be?
- document assumptions behind code design 

WHEN ARE YOU READY TO TEST?
- ensure code runs
	- remove syntax errors
	- remove static semantic errors
	- Python interpreter can usually find these for you
- have a set of expected results
	- an input set
	- for each input, the expected output 

CLASSES OF TESTS:
- UNIT TESTING
	- validate each piece of program
	- TESTING EACH FUNCTION SEPARATLY
- REGRESSION TESTING
	- add test for bugs as you find them in a function
	- CATCH REINTRODUCED errors that were previously fixed
- INTEGRATION TESTING
	- does OVERALL PROGRAM WORK?
	- >>tend to rush to do this<<

TESTING APPROACHES:
- INTUITION - about natural boundaries of the problem:
can you come up with some natural partitions?
	- if no natural partitions, might do RANDOM TESTING:
		- probability that code is correct increases with more tests
		- better options below:

- BLACK BOX testing
explore paths through specification
designed WITHOUT LOOKING at the code
can be done by someone other than the implementer to avoid some implementer BIASES
testing can be REUSED if implementation changes
PATH through specification:
	- build test cases in different natural space partitions 
	- also consider boundary conditions (empty lists, singleton list, large numbers, small numbers)

- GLASS BOX testing 
explore paths through code 
USE CODE directly to guide design to test cases
called PATH-COMPLETE if every potential path through code is tested at least once
- what are some DRAWBACKS of this type of testing?
	- can go through loops arbitrarily many times
	- missing paths
- guidelines
	- branches -> exercise all parts of a conditional
	- for loops -> loop not entered / body of loop executed exactly once or more than once
	- while loops -> same as for loops, cases that catch all ways to exit loop
 
 BUGS:
 - what you could do:
 	- isolate the bugs
 	- eradicate the bug
 	- retest until code runs correctly

 
 RUNTIME BUGS:
 - overt vs convert:
 	- OVERT - has a obvious manifestation - code crash or run forever
 	- CONVERT - no obvious sign - code return a value, which may be incorrect but hard to determine
 - Persistent vs intermittent:
 	- PERSISTENT - occurs every time code is run
 	- INTERMITTENT - only some times 

CATEGORIES OF BUGS:
- overt and persistent:
	- obvious to detect
	- Good programmers use DEFENSIVE PROGRAMMING to try to ensure that if error is made, bug will fall into this category
- overt and intermittent
	- more frustrating, can be harder to debug, but if conditions that prompt bug can be reproduced, can be handled
- convert
	- highly dangerous, as users may not realize answers are incorrect until code has been run for long period

DEBUGGING
- steep learning curve
- goal is to have bug - free program
- tools:
	 - build in to IDLE and Anaconda
	 - Python Tutor
	 - print statement
	 - use your brain, be systematic in your hunt 

PRINT STATEMETS:
- good way to TEST HYPOTHESIS
- when to print:
	- enter function
	- parameters
	- function results
- use BISECTION METHOD
	- put print halfway in code
	- decide where bug may occur

ERROR MESSAGES -> EASY 
- IndexError
	- test = [1,2,3] -> test[4]
	- trying to access beyond the limits of a list
- TypeError
	- int(test)
	- converting inappropriate type
- NameError
	- a
	- referencing a non-existent variable
- TypeError
	- '3'/4
	- mixing data types without appropriate coercion
- SyntaxError
	- a = len([1,2,3] 
	print a
	- forgetting to close parenthesis, quotation

>>>>>>>>>>>>>>>>>
LOGIC ERRORS -> HARDER
- THINK before writing new code
- DRAW pictures, take a break
- EXPLAING the code to 
>>>>>>>>>>>>>>>>

DEBUGGING STEPS:
- STUDY program code
	- ask how did I get the unexpected result
	- DON'T ASK WHAT IS WRONG
	- is it part of a family?
- SCIENTIFIC METHOD
	- study available data
	- form hypothesis
	- repeatable experiments
	- pick simplest input to test with

DON'T:
- write entire program
- test entire program
- debug entire program

DO:
- write a function
- test the function, debug the function
- write a function
- test the function, debug the function
- etc.

DON'T:
- change code
- remember where bug was
- test code
- FORGET WHERE BUG WAS OR WHAT CHANGE YOU MADE
- panic :(

DO:
- backup code
- change code
- write down potential bug in a comment
- test code
- compare new version with old version

DEBUGGING SKILLS:
- treat as a search problem:
	- looking for explanation for incorrect behaviour
	- study avaliable data - both correct test cases and incorrect ones
	- form an hypothesis consistent with the data
	- design and run a repeatable experiment with potential to refute the hypothesis
	- keep record of experiments performed: use narror range of hypotheses

DEBUGGING AS SEARCH:
- want to narrow down space of possible sources of error
- design experiments that expose intermediate stages of computation (use print statements!), and use results to further narrow search
- binary search can be a powerful tool for this

SOME PRAGMATIC HINTS:
- look for the usual suspects
- ask why the code is doing what it is, not why it is not doing what you want
- the bug is probably not where you think it is - eliminate locations
- explain the problem to someone else
- don't belive the documentation
- take a break and come back to the bug later

"""
