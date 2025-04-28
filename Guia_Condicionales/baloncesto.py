altura = float(input("¿Cuánto mides? "))
if altura >= 1.60 and altura <= 1.79:
    print("Juegas en escolta")
elif altura >= 1.80 and altura <= 1.99:
    print("Juegas en Alero")
elif altura >= 2.00 :
    print("Juegas en Pivot")
else:
       print("Juegas en Base")  
