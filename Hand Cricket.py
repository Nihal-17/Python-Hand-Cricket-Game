import random
def main():
    pname()
    toss(name)
    game(mf,name)
def pname():
    global name
    name=input("Enter your name (Default: Player): ")
    if(name==""):
        name="Player"
    else:
        pass
def toss(name):
    global mf
    con3=True
    while(con3):
        ptoss=input("Enter your choice(ODD or EVEN): ").upper()
        if ptoss not in ["ODD","EVEN"]:
            print("Invalid input")
            continue
        else:
            con3=False
    mt=random.randint(1,10)                                 
    pt=int(input("Enter a number (1-10): "))
    print("Computer:",mt)
    t=mt+pt
    if(t%2==0):
        print("Toss: Even")
        if(ptoss=="EVEN"):
            pc=input("Bat or Bowl: ").upper()
            print(name,"chose to ",pc," first.")
            if(pc=="BAT"):
                 mf="BOWL"
            else:
                 mf="BAT"

        else:
            mco=["BAT","BOWL"]
            mc=random.choice(mco)
            print("Computer chose to ",mc,"first.")
            mf=mc
            
    else:
        print("Toss: Odd")
        if(ptoss=="ODD"):
             pc=input("Bat or Bowl: ").upper()
             print(name, "chose to ",pc," first.")
             if(pc=="BAT"):
                 mf="BOWL"
             else:
                 mf="BAT"
             
        else:
            mco=["BAT","BOWL"]
            mc=random.choice(mco)
            print("Computer chose to ",mc,"first.")
            mf=mc        
def game(mf,name):
    global mbat,pbat
    mbat=0; pbat=0; con=True; con2=True
    if(mf=="BAT"):
        while(con==True):
            pchoice=input("Enter your choice (1-10): ")
            try:
                pchoice=int(pchoice)
                if pchoice < 1 or pchoice > 10:
                    print("Invalid input")
                    continue
            except ValueError:
                    print("Invalid input")
                    continue

            mchoice=random.randint(1,10)
            print("Computer: ",mchoice)
            if(mchoice!=int(pchoice)):
                mbat+=mchoice
                print("Computer current score: ", mbat)
            else:
                print("Computer Scored: ",mbat)
                print(name," need to score: ",(mbat+1))
                con=False
        while(pbat<(mbat+1) and con2==True):
            pchoice=input("Enter your choice (1-10): ")
            try:
                pchoice=int(pchoice)
                if pchoice < 1 or pchoice > 10:
                    print("Invalid input")
                    continue
            except ValueError:
                    print("Invalid input")
                    continue
            mchoice=random.randint(1,10)
            print("Computer: ",mchoice)
            if(int(pchoice)!=mchoice):
                pbat+=int(pchoice)
                print(name," current score: ",pbat)
            else:
                print(name," scored: ",pbat)
                con2=False
        if(pbat>mbat):
            print(name," won the match")
        else:
            print("Computer won the match")
    else:
        while(con==True):
            pchoice=input("Enter your choice (1-10): ")
            try:
                pchoice=int(pchoice)
                if pchoice < 1 or pchoice > 10:
                    print("Invalid input")
                    continue
            except ValueError:
                    print("Invalid input")
                    continue
            mchoice=random.randint(1,10)
            print("Computer: ",mchoice)
            if(int(pchoice)!=mchoice):
                pbat+=int(pchoice)
                print(name," current score: ",pbat)
            else:
                print(name," scored: ",pbat)
                print("Computer needs to score: ",(pbat+1))
                con=False
        while(mbat<(pbat+1) and con2==True):
            pchoice=input("Enter your choice (1-10): ")
            try:
                pchoice=int(pchoice)
                if pchoice < 1 or pchoice > 10:
                    print("Invalid input")
                    continue
            except ValueError:
                    print("Invalid input")
                    continue
            mchoice=random.randint(1,10)
            print("Computer: ",mchoice)
            if(mchoice!=int(pchoice)):
                mbat+=mchoice
                print("Computer current score: ", mbat)
            else:
                print("Computer scored: ",mbat)
                con2=False
        if(mbat>pbat):
            print("Computer won the match")
        else:
            print(name," won the match")
    return
main()