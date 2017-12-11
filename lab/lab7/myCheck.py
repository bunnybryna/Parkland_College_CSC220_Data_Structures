from chain_hash_map import ChainHashMap

filename = 'mydict.txt'
#filename = '/home/staff/kurban/public/lists/web2.txt'

theDict = ChainHashMap()

for piece in open(filename).read().lower().split():
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        theDict[word] = 1 + theDict.get(word, 0)
        
for word in theDict:
    print(word + " : " + str(theDict[word]))

sentence = "This is delight"
myList = sentence.lower().split()

notInDict = list()
print(notInDict)

for word in myList:
    if word not in theDict:
        print(word)
        notInDict.append(word)
        
print(notInDict)
