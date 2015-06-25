from sys import argv #imports argument variables from sys. 

script, filename = argv #sets the argument variables. 

print "We're going to erase %r." % filename #this just displays what the function is going to do. 
print "If you don't want that, hit CTRL-C (^C)." #displays a way to close out of the prompt. 
print "If you do want that, hit RETURN." #moves forward with the function. 

raw_input("?") #gives a ? in the command line... - this is probably to ask a user if they want to do it or not. 

print "Opening the file..." #prints a line that states that it is currently opening the file. 
target = open(filename, 'r+') #opens the variable in write mode, denoted by 'w'. 

print "Truncating the file. Goodbye!" #displays that it's going to be truncating the file. AKA, deleting what is stored in the file. 
target.truncate() #actually runs the truncate command on "target" variable. NOTE: this isn't even necessary in this particular example, as the 'w' stated in the open function writes ONLY what is stated. :) 

print "Now I'm going to ask you for three lines." #asks for lines that are going to be stored to the new file. 

line1 = raw_input("line 1: ") #line 1 that is going to be stored to the new file. 
line2 = raw_input("line 2: ") #line 2 that is going to be stored to the new file. 
line3 = raw_input("line 3: ") #line 3 that is going to be stored to the new file. 

print "I'm going to write these words to each particular line." #prints a statement that it's going to write these lines.

target.write(line1) #uses a write function on target variable on line1 of said variable.  
target.write("\n") #writes this line on a new line. 
target.write(line2) #uses a write function on target variable on line2 of said variable. 
target.write("\n") #writes this line on a new line. 
target.write(line3) #uses a write function on target variable on line3 of said variable. 
target.write("\n") #writes this line on a new line. 

target = open(filename) #reopens the file object in read mode. 
print target.read() #prints the contents of the previously defined variable (which is ex16_sample.txt)

print "And finally, we close it." #prints a line that states it is going to close the file.
target.close() #closes the file. 