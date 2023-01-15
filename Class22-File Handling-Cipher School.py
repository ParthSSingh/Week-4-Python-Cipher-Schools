# File Access Modes
'''
Read Only ('r')
Read and Write ('r+') 
Write Only ('w')
Write and Read ('w+')
Append Only ('a')
Append And Read ('a+')
'''
# Opening File
file = open("rendom.txt","w")
file.write("I am Demon King")
file.write("\nThis world shall know pain ")
file.close()
# Writing To a file
'''
> write
> writelines
'''
file = open("rendom.txt", "w")
file.write("Izuku Or Naruto")
a = ["\nEren\n","Ichigo\n","Saitama\n","Itachi\n","Rintarou"]
file.writelines(a)
file.close()
# Reading from a file
'''
> read
> readline
> readlines
'''
file = open("sample.txt","r")
file.read()
print(file.read())
# Streams
# Iterables which can iterated in single direction
# They don't have starting and ending point
# Moving the cursor
# >seek(n): Takes the file handle to the nth byte from the beginning. 
#  Smarter Way of opening files..... 
# Context Programming
with open("rendom.txt","r") as file:
    print(file.read())

print(file.read())
class A:
    def __enter__(self):
        print("Entered")

    def __exit__(self, *args):
        print("Exitted")
        print(args)
        return True
with A() as x:
    print(x)
    print("inside context")
    raise Exception

print("Outside context")
# xml
# html
'''
<html>
    <body>
        Hello World
    </body>
</html>
'''
# JSON files
'''
{
    "html": {
        "body": "Hello World"
    }
}
'''
# JSON rule
'''
-- keys can only be strings and numbers
-- values can only be array, json, string, numbers, boolean & null
'''
#  JSON Example---
a = {
    "name": "izuku",
    "marks": "100",
    "languages": ["c#","js","python","go","rust"]
}
import json
s = json.dumps(a)
type(s)
print(s)