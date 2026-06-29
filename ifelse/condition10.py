#Write a program to calculate profit or loss.
cp=1000
sp=1200 
if(sp>cp):
    print("The transaction is profitable")
    profit=sp-cp
    print("The profit is:",profit)
elif(cp>sp):    
    print("The transaction is not profitable")
    loss=cp-sp
    print("The loss is:",loss)