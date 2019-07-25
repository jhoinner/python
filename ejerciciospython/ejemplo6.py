edad = int(input("digite su edad"))
genero = input("digite sexo, H para hombre, M para mujer")
if edad>=18:
    if genero in'Hh':
        print ("Señor usted es mayor de edad")
    elif  genero in 'Mn':
        print ("Señorita usted es mayor de edad")
    else:
        print ("dato incorrecto")
else:
    if genero in 'Hh':
        print ("Niño usted es menor de edad")
    elif  genero in 'Mm':
        print ("Niña usted es Menor de edad")
    else:
        print ("dato incorrecto")
