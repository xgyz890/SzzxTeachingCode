a,b,c=-1,-2,-3

if a>=b:print("a>=b")
else:print("a<b")
print('..............')  


if a>b:
    print("a>b")
    print('1')
elif a==b:
     print("a=b")
     print('2')
else:
    print('a<b')
    print('3')
print('..............')  



if a>=b and a>=c:
    print("max=a")
print('1')
if b>=a and b>=c:
  print('max=b')
print('2')
if c>=a and c>=b:
    print('max=c')
print('3')
print('..............')  


if a>=b and a>=c:
    print("max=a")
if b>=a and b>=c:
    print('max=b')
else:
    print('max=c')
print('..............')  
