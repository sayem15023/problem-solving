x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))
ans = ((x2-x1)**2 + (y2-y1)**2)**.5
print("%.4f"%ans)