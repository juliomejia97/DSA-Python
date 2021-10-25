from Stack import *
def checkBrackets(expression):
    s =Stack()
    for c in expression:
        last = None
        if c in ('{','[','('):
            s.push(c)
        if c in ('}',']',')') and s.count > 0:
            last = s.pop()
        elif c in ('}',']',')') and s.count==0:
            return False
        if last:
            if last.data=='{' and c=='}':
                continue
            elif last.data=='[' and c==']':
                continue
            elif last.data=='(' and c==')':
                continue
            else:
                return False
    if s.count > 0:
        return False
    return True

sl = ( 
   "{(foo)(bar)}[hello](((this)is)a)test", 
   "{(foo)(bar)}[hello](((this)is)atest", 
   "{(foo)(bar)}[hello](((this)is)a)test))" 
) 
for s in sl: 
   m = checkBrackets(s) 
   print("{}: {}".format(s, m)) 