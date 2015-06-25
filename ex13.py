from sys import argv #add features to script from Python featuer set; Python doesn't use all features at once, and instead asks what you want. also acts as documentation for other programmers. 
#argv is "argument variable" - holds the arguments you pass to your Python script when ran. 
#Line 3 "unpacks" argv - doesn't hold all the arguments, but gives four variables to work with. "Take whatever is in argv, unpack it, and assign it to all of these variables in order." 

script, first, second, third = (argv) #this assigns the argument variables - script, first, second, and third in this case - you reference them later.
	#furthermore, take note that the "script" argument variable returns the name of your script. The others, you assign values to. 
fourth = raw_input("What is your fourth variable? ") #this asks users to define a variable. Would be useful in, say, a text-based RPG. 

print "All together, your script is called %r, your first variable is called %r, your second variable is called %r, your third variable is called %r, and your fourth variable is called %r." % (script, first, second, third, fourth)