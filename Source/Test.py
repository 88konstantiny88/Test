'''
Created on 24 черв. 2016

@author: koss
'''
    
#   tuple example 
a = "hello";
b = 5;
c = 123.67;

hh = (a,b,c);

# def printAllStrings():
#     for index, i in enumerate(hh):
#         print(str(index) + " " + hh[index]);


def printAllStrings(value):
    if(value == 5):
        for index,i in enumerate(hh):
            print(hh[index-1]);
    else:
        print(hh);
    
    
    
printAllStrings(b);    