from sys import argv #this imports the argument variable from "sys" which is the user settings on the computer
#pertaining to the script. 

script, user_name = argv #defines the argument variables as script and user_name
prompt = '> ' #the prompt (that displays on each line) displays an arrow - basic data entry location for users. 
date = raw_input ("What is the date?") #I played around with this and had a user enter the date, just to make the script a little more flashy. 
print "Hi %s, I'm the %s script. You are accessing me on %r" % (user_name, script, date) #
print "I'd like to ask you a few questions." #just prints a line; this is read in order on the script. 
print "Do you like me %s?" % user_name #this prompts the username that was previously defined in a string format, denoted by %s. 
likes = raw_input(prompt) #this then prompts the user for input, which also uses the > prompt. In the case of this, it is asking whether or not I like it. 

print "Where do you live %s?" % user_name #this prompts me to provide where I live, and later returns it in the bottom statement in line 21-26. 
lives = raw_input(prompt)

print "Hm. I'm not sure where that is. Could you tell me there that is %s?" % user_name #asks me for more data and returns my username again in string format. 
hood = raw_input (prompt) #this prompts me to provide where the hood is at. and later returns it in the bottom statement in line 21-26. 

print "What kind of computer do you have, %s ?"  % user_name #stores data to variable "computer" which will be returned in lines 21-26, while displaying a question drawing from the argv "user_name" which was previously defined. 
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. Can you tell me where that is at? 
Ah, so %r is where %r is at. Thanks!
And you have a %r computer. Nice.
""" % (likes, lives, hood, lives, computer) #returns all of these variables in raw format, just in case someone made something that was unreadable by the interpreter. 