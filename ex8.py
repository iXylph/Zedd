formatter = "%r %r %r %r" #assigns value %r %r %r %r to variable "formatter"

print formatter % (1, 2, 3, 4) #returns values 1, 2, 3, 4 in raw format. 
print formatter % ("one", "two", "three", "four") #returns values "one", "two", "three", "four" AKA strings in raw format. 
print formatter % (True, False, False, True) #returns values True, False, False, True (in that order) in raw format. 
print formatter % (formatter, formatter, formatter, formatter) #returns the string %r %r %r %r in raw format. 
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)