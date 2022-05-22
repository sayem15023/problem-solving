l1 = input().split(" ")
l2 = input().split(" ")
c1 , d1 , e1 = l1
a1, s1,d2 = l2
ans = (int(d1) * float(e1)) + (int(s1)* float(d2))
print("VALOR A PAGAR: R$ %.2f"%ans)