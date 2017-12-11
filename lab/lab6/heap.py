#!/usr/local/bin/python3.5
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
# Bryna Zhao

import heapq

def process(input):
    if input != None:
        lines = input.split('\r\n')
        q = []
        for line in lines:
            if line != '': 
                print("<br>")
                print("You entered: " +line)
                print("<br>")
                print("Print: ")
            if line == "DUMP":
                # a heap is not sorted
                q.sort()
                for item in q:
                    print(item)
            elif line == "FIRST":
                if len(q) == 0:
                    raise IndexError("Empty queue!")
                    break                
                print(q[0])
            elif line == "REMOVE":
                if len(q) == 0:
                    raise IndexError("Empty queue!")
                    break
                next = heapq.heappop(q)
                print(next)
            else:
                if len(line) == 0:
                    continue
                # can't use split(' '), since stirng might contain spaces 
                spacepos = line.find(' ')
                before = line[:spacepos]
                if before != "INSERT":
                    print(before)
                    raise ValueError("Invalid input!")
                    break
                insert = line[spacepos+1:]
                commapos = insert.find(',')
                value = insert[:commapos]
                string = insert[commapos+1:]
                #print("value is " + value)
                #print("string is " + string)
                value = int(value)
                heapq.heappush(q,(value,string))

import cgi, cgitb
cgitb.enable()

#print the http response header
print("Content-Type: text/html\n");

formInfo = cgi.FieldStorage()
userInput = formInfo.getvalue("program")
process(userInput)
