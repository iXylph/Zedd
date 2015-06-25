from sys import argv #imports argument variables from "sys"

script, filename = argv 
#defines what the argument variables will be. Asks user for certain data - uses argv to GET a file name. 

txt = open(filename) #in this case, we want to open ex15_sample.txt - this defines the variable txt to be referenced by open(filename) - just attributes the values of the text document (which is a file object). Python
#can now read this. 

print "Here's your file %r:" %filename  #also just prints a little message. 
print txt.read() ; txt.close() #calls read function on txt. Open pulls a file, but it doesn't do anything else until you tell it to. Then, it closes the file to free resources. 
#file can be given a command by using period. txt.read() actually says "read with no parameters." Commands also known as functions/methods. 
#closes the text that was previously opened in open(filename)print "Type the filename again:"  #this line can commented out to just run the file. open(filename) is the prefered method of opening a file, because it takes many less lines to do this. 
file_again = raw_input ("> ")

txt_again = open(file_again)

print txt_again.read() ; txt_again.close()