#easy 1#
def getlast(string):
    words=string.split()
    if len(words)>0:
        lastword=words[-1]
        return len(lastword)
    else:
        return 0
string="hello world"
lastword_length=getlast(string)
print(lastword_length)    