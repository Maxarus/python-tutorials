from datetime import datetime

filename = 'testes.txt'
print "opening the file..."
target = open(filename, 'a')

localtime = datetime.now()
print "Local current time :", localtime
print "I'm going to write these to the file."

target.write("Local current time :" + str(datetime.now()) + "\n" )
#target.write("\n")

print "And finally, we close it."
target.close()
