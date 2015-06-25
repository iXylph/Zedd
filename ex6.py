x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #references %s elements in order; so binary, and then do_not.

print x
print y

print "I said: %r." % x #This will print the raw input of X. 
print "I also said: '%s'." % y #this will print a string-format of Y. 

hilarious = False #this notes that the variable hilarious is indeed false. 
joke_evaluation = "Isn't that joke so funny?! %r" # %r is raw format. 

print joke_evaluation % hilarious #references variable hilarious and prints it into the string evaluation. 

w = "This is the left side of..."
e = "a string with a right side." 

print w + e #this prints the amalgamation of w + e, although it should be w + w + e, because JOHNNN CENA. 

