from datetime import datetime

name= input("Enter your name:")
#LISTS of items
lists='''
Rice   Rs 50/kg
sugar  Rs 40/kg
Salt   Rs 28/kg
Oil    Rs 120/liter
Paneer Rs 500/kg
Maggi  Rs 50/each
Boost  Rs 340/each
Ghee   Rs 60/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
list=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':50,
'sugar':40,
'Salt':28,
'Oil':120,
'Paneer':500,
'Maggi':50,
'Boost':340,
'Ghee':60}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            list.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","vijay supermarket",25*"=")
            print(28*" ","Tandur")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*"",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',*' ',list[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",30*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalmount:','Rs',finalamount)
            print(75*"-")
            print(25*" ","Thanks for visiting")
            print(75*"-")





