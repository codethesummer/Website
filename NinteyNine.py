import numpy as np
from statistics import median
baseStrs=input("Enter Line:").split(",")
i=0
e=0
while e<5:
    try:
        inStr=input("Enter Line:").split(",")
        global pt
        pt=int(inStr[0])
        p1HandStrs=baseStrs[:5]
        p2HandStrs=baseStrs[5:]
        pt=int(inStr[0])
        def getValueFromStr(s):
            if s.isdigit():
                return int(s)
            return {
                'J': 11,
                'Q': 12,
                'K': 13,
                'A': 14,
                'T': 10,
            }[s]

        p1Hand=[]
        p2Hand=[]
        vals=[]
        for s in inStr[1:]:
            vals.append(getValueFromStr(s))
        for s in p1HandStrs:
            p1Hand.append(getValueFromStr(s))
        for s in p2HandStrs:
            p2Hand.append(getValueFromStr(s))
        def addOne():
            global pt
            pt+=1
            if pt==34 or pt==56 or pt==78:
                pt+=5
        def addToPT(v):
            global pt
            if v==9:
                return
            if v==10:
                pt-=10
                return
            if v==7 and pt>92:
                addOne()
                return
            for i in range(v):
                addOne()

        for i in range(100):
            if i%2==0:
                addToPT(int(median(p1Hand)))
                p1Hand.remove(int(median(p1Hand)))
                if len(vals)>0:
                    p1Hand.append(vals[0])
                    vals=vals[1:]
                if pt>99:
                    print("%s, Player #2"%pt)
                    break
            if i%2==1:
                addToPT(int(median(p2Hand)))
                p2Hand.remove(int(median(p2Hand)))
                if len(vals)>0:
                    p2Hand.append(vals[0])
                    vals=vals[1:]
                if pt>99:
                    print("%s, Player #1"%pt)
                    break
    except:
        print("Input flawed, reenter line")
        e-=1
    e+=1
            
            
        
    