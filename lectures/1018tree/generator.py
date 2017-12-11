def foo():
    print " begin "
    for i in range(3):
        #print (" before yield " + str(i))
        yield i
        #print (" after yield " + str(i))
    print (" end ")
    
    
def foobar():
    for i in range(3):
        yield i
        
# for value in foo():
    # print (value)
    
f = foo()
f.next()
f.next()
f.next()

def words():
    yield "This"
    yield "is"
    yield "a"
    yield "lot"
    yield "of"
    yield "typing"
    
for i in words():
    print(i)