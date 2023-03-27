#write a program that allows a customer to submit his or her grocery order 
#Also ask if they do,continue taking order until they say no 
#Show item pricing at first, show the menu at the console and lastly a bill of total cost for the customers to pay


import datetime

e = datetime.datetime.now()

fruits={
    "APPLE":220.00,
    "BANANA":100.00,
    "MANGO":250.00
}

vegetable={
    "BROCCOLI":50.00,
    "CARROT":60.00,
    "POTATO":100.00,
    "TOMATO":40.00
}

Grain={
    "NOODLES":100.00,
    "EGG":300.00,
    "PASTA":90.00
}

#head print*************
print()
print("*************GROCERY ITEMS************")
print()

print(" FRUITS")
for x in fruits:
    print("        ",x,":",fruits[x])
print(" VGETABLES")
for x in vegetable:
    print("        ",x,":",vegetable[x])
print(" GRAINS")
for x in Grain:
    print("        ",x,":",Grain[x])

#choice of customer*****************
def choice(items):
    switch={
        "apple":120,
        "banana":100,
        "mango":150,
        "broccoli":120,
        "carrot":100,
        "potato":150,
        "tomato":100,
        "noodles":100,
        "egg":300,
        "pasta":150
      }
    return switch.get(items,"Outstock")
print()
print("****************Please, Fill the form*****************")
print()
#user enter*****************************
name=input("Enter your name: ")
address=input("enter your address: ")
print()
print("******************* your order************************")
print()
Citems=[]
Cprice=[]
ch="y"
#items enter*****************************
while(ch=="y" or ch=="Y"):
    itm=input("select the items:")
    itm=itm.strip()#*********************
    itm=itm.lower()
    if (choice(itm) !=  "Outstock" ):
        Citems.append(itm)
        Cprice.append(choice(itm))
    else:
       print("<--sorry, Out of the stock-->")
    ch=input("do you wanna continue taking order(y/n)?..")



#output**********************
nwidth=23
awidth=20
print()
print("             NEPAL COMAPANY LTD")
print("            Phn:+977 9800000000")
print("             ITAHARI,SUNSARI")
print()
print("*********************TAX INVOICE********************")
print(f"User:{name:<{nwidth}} Date: {e.day}/{e.month}/{e.year}")
print(f"Address:{address:<{awidth}} Time: {e.hour}:{e.minute}:{e.second}")
print("****************************************************")
print("SN\t\tProduct\t\t\t\t\tprice")
print("****************************************************")
def display():
    for i in range(0,len(Citems)):
        print(f"{i+1}\t\t{Citems[i].upper():<20}\t\t{Cprice[i]:<20}")

display()
print("****************************************************")

sum=0
for x in Cprice:
    sum+=x

print("Total: \t\t\t\t\tRs",sum)
print("****************************************************")
print("THANK YOU \t\t VISIT AGAIN!")