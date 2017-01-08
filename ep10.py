#define them strings
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#practice with escape characters
flashcards = '''
\\\ gives you a backslash
\\' single-quote
\\" double-quote
\\a ASCII bell (BEL)
\\b ASCII backspace (BS)
\\f ASCII formfeed (FF)
\\n ASCII linefeed (LF)
\\N{name} Character named name in the Unicode database (Unicode only)
\\r Carraige Return (CR)
\\t Horizontal Tab (TAB)
\\uxxxx Character with 16-bit hex value xxxx (u" string only)
\\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (u" string only)
\\v ASCII verticle tab (VT)
\ooo Character with octal value ooo
\\xhh Character with hex value hh
'''

#Print all the strings
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#study hard!
print "These are a few of my favorite escape characters"
print flashcards

#Cntrl+C to escape. Else, this is the song that never ends
while True:
     for i in ["/","-","|","\\","|"]:
         print "%s\r" % i,
