"""
GitHub: https://github.com/Chubasamuel/DCORdigitWorder/
"""
import re

cgreen="\33[32m";
cend="\033[m";
digitWord={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
pat=r"^-?[0-9]+\.?[0-9]*$"
def err(a):
    print("\33[91m\33[1m",a.capitalize(),"\033[m")
def succ(a):
    print("\33[32m\33[1m",a.capitalize(),"\033[m")
def talk(digt):
    d=str(digt)
    if(re.match(pat,d)):
        if("." in d):
           return talkDot(d);
        else:
           return talkNoDot(d);
    else:
        err("Oh oh! Enter appropriate digits please.")
        return ""
def talkAfterPoint(digt):
    # To talk the decimal fractions 
    # e.g .234= point two three four
    arr=[];
    d=list(str(digt));
    for x in d:
        arr.append(digitWord[int(x)])
    return " ".join(arr);
def talkDot(digt):
    # For digits with decimal fraction
    d=str(digt);
    d=d.split(".");
    return talkNoDot(d[0])+" point "+talkAfterPoint(d[1])
def talkNoDot(digt):
    #This function does not expect the value to be 
    #decimal fraction;
    #As this is rightly checked by the function talk(digt) 
    #before calling this function
    dC=int(digt)
    if(dC<0):
        dC=-1*dC
        isNegative="minus "
    else:
        isNegative=""
    d=str(dC);
    if(dC<=20 or (dC>20 and len(d)==2)):
        return isNegative+talkTwoD(d)
    elif(dC>=100 and len(d)==3):
        return isNegative+talkGTeHLTT(d)
    elif(dC>=1000 and( len(d)>3 and len(d)<=6)):
        return isNegative+talkGTeTLM(d)
    elif (dC>=1000000 and (len(d)>6 and len(d)<=9)):
        return isNegative+talkGTeMLTB(d)
def talkLTw(digt):
    #digt less than 20
    return digitWord[int(digt)]
def talkGTwLH(digt):
    #digt>20, and digt<100  
    d=str(digt)
    if(int(d[1:2])==0):
        retB=""
    else:
        retB=digitWord[int(d[1:2])]
    return digitWord[int(d[0:1]+"0")]+" "+retB
def talkTwoD(digt):
    #Combines the action of functions talkLTw and talkGTwLH
    dC=int(digt);
    d=str(digt);
    if(dC<=20):
        return talkLTw(digt)
    elif(dC>20 and len(d)==2):
        return talkGTwLH(digt)
    else:
        pass
def talkGTeHLTT(digt):
    #digt>=100, but <1000
    d=str(digt)
    if(int(d[1:3])==0):
        retW=""
    elif(int(d[1:3])>0 and int(d[1:3])<20):
        retW="and "+talkLTw(d[1:3])
    elif(int(d[1:3])>=20 and int(d[1:3])<100):
        retW="and "+talkGTwLH(d[1:3])
    else:
        pass
    return digitWord[int(d[0:1])]+" hundred "+retW
def talkGTeTLM(digt):
    #digt>=1000,and less than 1,000,000
    d=str(digt)
    sp=str(int(d[0:len(d)-3]))
    sp2=str(int(d[len(d)-3:len(d)]))
    comma=""
    if(len(sp2)<len(d[len(d)-3:len(d)]) and int(sp2)>0):
        #To add 'and' if in format e.g 12003 or 12098 or 123045
        And=" and"
        comma=""
    else:
        And=""
        if(int(sp2)<=0):
            comma=""
        else:
            comma=","
    if(int(sp)<=20 or (int(sp)>20 and len(str(int(sp)))==2)):
        retW1=talkTwoD(sp)
    elif(int(sp)>=100 and len(str(int(sp)))==3):
        retW1=talkGTeHLTT(sp)
    else:
        pass
    if(int(sp2)==0):
        retW2=""
    elif(int(sp2)<=20 or (int(sp2)>20 and len(str(int(sp2)))==2)):
        retW2=talkTwoD(sp2)
    elif(int(sp2)>=100 and len(str(int(sp2)))==3):
        retW2=talkGTeHLTT(sp2)
    else:
        pass
    return retW1+" thousand"+comma+And+" "+retW2
def talkGTeMLTB(digt):
    # digt>=1,000,000, and less than 1,000,000,000
    d=str(int(digt))
    if(int(d[len(d)-5:len(d)-4])==0):
        And="and "
    else:
        And=""
    return talk(d[0:len(d)-6])+" million "+And+talk(d[len(d)-6:len(d)])
class digitWorder:
    """.
=========================================================           
               DCORdigitWorder

#GitHub: https://github.com/Chubasamuel/DCORdigitWorder/

A python script that converts digits to words

> Input value can be negative or positive, 
> and can be whole number or decimal fraction.
> Input can be passed as string or number

## Usage

from DCORdigitWorder import digitWorder as dw
print(dw.word(-123456))
print(dw.word(234.55))

#### OR

from DCORdigitWorder import digitWorder as dw
print(dw.word("12345"))
print(dw.word("234.55"))

=========================================================
"""
    def __init__(self):
        pass
    def word(digit):
        return talk(str(digit))
