inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número mayor al primero: "))
if inicio <= fin:
   print("extremos incluidos")
   for i in range (inicio , fin +1):
       print(i) 
   print("extremos excluidos") 
   for i in range (inicio +1 , fin):
       print(i)   
else:
    print ("Ingreso incorrecto")       