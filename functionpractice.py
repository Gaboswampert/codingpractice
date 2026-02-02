def funcpractice(var):
    
    if var == "remove":
        print(shoplist)
        destroy=input("What do you want to remove?: ")
        if destroy in shoplist:
            shoplist.remove(destroy)
        else:
            print("Invalid Item.")
            print("")
    elif var == "r":
        print(shoplist)
        destroyr=input("What do you want to remove?: ")
        if destroyr in shoplist:
            shoplist.remove(destroyr)
        else:
            print("Invalid Item.")
            print("")
    elif var == str(var):
        shoplist.append(var)
        
shoplist=[]
bigbool=True
while bigbool == True:
    print("Items Currently in Shopping List:")
    print("")
    print(shoplist)
    print("")
    print("Input \"end\" when your list is finished, and \"remove\" (or r) when you want to remove an item!")
    shopadd=input("What do you want to add to the shopping list?: ")
    funcpractice(shopadd)
    if "end" in shoplist:
        againbool=True
        shoplist.remove("end")
        print("Here's your final shopping list!:")
        print("")
        print(shoplist)
        print("")
        shoplist.clear()
        while againbool == True:
            goagain=input("Want to make a new list? (y/n): ")
            if goagain == "y":
                againbool=False
                continue
            elif goagain == "n":
                bigbool=False
                break
            else:
                continue
    continue
    


