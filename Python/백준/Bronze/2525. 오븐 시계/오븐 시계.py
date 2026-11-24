h, m = map(int, input().split())  
um = int(input())
rm = m + um

if rm >= 60:
  h += rm // 60  
  rm = rm % 60  

h %= 24 

print(h, rm)
