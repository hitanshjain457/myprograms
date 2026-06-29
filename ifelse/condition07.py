#Write a program to count total number of notes in given amount.
x=195
if(x>=500):
    a=x//500
    x=x%500
    print("Total number of 500 notes:",a)
if(x>=200):
    b=x//200
    x=x%200
    print("Total number of 200 notes:",b)
if(x>=100):
    c=x//100
    x=x%100
    print("Total number of 100 notes:",c)
if(x>=50):
    d=x//50
    x=x%50
    print("Total number of 50 notes:",d)
if(x>=20):
    e=x//20
    x=x%20
    print("Total number of 20 notes:",e)
if(x>=10):
    f=x//10
    x=x%10
    print("Total number of 10 notes:",f)