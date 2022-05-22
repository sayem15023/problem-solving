a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
d = 3.14159
t = .5 * a * c
cir = d * (c*c)
tra = ((a+b)/2)*c
s = (b*b)
r = (a*b)
print("TRIANGULO: %.3f"%t)
print("CIRCULO: %.3f"%cir)
print("TRAPEZIO: %.3f"%tra)
print("QUADRADO: %.3f"%s)
print("RETANGULO: %.3f"%r)