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

 





"""

