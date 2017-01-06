formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, False)
print formatter % (formatter, formatter, formatter, formatter)
# We use both single and double quotes to show the
# exactly what is in memory gets printed
print formatter % (
    'I had this thing.',
    'That you could type right.',
    "But it didn't sing.",
    'So I said goodnight.'
)
