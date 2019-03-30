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
    # in sublime input won't work!
    # a = int(input("tell me a number: "))
    # b = int(input("tell me another: "))
    a = 3
    b = 0
    print(a / b)
    print("ok")
except ValueError:
    print("there is value bug")
except ZeroDivisionError:
    print("divide by zero")
except:
    print("other bug")
print("outside")


"""
exceptions RAISED by any statement in body of TRY are HANDLED by the EXCEPT statement and executions continues after the body of the EXCEPT statement 

other exceptions
else:
	body of this is executed when execution of associated TRY body  COMPLETES WITH NO EXCEPTIONS
finally:
	- body of this is ALWAYS EXECUTED after TRY, ELSE and EXCEPT clauses, even if they raised another error or executed a BREAK, CONTINUE or RETURN
	- useful for clean-up code that should be run no matter what else happened (eg. close a file)
"""

# example : control unit
data =[]
file_name = 'file.py'
try:
	fh = open(file_name,'r')
except IOError:
	print('cannot open', file_name)
else:
	for new in fh:
		if new != '\n':
			addIt=new[:1].split(',') #remove trailing \n
			data.append(addIt)
finally:
	fh.close() #close file even if 





