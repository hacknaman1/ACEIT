n = int(input("Enter the number of rows: "))
i=1;j=0
while(i<=n):
    while(j<=i-1):
        print("* ",end="")
        j+=1
    print("\r")
    j=0;i+=1
