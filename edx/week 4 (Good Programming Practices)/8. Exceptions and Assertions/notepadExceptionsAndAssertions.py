# notepad exceptions and assertions

"""
WHAT TO DO WITH EXCEPTIONS?
- return a "error" value
	- what value to choose?
	- complicates code having to check for a special value
- stop execution, SIGNAL ERROR condition
	 - in python: RAISE AN EXCEPTION
	 ex -> raise Exception ("descriptive string")

DEALING WITH EXCEPTIONS
Python code can provide HANDLERS for exceptions	
"""
try:
    a = int(input("tell me a number: "))
    b = int(input("tell me another: "))
    print(a / b)
    print("ok")
except:
    print("there is bug")
print("outside")

"""
exceptions RAISED by any statement in body of TRY are HANDLED by the EXCEPT statement and executions continues after the body of the EXCEPT statement 

"""
