from sys import argv #imports argument variables from sys.
from os.path import exists #this imports the EXISTS function from the OS path, or the path, which signifies whether or not a file exists. 

script, from_file, to_file = argv #assigns these argument variables in order. 

print "Copying from %s to %s" % (from_file, to_file) #displays from_file and to_file in string format in the command line. 

# we could do these two on one line how? - placed a semicolon between functions to signify that it will be performing these functions in order. 
in_file = open(from_file) ; indata = in_file.read()

print "The input file is %d bytes long" % len(indata) #displays the length attribute of indata, which is just ex17_from.txt

print "Does the output file exist? %r" % exists(to_file) #states whether or not the file is located in the OS path. 
print "Ready, hit RETURN to continue, CTRL-C to abort." #brings you to the next line. 
raw_input("ENTER to continue, CTRL-C to abort.") 

out_file = open(to_file, 'w') #opens the argv to_file in write mode. 
out_file.write(indata) #writes data assigned to indata variable (which is ex17_from.txt) to out_file, (ex17_to.txt in write mode)

print "Alright, all done." #prints a statement to show the user that this particular conversion has been completed. 

out_file.close() #closes out_file. 
in_file.close() #closes in_file.