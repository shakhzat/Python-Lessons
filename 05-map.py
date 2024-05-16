#a,b=map(int,input().split())
#print(a+b)

#a,b=map(int,input().split())
#if a>0 and b>0:
#    print("I")
#elif a<0 and b>0:
#    print("II")
#elif a<0 and b<0:
#    print("III")
#else:
#    print("IV")

#a,b=map(int,input().split())
#if a>0:
#    if b>0:
#        print("I")
#    else:
#        print("IV")
#else:
#    if b>0:
#        print("II")
#    else:
#        print("III")

#a,b=map(int,input().split())
#c,d=map(int,input().split())
#e=int(input())
#x=a*60+b
#y=c*60+d
#if x-y>=e:
#    print("YES")
#else:
#    print("NO")

#a=int(input())
#b=int(input())
#c=float(input())
#x=(b-a)*c
#print(x)

#a=int(input())
#b=int(input())
#c=float(input())
#if a<b:
#    x=c*(b-a)
#    print("2-car",x,"km")
#elif a>b:
#    y=c*(a-b)
#    print("1-car",y,"km")
#else:
#    print("ten")

#a,b=map(int,input().split())
#c,d=map(int,input().split())
#x=a*b
#y=c*d
#if x<y:
#    print("2-car",y-x)
#elif x>y:
#    print("1-car",x-y)
#else:
#    print("ten")

#a=int(input())
#if 85<a<=100:
#    print(5)
#elif 66<a<=84:
#    print(4)
#elif 40<a<=65:
#    print(3)
#else:
#    print(2)

#a=int(input())
#b=int(input())
#c=int(input())
#z=a*0.25+b*0.25+c*0.5
#if 85<z<=100:
#    print(5)
#elif 66<z<=84:
#    print(4)
#elif 40<z<=65:
#    print(3)
#else:
#    print(2)

a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
x=a*0.25+c*0.25+e*0.5
y=b*0.25+d*0.25+f*0.5
print(x,y)
if 85<x<=100:
    print(5)
    m=5
elif 66<x<=84:
    print(4)
    m=4
elif 40<x<=65:
    m=3
    print(3)
else:
    m=2
    print(2)
if 85<y<=100:
    print(5)
    n=5
elif 66<y<=84:
    print(4)
    n=4
elif 40<y<=65:
    print(3)
    n=3
else:
    n=2
    print(2)
if m>n:
    print("uttym")
elif m<n:
    print("utyldym")
else:
    print("ten")





















