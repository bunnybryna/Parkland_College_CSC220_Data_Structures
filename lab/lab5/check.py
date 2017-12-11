#!/usr/local/bin/python3.5
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
# Bryna Zhao

def isNum(string):
    for c in string:
        if not (c in "0123456789."):
            return False
    return True
    
def isOp(c):
    if c != "": 
        return (c in "+-*/^")
    else: 
        return False
        
def isVar(string):
    if string[0] in "abcdefghijklmnopqrstuvqxyz":
        return True
    else:
        return False
        
def hasVar(stringList):
    for string in stringList:
        if isVar(string):
            return True
    return False        
            
def pri(c):
    if c in "+-":
        return 0
    if c in "*/":
        return 1
    if c in "^":
        return 2
        
def calc(op, num1, num2):
    if op == "+": return str(float(num1) + float(num2))
    if op == "-": return str(float(num1) - float(num2))
    if op == "*": return str(float(num1) * float(num2))
    if op == "/": return str(float(num1) / float(num2))
    if op == "^": return str(float(num1) ** float(num2))
        
def processExpr(expr):
    stackChr = list()
    stackNum = list()
    while len(expr) > 0:
        c = expr.pop(0)
        if isNum(c):
            #print(c+" is a number")
            stackNum.append(c)
        elif isOp(c):
            #print(c+" is an op")
            while True:
                if len(stackChr) > 0:
                    top = stackChr[-1]
                else:
                    top = ""
                if isOp(top):
                    if not pri(c) > pri(top):
                        try:
                            num2 = stackNum.pop()
                            op = stackChr.pop()
                            num1 = stackNum.pop()
                            stackNum.append(calc(op, num1, num2))
                        except:
                            raise IndexError("Trying to pop from an empty stack!")
                            break
                    else:
                        stackChr.append(c)
                        break
                else:
                    stackChr.append(c)
                    break
        elif c == "(":
            stackChr.append(c)
        elif c == ")":
            while len(stackChr) > 0:
                c = stackChr.pop()
                if c == "(":
                    break
                elif isOp(c):
                    num2 = stackNum.pop()
                    num1 = stackNum.pop()
                    stackNum.append(calc(c, num1, num2))
                    
    while len(stackChr) > 0:
        c = stackChr.pop()
        if c == "(":
            break
        elif isOp(c):
            num2 = stackNum.pop()
            num1 = stackNum.pop()
            stackNum.append(calc(c, num1, num2))

    return stackNum.pop()
            
    
def infix(input):
    if input != None:
        #while input.find('\r') != -1:
           #input.replace('\r','')
        lines = input.split('\r\n')
        varDict = dict()
        for line in lines:
            eqpos = line.find('=')        
            # if DUMP => print
            if line == "DUMP":
                for vars, values in varDict.items():
                    print(str(vars) + ": "+ str(values))
            # if no => plain expressions
            elif eqpos == -1:
            
                line = line.split(' ')
                processExpr(line)
            # if assignment
            else:
                # -1/+2 since there is a space before/after =
                var = line[:eqpos-1]
                if not isVar(var):
                    raise ValueError("Invalid variable! " + str(var))
                    break
                expr = line[eqpos+2:]
                expr = expr.split(' ')
                # if right hand side has vars            
                if hasVar(expr):
                    for i in range(len(expr)):
                        ele = expr[i]
                        if isVar(ele):
                            try:
                                number = varDict[ele]
                            except: 
                                raise KeyError("Couldn't find key: " + str(ele))
                                break
                            # update the variable with its value stored
                            if number[0] == '-':
                                print("Unary operation!")
                            expr[i] = number
                            #print("expr[i] has been updated to " + number)
                        else:
                            continue
                # if right hand side has no vars            
                value = processExpr(expr)
                #print("value is " + value)
                varDict[var] = value

        
import cgi, cgitb
cgitb.enable()

#print the http response header
print("Content-Type: text/html\n");

formInfo = cgi.FieldStorage()

# TEST
#expressions = "val1 = 3 + 4 * 3\nval2 = 3 / 2\nval3 = 3 + 2 ^ 3\nval4 = ( 3 + 4 ) * 3\nDUMP"
#expressions = "val1 = val2"
expressions = formInfo.getvalue("sentence")
infix(expressions)
