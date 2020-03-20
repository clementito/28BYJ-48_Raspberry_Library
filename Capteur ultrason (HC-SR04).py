import Library_HCSR04 as capteur

capteur.pin(2,3) #Numéro du GPIO
distance = capteur.mesurer()

print(distance)