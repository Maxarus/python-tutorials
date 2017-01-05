#declares variables
#adds 10 in to the variable x string
x = "There are %d types of people." % 10
#declares binary
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#prints x and y
#bad joke those who know binary and those who don't
#one string within a string
print x
#two strings within a string
print y

#Another way of saying there are 10 types of people
print "I said: %r." % x
print "I also said: '%s'." % y

#declares hilarious
hilarious = False
#Is that joke funny? False
joke_evaluation = "Isn't that joke so funny?! %r"

#confirms, not funny
#String within a string
print joke_evaluation % hilarious

#declaes two sides of a string
w = "This is the left side of..."
e = "a string with a right side."

#adding strings simply concatenates them
#two strings within a string
print w + e
