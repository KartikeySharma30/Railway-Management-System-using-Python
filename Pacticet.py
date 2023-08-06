n=int(input("Enter the no. of Records u Want to Put : "))
L=[]
F=open("Game.txt","w")
for i in range(0,n):
    a=input("Enter the Game No. :")
    b=input("Enter the Game Name :")
    c=input("Enter the No. of participants :")
    d=[a,b,c]
    d=str(d)
    L.append(d)
    F.writelines(L)
print(L)      
F.close()
l1=[]
print("Game NO.","Game Name","No. of Praticipants")
F=open("Game.txt","r")
D=F.readlines()
for v in D:
    if("BasketBall" in v):
        l1.append(v)
        for f in l1:
            print(f)
F.close()    
