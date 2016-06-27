'''
Created on 24 черв. 2016

@author: koss
'''
import string;
import socket;

#   tuple example 
a = "hello";
b = 5;
c = 123.67;

hh = (a,b,c);

# def printAllStrings():
#     for index, i in enumerate(hh):
#         print(str(index) + " " + hh[index]);



def getAddr(value):
    addr = (socket.gethostbyname(value));
    return addr;



def printAllStrings(value):
    if(value == 5):
        for index,i in enumerate(hh):
            print(hh[index-1]);
    else:
        return print(value);
    

def letterCount(text, letters = string.ascii_letters):
    letters = frozenset(letters);
    count = 0;
    for char in text:
        if char in letters:
                count += 1 ;
    return count;

    
    
printAllStrings(b);
print(letterCount("fuck"));
print(getAddr("google.ua"));
print(getAddr("google.com"));
print(getAddr("4pda.ru"));    