#chap 4
# while 문

x=0

while (x<10):
    x+=1
    print("hello")
    
a=['foo','bar','baz']

while a:
    print(a.pop())

n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print('Loop Ended')  

m=5
while m>0:
    m-=1
    if m==2:
        continue
    print(m)
print('Loop Ended')  

#if 중첩

i=0
while i<=10:
    print('i:',i)
    if i==6:
        break
    i+=1

k=10
while k>0:
    k-=1
    print(k)
    if k==5:
        break
else:
    print('else out')

b=['foo','bar','baz','quz']
s='qux'
i=0
while i<len(b):
    if b[i]==s:
        break
    i+=1
else:
    print(s,'not found in list')


bb=['foo','bar','baz','quz']

while True:
    if not a:
        break
    print(a.pop())