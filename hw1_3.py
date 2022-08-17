n=int(input())
s=n%60
m=(n//60)%60
h=n//60//60
print(f"{h}時{m}分{s}秒")
