a, b, c = map(int, input().split())
d = int(input()) 

def hour_plus(a):
    tmp = int(a/24)
    a-=(tmp*24)
    return a

def min_plus(a, b):
    tmp = int(b/60) 
    a+=tmp 
    b -= tmp*60
    return a, b

def sec_plus(b, c):
    tmp = int(c/60)
    b+=tmp
    c-=tmp*60
    return b, c

min = int(d/60) 
cho = int(d%60) 
   
b+=min #140
if b >= 60: 
    a, b = min_plus(a,b)
if a>=24:
     a = hour_plus(a)
    
c+=cho
if c>=60:
    b, c = sec_plus(b, c)
if b>=60:
    a, b = min_plus(a,b)
if a>=24:
    a = hour_plus(a)

print(int(a),int(b),int(c))