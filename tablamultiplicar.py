
fila = 9
columna = 4

a='';

for i in range(fila+1):
    for b in range(columna+1):
        if i==0:
            a+=str(b) +" "
        elif b==0:
            a+=str(i) + " "
        else:
            a+=str(i*b) + " "
    a+="\n"
print (a)
