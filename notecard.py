from sys import argv

prompt = "> "

print "this replaces the checklist notecard." 

print "Did you start your function definition with def?" 
fo = raw_input(prompt)

print "Does your function name have only characters and _ underscore) characters?"
foo = raw_input(prompt)

print "Did you put an open parenthesis ( right after the function name?"
fooo = raw_input(prompt)

print "Did you put your arguments after the parentheis ( separated by commas?" 
foooo = raw_input(prompt)

print "Did you make each argument unique (meaning no duplicated names)?"
fooooo = raw_input(prompt)

print "Did you put a close parenthesis and a colon ): after the arguments?"
foooooo = raw_input(prompt)

print "Did you indent all lines of code you want in the function four spaces? No more, no less."
fooooooo = raw_input(prompt)

print "Did you end your function by going back to writing with no indent (dedenting we call it)?"
foooooooo = raw_input(prompt)

print "Okay, so %r %r %r %r %r %r %r %r." %  (fo, foo, fooo, foooo, fooooo, foooooo, foooooo, fooooooo)