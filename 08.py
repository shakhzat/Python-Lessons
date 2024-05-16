'''
z=int(input())
s=0
for i in range(1,z+1,2):
    s=s+i
print(s)

a=int(input())
x=0
for i in range(a+1):
    if i%2==1:
        x=x+i
print(x)

a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    if i%2==0:
        s=s+i
print(s)

a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    if i%10==0:
        s=s+(-i)
print(s)

i=0
while i<5:
    print(i)
    i=i+2

i=30
while i>-1:
    print(i)
    i=i-1

i=0
while i<4:
    print(i**i)
    i=i+1
'''

a=int(input())
i=0
s=1
while i<a:
    i=i+1
    s=s*i
print(s)