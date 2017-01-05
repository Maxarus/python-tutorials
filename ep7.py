#lets sing a song
print "Mary had a little lamb."
#injects a String directly, replicating exactly what is in memory
print "Its fleece was white as %r." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do? That added 10 periods..........

# creates way too many variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# lets improve on it
end = [end1,end2,end3,end4,end5,end6,end7,end8,end9,end10,end11,end12]

#improve again!

endx = ['C','h','e','e','s','e','B','u','r','g','e','r','!','!']
#prints out all the letters from all those variables.
print end1 + end2 + end3 + end4 + end5 + end6, #comma keeps it on the same line
#indicates not to include the standard '\n'
print end7 + end8 + end9 + end10 + end11 + end12

#prints our 'improvements'
for i in end:
    # print(i, end='')
    # print i+,
    print i,

print "\n"

for i in endx:
    print i
