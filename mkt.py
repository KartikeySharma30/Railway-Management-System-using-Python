def test(s,a):
    str_u=s
    Str_a=a
    count=0
    for i in s:
        if(i==a):
            count+=1
    print(count)        
U_s=input("Enter The str")
U_a=input("Ënter The char")
test(U_s,U_a)
