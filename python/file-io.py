## Open / Open Modes

# open() returns a file object
fileobject = open('filepath', 'mode')
# r = read (default)
# w = write, truncate
# r+ = read/write
# w+ = read/write, truncate
# a+ = read/append
# truncate means if the file has data in it when you write to the file 
# it removes the data that was already in the file

# Real Example
database = open('database.txt')
database.close()


# It is good practice is to use the 'with' keyword when dealing with file objects
# When the 'with' keyword is used is the file gets properly closed 
with open('filename') as fileobject:
    read_file = fileobject.read()


