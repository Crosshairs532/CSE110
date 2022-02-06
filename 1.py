x=int(input("Enter the number:"))
if(x%2==0 ):
    print("invalid output")
else:
    for i in range(1, x+1):
        for j in range(1,x+1):
            if(i%2!=0):
                print(i,end="")
            else:
                if(j==1 or j==x):
                    print(i, end="")
                else:
        
                    print("#", end="")
        print()   
        
    