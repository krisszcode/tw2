def andyouPrintItOut(place):
    print("  1 2 3 4 5 6 7 8 9")
    print(" "+pgTop)
    print("a"+str(placeList[0]))
    print("b"+str(placeList[1]))
    print("c"+str(placeList[2]))
    print(" "+pgBwLine)
    print("d"+str(placeList[3]))
    print("e"+str(placeList[4]))
    print("f"+str(placeList[5]))
    print(" "+pgBwLine)
    print("g"+str(placeList[6]))
    print("h"+str(placeList[7]))
    print("i"+str(placeList[8]))
    print(" "+pgBot)
def whereList():
    #whereList=[[0,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    whereList=[[0,3,0,0,0,0,0,0,0],[0,0,0,1,9,5,0,0,0],[0,0,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,0],[4,0,0,8,0,0,0,0,1],[0,0,0,0,2,0,0,0,0],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,0,0,0,7,0]]
    #whereList=[[0,0,1,5,6,4,6,7,8],[3,2,2,1,9,5,5,3,2],[1,3,8,6,3,3,3,6,3],[8,3,3,3,6,3,3,3,3],[4,4,5,8,6,7,8,6,1],[5,4,3,1,2,6,5,4,3],[6,6,5,3,4,5,2,8,7],[3,2,5,4,1,9,7,4,5],[4,2,3,1,4,5,6,7,6]]
    return whereList

def def_list():
    whereList=[[0,3,0,0,0,0,0,0,0],[0,0,0,1,9,5,0,0,0],[0,0,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,0],[4,0,0,8,0,0,0,0,1],[0,0,0,0,2,0,0,0,0],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,0,0,0,7,0]]
    return whereList

def place(whereList):
    placeList=["","","","","","","","",""]
    ritenou=""
    for i in range(len(whereList)): 
        ritenou=""
        for j in range(len(whereList[i])):
            if whereList[i][j]!="0":
                ritenou+=str(whereList[i][j])
            else:
                ritenou+="-"
        placeList[i]+=("║"+ritenou[0]+" "+ritenou[1]+" "+ritenou[2]+"║"+ritenou[3]+" "+ritenou[4]+" "+ritenou[5]+"║"+ritenou[6]+" "+ritenou[7]+" "+ritenou[8]+"║")   

    return placeList

def replacetest(alaplista,lista):
    while True:
        repl=input("give me a row and a col(like a1): ")
        numb=int(input("What's the number? "))
        a=0
        b=0
                    
        if repl[0]=="a":
            a = 0
        elif repl[0]=="b":
            a = 1
        elif repl[0]=="c":
            a = 2
        elif repl[0]=="d":
            a = 3
        elif repl[0]=="e":    
            a = 4
        elif repl[0]=="f":
            a = 5
        elif repl[0]=="g":
            a = 6
        elif repl[0]=="h":
            a = 7
        elif repl[0]=="i":
            a = 8
                    

        if repl[1]=="1":
            b = 0
        elif repl[1]=="2":
            b = 1
        elif repl[1]=="3":
            b = 2
        elif repl[1]=="4":
            b = 3
        elif repl[1]=="5":
            b = 4
        elif repl[1]=="6":
            b = 5
        elif repl[1]=="7":
            b = 6
        elif repl[1]=="8":
            b = 7
        elif repl[1]=="9":
            b = 8

        test=lista[a][b]
        lista[a][b]=numb
        y=ellenorzes(alaplista,lista)
        if y:
            return lista
        else:
            print("Wrong input!")
            lista[a][b]=test
            continue

def numZeros(l):
    numOzeros=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j]==0:
                numOzeros+=1
    if numOzeros==0:
        return True
    else:
        return False
    
def check(lista):
    whereList=[[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    if lista==whereList:
        print("We have a winner!!!")
        return True
    else:
        return False

def copy(lista):
    copyka=lista
    return copyka
    

#####TESZT!

def elementcalc0(alaplista):
    checklist=[]
    for i in range(len(alaplista)):
        row=alaplista[i]
        for column,number in enumerate(row):
            if number!=0:
                checklist.append([i,column,number])
    return checklist

def elementcalc(wherecopy):
    checklist=[]
    for i in range(len(wherecopy)):
        row=wherecopy[i]
        for column,number in enumerate(row):
            checklist.append([i,column,number])
    return checklist

def intersection(lst1, lst2): 
      
    return [item for item in lst1 if item in lst2]

def isoverlap(eredeti,x):
    if eredeti==x:
        return True
    else:
        return False

def ellenorzes(alaplista,lista):
    eredeti=elementcalc0(alaplista)
    uj=elementcalc(lista)
    x=intersection(eredeti,uj)
    y=isoverlap(eredeti,x)
    return y




pgTop="╔"+("═"*5+"╦")*2+"═"*5+"╗"
pgBwLine="╠"+("═"*5+"╬")*2+"═"*5+"╣"
pgBot="╚"+("═"*5+"╩")*2+"═"*5+"╝"


alaplista=def_list()
lista=whereList()
placeList=place(lista)
andyouPrintItOut(placeList)

ch=True
while ch:
    tmp=copy(lista)
    x=replacetest(alaplista,lista)
    placeList=place(lista)
    for i in range(20):
        print()
    andyouPrintItOut(placeList)
    if numZeros(lista):
        ans = input("Can i check your sudoku? (y/n)")
        if ans =="y":
            if check(lista):
                ch=False
            else:
                print("You'r solution is not correct, try again")
                ch=True
        if ans == "n":
            ch==True        
