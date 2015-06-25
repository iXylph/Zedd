from sys import argv

prompt = " >" 

print "Did you call/use/run this function by typing its name?" 
fo = raw_input(prompt)

print "Did you put the ( character after the name to run it?"
foo = raw_input(prompt)

print "Did you put the values you want into the parenthesis separated by commas?"
fooo = raw_input(prompt)

print "Did you end the function call with a ) character?" 
foooo = raw_input(prompt)

print "Okay, so %r %r %r %r ." % (fo, foo, fooo, foooo) 