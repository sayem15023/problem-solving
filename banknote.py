import math
n= float(input())
hundred = math.floor(n//100)
n= n%100
fifty = math.floor(n//50)
n = n%50
twenty =math.floor(n//20)
n = n%20
ten = math.floor(n//10)
n = n%10
five = math.floor(n//5)
n = n%5
two = math.floor(n//2)
n = n%2
one = math.floor(n//1)
n = n%1
a = math.floor(n//.50)
n = n%.50
c = math.floor(n//.25)
n = n%.25
tenpoy = math.floor(n//.10)
n = n%.10
fivepoy = math.floor(n//.05)
n = n%.05
onepoy = math.floor(n//.01)
print(f'''NOTAS:
{hundred} nota(s) de R$ 100.00
{fifty} nota(s) de R$ 50.00
{twenty} nota(s) de R$ 20.00
{ten} nota(s) de R$ 10.00
{five} nota(s) de R$ 5.00
{two} nota(s) de R$ 2.00
MOEDAS:
{one} moeda(s) de R$ 1.00
{a} moeda(s) de R$ 0.50
{c} moeda(s) de R$ 0.25
{tenpoy} moeda(s) de R$ 0.10
{fivepoy} moeda(s) de R$ 0.05
{onepoy} moeda(s) de R$ 0.01
''')