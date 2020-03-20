import time
import Library_28BYJ48 as moteur

#moteur.pin(IN1,IN2,IN3,IN4)
moteur.pin(24,25,8,7)

#moteur.avancer(angle en degré, vitesse en seconde/tour)
moteur.avancer(360,15)

time.sleep(1)

moteur.reculer(360,15)