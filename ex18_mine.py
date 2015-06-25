# this one is like your scripts with argv
def print_two(*args): #def makes a function - def = define. Give function name. We called it, in this case, print two. Could be anything. *Args must be in parentheses. 
#line is ended with a COLON, and the next two things are INDENTED. Not the easiest way to make a function. We don't even need to unpack arguments (check line 8)
	arg1, arg2 = args #this stores arg1 and arg2 as the argument in a list, denoted by *args. 
	print "arg1: %r, arg2: %r" % (arg1, arg2) #prints arg1: with arg1 raw data, and arg2: with arg2 raw data.

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): #defines print_two_again with as arg1, arg2 on the same line
	print "arg1: %r, arg2: %r" % (arg1, arg2) #prints arg1: with arg1 raw data, and arg2: with arg2 raw data.
	
# this takes just one argument
def print_one(arg1): #defines "print_one" argument with one argument. 
	print "arg1: %r" % arg1 #prints arg1: with arg1 raw data. 

# this one takes no arguments
def print_none(): #defines "print none" function.
	print "I got nothin'." #prints line, bc no args. 

	
print_two("Zed","Shaw") #two arguments; the arguments are Zed and Shaw. 
print_two_again("Zed","Shaw") #two arguments. the arguments are Zed and Shaw. 
print_one("First!") #one argument. The argument here is "First!" 
print_none() # no arguments. just prints what is stored. 