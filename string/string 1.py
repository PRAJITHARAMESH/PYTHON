a=input("enter a sring")
if len(a)<2:
 result=''
else:
 result=a[:2]+a[-2:]
print("result",result)
