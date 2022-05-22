second = int(input())
minute = second//60
second %=60 
hours = minute//60
minute %= 60
print(f'{hours}:{minute}:{second}')
