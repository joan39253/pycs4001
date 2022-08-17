try:
    a=int(input())
    b=int(input())
    n=a/b
    if(n*1000%10<5):
        n=int(n*100)/100
    else:
        n=(int(n*100)+1)/100
    print(n) #print(f"{n:.2f}")
except:
    print("請輸入正確數字格式")
