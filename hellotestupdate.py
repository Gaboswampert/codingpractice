#print("hello world")
#x="prueba"
#ab=69
#print(x,ab)
#si por alguna razon hago un codigo que es un bucle infinito, apreta ctrl + c
#e=4
#y=int(8)
#f=float(3.1)
#s=str(9)
#int es para int, float es para float, str no se suma, juntan las variables
#int es para enteros, float es para decimales
#str es para cosas que no se suman
#input es como el print en reversa, le da a la consola una variable
#desde la ejecucion
#yy=int(32)
#ff=float(6.8)
#print(y+yy)
#print(f+ff)
#ss=str(6)
#print(s+ss)
#print(ss*y)
#coloca en una lista los numeros, recuerda hacerlos string porque entran asi


#equations=["+","-","*","/"]
#numbers=["1","2","3","4","5","6","7","8","9","0"]
#eviletters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m","."]

#while True:
    #print("\n \t Hello! This is my test calculator, hope you enjoy it!")
    #fnumbernoint=input("Input the first number here!:")
    #if fnumbernoint.isnumeric() is False:
        #print("Sorry, but you can only type numbers here.")
        #continue
    #fnumber=int(fnumbernoint)
    #thing=input("Do you want to add+, subtract-, multiply* or divide/?:")
    #if thing in equations:
        #snumbernoint=input("Input the second number here!:")
        #if snumbernoint.isnumeric() is False:
           #print("Sorry, but you can only type numbers here.")
           #continue
        #else:
            #snumber=int(snumbernoint)
            #if thing == "+":
               #print("Here's your result!:",fnumber+snumber)
            #elif thing == "-":
                 #print("Here's your result!:",fnumber-snumber)
            #elif thing == "*":
                 #print("Here's your result!:",fnumber*snumber)
            #elif thing == "/":
                 #print("Here's your result!:",fnumber//snumber)          
    #else:
        #print("You didn't input a valid equation.")
    #again=input("Want to calculate again? (y/n)")
    #if again == "y":
        #continue
    #else:
        #print("Ok then! Byeee!")
        #break

equations=("+","-","*","/","//","%")
numbers=("1","2","3","4","5","6","7","8","9","0")

def intmachine():
    for i in range(len(calclist)):
        if calclist[i].isnumeric():
            calclist[i]=int(calclist[i])
#check for bugs here, seems as if this can be bypassable w only putting a number
def equatiolist():
    if '+' in calclist:
        pass
    elif '-' in calclist:
        pass
    elif '*' in calclist:
        pass
    elif '/' in calclist:
        pass
    else:
        silly=("not a valid response")

while True:
    secondbool=False
    thirdbool=False
    fourthbool=False
    fifthbool=False
    sixthbool=False
    seventhbool=False
    eighthbool=False
    ninthbool=False
    tenthbool=False
    calcstring=input("\nHello, please input your problem here, or input Help for more information: ")
    if calcstring == "Help":
        print(" + = addition. \n - = substraction. \n * = multiplication. \n / = division. \n This calculator only operates with the operations mentioned before.  \n This calculator doesn't operate with decimals (floats), or PEMDAS in mind. \n Operation limit is 10 operations.") 
        continue
    
    calclist=[]
    calcstart=int(1)

    silly=(None)
    for x in calcstring:
        calclist.append(x)
    calclist.append(" ")
    calclistlen=(len(calclist))
    if '1' in calcstring[0]:
        equatiolist()
    elif '2' in calcstring[0]:
        equatiolist()
    elif '3' in calcstring[0]:
        equatiolist()
    elif '4' in calcstring[0]:
        equatiolist()
    elif '5' in calcstring[0]:
        equatiolist()
    elif '6' in calcstring[0]:
        equatiolist()
    elif '7' in calcstring[0]:
        equatiolist()
    elif '8' in calcstring[0]:
        equatiolist()
    elif '9' in calcstring[0]:
        equatiolist()
    elif '0' in calcstring[0]:
        equatiolist()
    else:
        print("Not a Valid Response.")
        continue
    if silly == "not a valid response":
        print("Not a Valid Response")
        continue
        
    numberlist=[ ]
    equalocation=int(0)
    for u in calcstring:
        if u.isnumeric() is False:
            equalocation=calcstring.index(u)
            break
        numberlist.append(u)
    firstnumber=str("")
    for r in range(len(numberlist)):
        firstnumber=(firstnumber+numberlist[r])
    firstnumber.strip()
    firstnumblen=len(firstnumber)
    firstnumber=int(firstnumber)
    fullnumber=(calcstring[equalocation:])
    equation1=(fullnumber[0])
    if len(fullnumber) > firstnumblen:
        secondbool=True
        equalocation2=int(0)
        fullnumber=(fullnumber[1:])
        secondlist=[ ]
        for w in fullnumber:
            if w.isnumeric() is False:
                equalocation2=fullnumber.index(w)
                break
            secondlist.append(w)
        secondnumber=str("")
        for q in range(len(secondlist)):
            secondnumber=(secondnumber+secondlist[q])
        secondnumber.strip()
        if secondnumber == "":
            print("Not a Valid Response")
            continue
        secondnumblen=(len(secondnumber))
        fullnumber=(fullnumber[equalocation2:])
        secondnumber=int(secondnumber)
        if len(fullnumber) > secondnumblen:
            #reminder that you should remove the next digit from fullnumber after doing the operation
            thirdbool=True
            equalocation3=int(0)
            equation2=(fullnumber[0])
            fullnumber=(fullnumber[1:])
            thirdlist=[ ]
            for l in fullnumber:
                if l.isnumeric() is False:
                    equalocation3=fullnumber.index(l)
                    break
                thirdlist.append(l)
            thirdnumber=str("")
            for k in range(len(thirdlist)):
                thirdnumber=(thirdnumber+thirdlist[k])
            thirdnumber.strip()
            if thirdnumber == "":
                print("Not a Valid Response")
                continue
            thirdnumblen=(len(thirdnumber))
            fullnumber=(fullnumber[equalocation3:])
            thirdnumber=int(thirdnumber)
            if len(fullnumber) > thirdnumblen:
                fourthbool=True
                equalocation4=int(0)
                equation3=(fullnumber[0])
                fullnumber=(fullnumber[1:])
                fourthlist=[ ]
                for g in fullnumber:
                    if g.isnumeric() is False:
                        equalocation4=fullnumber.index(g)
                        break
                    fourthlist.append(g)
                fourthnumber=str("")
                for d in range(len(fourthlist)):
                    fourthnumber=(fourthnumber+fourthlist[d])
                fourthnumber.strip()
                if fourthnumber == "":
                    print("Not a Valid Response")
                    continue
                fourthnumblen=(len(fourthnumber))
                fullnumber=(fullnumber[equalocation4:])
                fourthnumber=int(fourthnumber)
                if len(fullnumber) > fourthnumblen:
                    fifthbool=True
                    equalocation5=int(0)
                    equation4=(fullnumber[0])
                    fullnumber=(fullnumber[1:])
                    fifthlist=[ ]
                    for x in fullnumber:
                        if x.isnumeric() is False:
                            equalocation5=fullnumber.index(x)
                            break
                        fifthlist.append(x)
                    fifthnumber=str("")
                    for y in range(len(fifthlist)):
                        fifthnumber=(fifthnumber+fifthlist[y])
                    fifthnumber.strip()
                    if fifthnumber == "":
                        print("Not a Valid Response")
                        continue
                    fifthnumblen=(len(fifthnumber))
                    fullnumber=(fullnumber[equalocation5:])
                    fifthnumber=int(fifthnumber)
                    if len(fullnumber) > fifthnumblen:
                        sixthbool=True
                        equalocation6=int(0)
                        equation5=(fullnumber[0])
                        fullnumber=(fullnumber[1:])
                        sixthlist=[ ]
                        for x in fullnumber:
                            if x.isnumeric() is False:
                                equalocation6=fullnumber.index(x)
                                break
                            sixthlist.append(x)
                        sixthnumber=str("")
                        for y in range(len(sixthlist)):
                            sixthnumber=(sixthnumber+sixthlist[y])
                        sixthnumber.strip()
                        if sixthnumber == "":
                            print("Not a Valid Response")
                            continue
                        sixthnumblen=(len(sixthnumber))
                        fullnumber=(fullnumber[equalocation6:])
                        sixthnumber=int(sixthnumber)
                        if len(fullnumber) > sixthnumblen:
                            seventhbool=True
                            equalocation7=int(0)
                            equation6=(fullnumber[0])
                            fullnumber=(fullnumber[1:])
                            seventhlist=[ ]
                            for x in fullnumber:
                                if x.isnumeric() is False:
                                    equalocation7=fullnumber.index(x)
                                    break
                                seventhlist.append(x)
                            seventhnumber=str("")
                            for y in range(len(seventhlist)):
                                seventhnumber=(seventhnumber+seventhlist[y])
                            seventhnumber.strip()
                            if seventhnumber == "":
                                print("Not a Valid Response")
                                continue
                            seventhnumblen=(len(seventhnumber))
                            fullnumber=(fullnumber[equalocation7:])
                            seventhnumber=int(seventhnumber)
                            if len(fullnumber) > seventhnumblen:
                                eighthbool=True
                                equalocation8=int(0)
                                equation7=(fullnumber[0])
                                fullnumber=(fullnumber[1:])
                                eighthlist=[ ]
                                for x in fullnumber:
                                    if x.isnumeric() is False:
                                        equalocation8=fullnumber.index(x)
                                        break
                                    eighthlist.append(x)
                                eighthnumber=str("")
                                for y in range(len(eighthlist)):
                                    eighthnumber=(eighthnumber+eighthlist[y])
                                eighthnumber.strip()
                                if eighthnumber == "":
                                    print("Not a Valid Response")
                                    continue
                                eighthnumblen=(len(eighthnumber))
                                fullnumber=(fullnumber[equalocation8:])
                                eighthnumber=int(eighthnumber)
                                if len(fullnumber) > eighthnumblen:
                                    ninthbool=True
                                    equalocation9=int(0)
                                    equation8=(fullnumber[0])
                                    fullnumber=(fullnumber[1:])
                                    ninthlist=[ ]
                                    for x in fullnumber:
                                        if x.isnumeric() is False:
                                            equalocation9=fullnumber.index(x)
                                            break
                                        ninthlist.append(x)
                                    ninthnumber=str("")
                                    for y in range(len(ninthlist)):
                                        ninthnumber=(ninthnumber+ninthlist[y])
                                    ninthnumber.strip()
                                    if ninthnumber == "":
                                        print("Not a Valid Response")
                                        continue
                                    ninthnumblen=(len(ninthnumber))
                                    fullnumber=(fullnumber[equalocation9:])
                                    ninthnumber=int(ninthnumber)
                                    if len(fullnumber) > ninthnumblen:
                                        tenthbool=True
                                        equalocation10=int(0)
                                        equation9=(fullnumber[0])
                                        fullnumber=(fullnumber[1:])
                                        tenthlist=[ ]
                                        for x in fullnumber:
                                            if x.isnumeric() is False:
                                                equalocation10=fullnumber.index(x)
                                                break
                                            tenthlist.append(x)
                                        tenthnumber=str("")
                                        for y in range(len(tenthlist)):
                                            tenthnumber=(tenthnumber+tenthlist[y])
                                        tenthnumber.strip()
                                        if tenthnumber == "":
                                            print("Not a Valid Response")
                                            continue
                                        tenthnumblen=(len(tenthnumber))
                                        fullnumber=(fullnumber[equalocation10:])
                                        tenthnumber=int(tenthnumber)
                                        if len(fullnumber) > tenthnumblen:
                                            print("Operation limit is 10 operations.")
                                            continue
    
    #reminder to add eleventh if lenfullnumber > xnumblen and makes it so it invalidates the equation

    result=(firstnumber)
    if secondbool == True:
        if equation1 == "+":
            result=(firstnumber+secondnumber)
        elif equation1 == "-":
            result=(firstnumber-secondnumber)
        elif equation1 == "*":
            result=(firstnumber*secondnumber)
        elif equation1 == "/":
             result=(firstnumber//secondnumber)
        if thirdbool == True:
            if equation2 == "+":
                    result=(result+thirdnumber)
            elif equation2 == "-":
                    result=(result-thirdnumber)
            elif equation2 == "*":
                    result=(result*thirdnumber)
            elif equation2 == "/":
                    result=(result//thirdnumber)
            if fourthbool == True:
                if equation3 == "+":
                    result=(result+fourthnumber)
                elif equation3 == "-":
                    result=(result-fourthnumber)
                elif equation3 == "*":
                    result=(result*fourthnumber)
                elif equation3 == "/":
                    result=(result//fourthnumber)
                if fifthbool == True:
                    if equation4 == "+":
                        result=(result+fifthnumber)
                    elif equation4 == "-":
                        result=(result-fifthnumber)
                    elif equation4 == "*":
                        result=(result*fifthnumber)
                    elif equation4 == "/":
                        result=(result//fifthnumber)
                    if sixthbool == True:
                        if equation5 == "+":
                            result=(result+sixthnumber)
                        elif equation5 == "-":
                            result=(result-sixthnumber)
                        elif equation5 == "*":
                            result=(result*sixthnumber)
                        elif equation5 == "/":
                            result=(result//sixthnumber)
                        if seventhbool == True:
                            if equation6 == "+":
                                result=(result+seventhnumber)
                            elif equation6 == "-":
                                result=(result-seventhnumber)
                            elif equation6 == "*":
                                result=(result*seventhnumber)
                            elif equation6 == "/":
                                result=(result//seventhnumber)
                            if eighthbool == True:
                                if equation7 == "+":
                                    result=(result+eighthnumber)
                                elif equation7 == "-":
                                    result=(result-eighthnumber)
                                elif equation7 == "*":
                                    result=(result*eighthnumber)
                                elif equation7 == "/":
                                    result=(result//eighthnumber)
                                if ninthbool == True:
                                    if equation8 == "+":
                                        result=(result+ninthnumber)
                                    elif equation8 == "-":
                                        result=(result-ninthnumber)
                                    elif equation8 == "*":
                                        result=(result*ninthnumber)
                                    elif equation8 == "/":
                                        result=(result//ninthnumber)
                                    if tenthbool == True:
                                        if equation9 == "+":
                                            result=(result+tenthnumber)
                                        elif equation9 == "-":
                                            result=(result-tenthnumber)
                                        elif equation9 == "*":
                                            result=(result*tenthnumber)
                                        elif equation9 == "/":
                                            result=(result//tenthnumber)

    print("Here's your result!:")
    print(result)
    continue
    
