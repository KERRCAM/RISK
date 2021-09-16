import time
import math
import random

#fix player out validation thingys

layout = "{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4} "
column_check = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
row_check = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27"]


##
land=10
#~
shippinglanes=10
#_
ocean=10
# H
p1army=10
# Z
p2army=10
# K
p3army=10
# X
p4army=10

p1alive = True
p2alive = True
p3alive = True
p4alive = True

def coordinates():
    print("latitudes")
    print("A=1")
    print("B=2")
    print("C=3")
    print("D=4")
    print("E=5")
    print("F=6")
    print("G=7")
    print("b=8")
    print("I=9")
    print("J=10")
    print("c=11")
    print("L=12")
    print("M=13")
    print("N=14")
    print("O=15")
    print("P=16")
    print("Q=17")
    print("R=18")
    print("S=19")
    print("T=20")
    print("U=21")
    print("V=22")
    print("W=23")
    print("d=24")
    print("Y=25")
    print("e=26")
    print("a=27")

    print("longitudes")
    print("a=0")
    print("b=1")
    print("c=2")
    print("d=3")
    print("e=4")
    print("f=5")
    print("g=6")
    print("h=7")
    print("i=8")
    print("j=9")
    print("k=10")
    print("l=11")
    print("m=12")
    print("n=13")
    print("o=14")
    print("p=15")
    print("q=16")
    print("r=17")
    print("s=18")
    print("t=19")
    print("u=20")
    print("v=21")
    print("w=22")
    print("x=23")
    print("y=24")
    print("z=25")
    print("A=26")





def player1():
    global worldmap
    global p1army
    global p2army
    global p3arm
    global p4army
    global p1alive    
    if p1alive == False:
        print("player 1 is out")
        (player2)
    found1 = False
    for i in range(rows):
        for j in range(columns):
            if worldmap[i][j] == "H":
                print("player 1 armies:",(p1army))
                found1=True
    if found1 == False:
        print("test")
        p1alive = False        
    coordinates()
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    check = False

    turn = False
    while turn == False:     
        p1_column  = input("p1-what longtitude is the target: ")
        if p1_column == "":
            print("invalid input")
        elif p1_column not in column_check:
            print("invalid input")
        else:
            p1_column = int(p1_column)
            p1_row = input("p1-what latitude is the target: ")
            if p1_row == (""):
                print("invalid input")
            elif p1_row not in row_check:
                print("invalid input")
            else:
                p1_row = int(p1_row)
                turn = True
            #NEED TO REPLEACE VALIDATION IN OTHER FUNCTIONS WITH THIS
    while check==False:
        checkla1=p1_column-1
        checklo1=p1_row-1
        if worldmap[checkla1][checklo1]=="H":
            check=True
            turn=True
            break
        checkla2=p1_column+1
        checklo2=p1_row+1
        if worldmap[checkla2][checklo2]=="H":
            check=True
            turn=True
            break
        checkla3=p1_column-1
        checklo3=p1_row+1
        if worldmap[checkla3][checklo3]=="H":
            check=True
            turn=True
            break
        checkla4=p1_column+1
        checklo4=p1_row-1
        if worldmap[checkla4][checklo4]=="H":
            check=True
            turn=True
            break
        checkla5=p1_column
        checklo5=p1_row-1
        if worldmap[checkla5][checklo5]=="H":
            check=True
            turn=True
            break
        checkla6=p1_column-1
        checklo6=p1_row
        if worldmap[checkla6][checklo6]=="H":
            check=True
            turn=True
            break
        checkla7=p1_column+1
        checklo7=p1_row
        if worldmap[checkla7][checklo7]=="H":
            check=True
            turn=True
            break
        checkla8=p1_column
        checklo8=p1_row+1
        if worldmap[checkla8][checklo8]=="H":
            check=True
            turn=True
            break
        else:
            print("p1-that targit is out of range")
            print("p1-available armys are now:")
            print(p1army)
            time.sleep(4)
            player2()
        turn=False
        if  worldmap [p1_column][p1_row]== "-":
            print ("p1-that is the ocean")
        if  worldmap [p1_column][p1_row]== "X":
            print ("p1-that is your own land")
        if worldmap [p1_column][p1_row]== "Z" or worldmap [p1_column][p1_row]== "K" or worldmap [p1_column][p1_row]== "X" or worldmap [p1_column][p1_row]== "#":
                if worldmap [p1_column][p1_row]== "Z":
                    p1rn=random.randint(1,p1army)
                    p2rn=random.randint(1,p2army)
                    invade=(p1rn-p2rn)
                    if invade > 0:
                        worldmap [p1_column][p1_row]= "H"                
                if worldmap [p1_column][p1_row]== "K":
                    p1rn=random.randint(1,p1army)
                    p3rn=random.randint(1,p3army)
                    invade=(p1rn-p3rn)
                    if invade > 0:
                        worldmap [p1_column][p1_row]= "H"
                if worldmap [p1_column][p1_row]== "X":
                    p1rn=random.randint(1,p1army)
                    p4rn=random.randint(1,p4army)
                    invade=(p1rn-p4rn)
                    if invade > 0:
                        worldmap [p1_column][p1_row]= "H"
                if worldmap [p1_column][p1_row]== "#":
                    p1army=p1army-1
                    worldmap [p1_column][p1_row]= "H"
                if worldmap [p1_column][p1_row]== "~":
                    p1army=p1army-1
                    worldmap [p1_column][p1_row]= "H"  
                for i in worldmap:
                    for j in i:
                        if j=="H":
                            p1army=p1army+1
                print("p1-available armys are now:")
                print(p1army)
        turn=True
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    player2()
    


def player2():
    global worldmap
    global p1army
    global p2army
    global p3army
    global p4army
    global p2alive
    if p2alive == False:
        print("player 2 is out")
        (player3)
    found2 = False
    for i in range(rows):
        for j in range(columns):
            if worldmap[i][j] == "Z":
                print("player 2 armies:",(p1army))
                found2=True
    if found2 == False:
        p2alive = False
    coordinates()
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    check = False



    
    turn = False
    while turn == False:
        p2_column  = int(input("p2-what longtitude is the targit: "))
        if p2_column == (""):
            print("invalid input")
        if p2_column != ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("8") or ("9") or ("9") or ("10") or ("11") or ("12") or ("13") or ("14") or ("15") or ("16") or ("17") or ("18") or  ("19") or ("20") or ("21") or ("22") or ("23") or ("24") or ("25") or ("26"):
            print("invalid input")
        p2_row = int(input("p2-what latitude is the targit: "))
        if p2_row == (""):
            print("invalid input")
        if p2_row != ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("8") or ("9") or ("9") or ("10") or ("11") or ("12") or ("13") or ("14") or ("15") or ("16") or ("17") or ("18") or  ("19") or ("20") or ("21") or ("22") or ("23") or ("24") or ("25") or ("26") or ("27"):
            print("invalid input")



        
    while check==False:
        checkla1=p2_column-1
        checklo1=p2_row-1
        if worldmap[checkla1][checklo1]=="Z":
            check=True
            turn=True
            break
        checkla2=p2_column+1
        checklo2=p2_row+1
        if worldmap[checkla2][checklo2]=="Z":
            check=True
            turn=True
            break
        checkla3=p2_column-1
        checklo3=p2_row+1
        if worldmap[checkla3][checklo3]=="Z":
            check=True
            turn=True
            break
        checkla4=p2_column+1
        checklo4=p2_row-1
        if worldmap[checkla4][checklo4]=="Z":
            check=True
            turn=True
            break
        checkla5=p2_column
        checklo5=p2_row-1
        if worldmap[checkla5][checklo5]=="Z":
            check=True
            turn=True
            break
        checkla6=p2_column-1
        checklo6=p2_row
        if worldmap[checkla6][checklo6]=="Z":
            check=True
            turn=True
            break
        checkla7=p2_column+1
        checklo7=p2_row
        if worldmap[checkla7][checklo7]=="Z":
            check=True
            turn=True
            break
        checkla8=p2_column
        checklo8=p2_row+1
        if worldmap[checkla8][checklo8]=="Z":
            check=True
            turn=True
            break
        else:
            print("p2-that targit is out of range")
            print("p2-available armys are now:")
            print(p2army)
            time.sleep(4)
            player3()
        turn=False
        if  worldmap [p2_column][p2_row]== "-":
            print ("p2-that is the ocean")
        if  worldmap [p2_column][p2_row]== "Z":
            print ("p2-that is your own land")
        if worldmap [p2_column][p2_row]== "H" or worldmap [p2_column][p2_row]== "K" or worldmap [p2_column][p2_row]== "X" or worldmap [p2_column][p2_row]== "#":
                if worldmap [p2_column][p2_row]== "H":
                    p2rn=random.randint(1,p2army)
                    p1rn=random.randint(1,p1army)
                    invade=(p2rn-p1rn)
                    if invade > 0:
                        worldmap [p2_column][p2_row]= "Z"                
                if worldmap [p2_column][p2_row]== "K":
                    p2rn=random.randint(1,p2army)
                    p3rn=random.randint(1,p3army)
                    invade=(p2rn-p3rn)
                    if invade > 0:
                        worldmap [p2_column][p2_row]= "Z"
                if worldmap [p2_column][p2_row]== "X":
                    p2rn=random.randint(1,p2army)
                    p4rn=random.randint(1,p4army)
                    invade=(p2rn-p4rn)
                    if invade > 0:
                        worldmap [p2_column][p2_row]= "Z"
                if worldmap [p2_column][p2_row]== "#":
                    p2army=p2army-1
                    worldmap [p2_column][p2_row]= "Z"
                if worldmap [p2_column][p2_row]== "~":
                    p2army=p2army-1
                    worldmap [p2_column][p2_row]= "Z"
                for i in worldmap:
                    for j in i:
                        if j=="Z":
                            p2army=p2army+1
                print("p2-available armys are now:")
                print(p2army)
        turn=True
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    player3()


def player3():
    global worldmap
    global p1army
    global p2army
    global p3army
    global p4army
    global p3alive
    if p3alive == False:
        print("player 3 is out")
        (player4)
    found3 = False
    for i in range(rows):
        for j in range(columns):
            if worldmap[i][j] == "K":
                print("player 3 armies:",(p1army))
                found3=True
    if found3 == False:
        p3alive = False        
    coordinates()
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    check = False




     
    turn = False
    while turn == False:
        p3_column  = int(input("p3-what longtitude is the targit: "))
        if p3_column == (""):
            print("invalid input")
        if p3_column != ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("8") or ("9") or ("9") or ("10") or ("11") or ("12") or ("13") or ("14") or ("15") or ("16") or ("17") or ("18") or  ("19") or ("20") or ("21") or ("22") or ("23") or ("24") or ("25") or ("26"):
            print("invalid input")
        p3_row = int(input("p3-what latitude is the targit: "))
        if p3_row == (""):
            print("invalid input")
        if p3_row != ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("8") or ("9") or ("9") or ("10") or ("11") or ("12") or ("13") or ("14") or ("15") or ("16") or ("17") or ("18") or  ("19") or ("20") or ("21") or ("22") or ("23") or ("24") or ("25") or ("26") or ("27"):
            print("invalid input")




            
    while check==False:
        checkla1=p3_column-1
        checklo1=p3_row-1
        if worldmap[checkla1][checklo1]=="K":
            check=True
            turn=True
            break
        checkla2=p3_column+1
        checklo2=p3_row+1
        if worldmap[checkla2][checklo2]=="K":
            check=True
            turn=True
            break
        checkla3=p3_column-1
        checklo3=p3_row+1
        if worldmap[checkla3][checklo3]=="K":
            check=True
            turn=True
            break
        checkla4=p3_column+1
        checklo4=p3_row-1
        if worldmap[checkla4][checklo4]=="K":
            check=True
            turn=True
            break
        checkla5=p3_column
        checklo5=p3_row-1
        if worldmap[checkla5][checklo5]=="K":
            check=True
            turn=True
            break
        checkla6=p3_column-1
        checklo6=p3_row
        if worldmap[checkla6][checklo6]=="K":
            check=True
            turn=True
            break
        checkla7=p3_column+1
        checklo7=p3_row
        if worldmap[checkla7][checklo7]=="K":
            check=True
            turn=True
            break
        checkla8=p3_column
        checklo8=p3_row+1
        if worldmap[checkla8][checklo8]=="K":
            check=True
            turn=True
            break
        else:
            print("that targit is out of range")
            print("p3-available armys are now:")
            print(p3army)
            time.sleep(4)
            player4()
        turn=False
        if  worldmap [p3_column][p3_row]== "-":
            print ("p3-that is the ocean")
        if  worldmap [p3_column][p3_row]== "K":
            print ("p3-that is your own land") 
        if worldmap [p3_column][p3_row]== "Z" or worldmap [p3_column][p3_row]== "H" or worldmap [p3_column][p3_row]== "X" or worldmap [p3_column][p3_row]== "#":
                if worldmap [p3_column][p3_row]== "Z":
                    p3rn=random.randint(1,p3army)
                    p2rn=random.randint(1,p2army)
                    invade=(p3rn-p2rn)
                    if invade > 0:
                        worldmap [p3_column][p3_row]= "K"                
                if worldmap [p3_column][p3_row]== "H":
                    p3rn=random.randint(1,p3army)
                    p1rn=random.randint(1,p1army)
                    invade=(p3rn-p1rn)
                    if invade > 0:
                        worldmap [p3_column][p3_row]= "K"
                if worldmap [p3_column][p3_row]== "X":
                    p3rn=random.randint(1,p3army)
                    p4rn=random.randint(1,p4army)
                    invade=(p3rn-p4rn)
                    if invade > 0:
                        worldmap [p3_column][p3_row]= "K"
                if worldmap [p3_column][p3_row]== "#":
                    p3army=p3army-1
                    worldmap [p3_column][p3_row]= "K"
                if worldmap [p3_column][p3_row]== "~":
                    p3army=p3army-1
                    worldmap [p3_column][p3_row]= "K"
                for i in worldmap:
                    for j in i:
                        if j=="K":
                            p3army=p3army+1
                print("p3-available armys are now:")
                print(p3army)
        turn=True
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    player4()


def player4():
    global worldmap
    global p1army
    global p2army
    global p3army
    global p4army
    global p4alive
    if p4alive == False:
        print("player 4 is out")
        (player1)
    found4 = False
    for i in range(rows):
        for j in range(columns):
            if worldmap[i][j] == "X":
                print("player 4 armies:",(p4army))
                found4=True
    if found4 == False:
        p4alive = False        
    coordinates()
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    check = False



    
    turn = False
    while turn == False:       
        p4_column  = int(input("p4-what longtitude is the targit: "))
        if p4_column == (""):
            print("invalid input")
        if  p4_column != ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("8") or ("9") or ("9") or ("10") or ("11") or ("12") or ("13") or ("14") or ("15") or ("16") or ("17") or ("18") or  ("19") or ("20") or ("21") or ("22") or ("23") or ("24") or ("25") or ("26"):
            print("invalid input")
        p4_row = int(input("p4-what latitude is the targit: "))
        if p4_row == (""):
            print("invalid input")
        if p4_row != ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("8") or ("9") or ("9") or ("10") or ("11") or ("12") or ("13") or ("14") or ("15") or ("16") or ("17") or ("18") or  ("19") or ("20") or ("21") or ("22") or ("23") or ("24") or ("25") or ("26") or ("27"):
            print("invalid input")




            
    while check==False:
        checkla1=p4_column-1
        checklo1=p4_row-1
        if worldmap[checkla1][checklo1]=="X":
            check=True
            turn=True
            break
        checkla2=p4_column+1
        checklo2=p4_row+1
        if worldmap[checkla2][checklo2]=="X":
            check=True
            turn=True
            break
        checkla3=p4_column-1
        checklo3=p4_row+1
        if worldmap[checkla3][checklo3]=="X":
            check=True
            turn=True
            break
        checkla4=p4_column+1
        checklo4=p4_row-1
        if worldmap[checkla4][checklo4]=="X":
            check=True
            turn=True
            break
        checkla5=p4_column
        checklo5=p4_row-1
        if worldmap[checkla5][checklo5]=="X":
            check=True
            turn=True
            break
        checkla6=p4_column-1
        checklo6=p4_row
        if worldmap[checkla6][checklo6]=="X":
            check=True
            turn=True
            break
        checkla7=p4_column+1
        checklo7=p4_row
        if worldmap[checkla7][checklo7]=="X":
            check=True
            turn=True
            break
        checkla8=p4_column
        checklo8=p4_row+1
        if worldmap[checkla8][checklo8]=="X":
            check=True
            turn=True
            break
        else:
            print("p4-that targit is out of range")
            print("p4-available armys are now:")
            print(p4army)
            time.sleep(4)
            player1()
        turn=False
        if  worldmap [p4_column][p4_row]== "-":
            print ("p4-that is the ocean")
        if  worldmap [p4_column][p4_row]== "X":
            print ("p4-that is your own land")
        if worldmap [p4_column][p4_row]== "Z" or worldmap [p4_column][p4_row]== "K" or worldmap [p4_column][p4_row]== "H" or worldmap [p4_column][p4_row]== "#":
                if worldmap [p4_column][p4_row]== "Z":
                    p4rn=random.randint(1,p4army)
                    p2rn=random.randint(1,p2army)
                    invade=(p4rn-p2rn)
                    if invade > 0:
                        worldmap [p4_column][p4_row]= "X"                
                if worldmap [p4_column][p4_row]== "K":
                    p4rn=random.randint(1,p4army)
                    p3rn=random.randint(1,p3army)
                    invade=(p1rn-p3rn)
                    if invade > 0:
                        worldmap [p4_column][p4_row]= "X"
                if worldmap [p4_column][p4_row]== "H":
                    p4rn=random.randint(1,p4army)
                    p1rn=random.randint(1,p1army)
                    invade=(p4rn-p1rn)
                    if invade > 0:
                        worldmap [p4_column][p4_row]= "X"
                if worldmap [p4_column][p4_row]== "#":
                    p4army=p4army-1
                    worldmap [p4_column][p4_row]= "X"
                if worldmap [p4_column][p4_row]== "~":
                    p4army=p4army-1
                    worldmap [p4_column][p4_row]= "X"
                for i in worldmap:
                    for j in i:
                        if j=="X":
                            p4army=p4army+1
                print("p4-available armys are now:")
                print(p4army)
        turn=True
    for line in worldmap:
        print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
    player1()



worldmap=["a","A","B","C","D","E","F","G","b","I","J","c","L","M","N","O","P","Q","R","S","T","U","V","W","d","Y","e","f"],["b","-","#","-","#","#","-","#","-","-","#","#","-","-","-","-","-","-","-","-","#","#","-","-","-","-","-","-"],["c","#","#","#","-","-","#","-","-","#","#","#","-","-","-","-","-","-","#","#","#","#","#","#","-","-","-","-"],["d","-","#","#","#","#","-","-","-","#","#","#","#","-","-","#","-","#","#","#","#","#","#","#","#","-","-","-"],["e","-","-","#","#","#","#","-","-","-","#","#","#","-","-","#","#","#","#","#","#","#","#","#","#","#","#","-"],["f","-","-","#","P","#","#","#","-","-","#","#","#","-","-","#","#","#","#","#","X","#","#","#","#","#","#","#"],["g","-","-","#","#","#","#","#","-","-","#","#","-","-","#","-","#","#","#","#","#","#","#","#","#","#","#","-"],["h","-","#","#","#","#","#","#","#","#","-","#","-","-","#","-","#","#","#","#","#","#","#","#","#","#","-","-"],["i","#","#","#","#","#","#","#","#","-","-","-","~","#","-","#","#","#","#","#","#","#","#","#","-","~","-","-"],["j","#","#","#","#","#","#","#","#","-","-","#","-","#","#","#","#","#","#","#","#","#","#","#","-","#","-","-"],["k","#","#","#","#","#","#","#","-","-","-","~","-","-","#","#","#","#","#","#","#","#","#","#","-","#","-","-"],["l","_","#","#","#","#","_","#","_","_","_","_","#","#","#","#","#","#","#","#","#","#","#","_","#","#","-","-"],["m","_","_","#","#","_","_","#","_","_","#","#","_","_","#","#","#","#","#","#","#","#","_","_","#","-","-","-"],["n","_","_","#","#","_","_","~","_","#","#","#","#","#","_","#","#","#","#","#","_","_","_","_","_","-","-","-"],["o","_","_","_","#","_","_","_","#","#","#","#","#","#","#","_","_","#","#","_","_","_","_","_","_","-","-","-"],["p","_","_","_","#","#","_","_","#","#","#","#","#","#","#","_","_","#","#","_","_","#","_","_","_","-","-","-"],["r","_","_","#","#","#","#","_","_","#","#","#","#","#","#","_","~","_","#","_","#","#","_","_","_","-","-","-"],["q","_","_","#","#","#","#","Z","~","#","#","#","#","#","#","#","_","_","#","~","#","_","#","#","#","-","-","-"],["r","_","_","#","#","#","#","#","_","_","#","#","#","#","#","_","_","_","_","-","_","_","_","#","_","-","-","-"],["s","_","_","_","_","#","#","#","_","_","#","#","#","#","_","_","_","_","_","-","_","-","_","~","_","-","-","-"],["t","_","_","_","#","#","#","_","_","_","#","#","#","#","_","_","_","_","-","-","-","-","#","-","#","-","-","-"],["u","_","_","_","#","#","#","_","_","_","-","#","#","#","_","_","_","-","-","-","-","-","#","#","#","-","-","-"],["v","_","_","_","#","#","_","_","_","_","-","#","#","_","#","_","_","-","-","-","-","#","#","#","#","#","-","-"],["w","_","_","_","#","#","_","_","_","_","-","#","#","_","#","~","~","~","~","~","#","#","#","#","K","#","-","-"],["x","_","_","-","#","_","_","_","_","_","_","#","#","_","_","_","_","_","_","-","-","#","#","#","#","-","-","-"],["y","_","_","-","#","_","_","_","_","_","_","#","#","_","_","_","_","_","_","-","-","_","#","-","#","~","-","#"],["z","_","_","_","#","~","#","~","_","#","_","_","~","_","#","_","_","_","_","_","-","_","_","-","#","-","#","-"],["A","_","_","_","-","_","_","_","#","#","#","#","#","#","#","#","#","_","_","_","_","_","_","-","-","-","-","-"],

rows = len(worldmap)
columns = len(worldmap[0])

for line in worldmap:
    print (layout.format(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27]))
           

player1()
 
