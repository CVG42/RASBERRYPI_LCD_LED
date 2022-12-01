from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from gpiozero import LED
from gpiozero import Button
import pdb

lcd = LCD()
green = LED(27)
red = LED(23)
buttonGreen = Button(17)
buttonRed = Button(24)
def safe_exit(signum, frame):
    exit(1)
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

def Decision(answer):
    if buttonGreen.is_pressed:
        green.on()
        answer = True
    else:
        green.off()
    if buttonRed.is_pressed:
        red.on()
        answer = False
    else:
        red.off()
    
    return answer

try:
    lcd.text("Siempre vas a lo seguro?", 1)
    print ("Siempre vas a lo seguro? ")
    while True:
        answer = 3
        answer = Decision(answer)
        if answer == True:
            print ("Te gusta el clima frio?")
            lcd.text("Te gusta el clima frio?", 1)
            while True:
                answer = 3
                answer = Decision(answer)
                if answer == True:
                    print ("Prefieres lo dulce a los salado?")
                    lcd.text("Prefieres lo dulce a los salado?", 1)
                    while True:
                        answer = 3
                        answer = Decision(answer)
                        if answer == True:
                            print ("Eres una pizza Hawaiiana")
                            lcd.text("Eres una pizza hawaiiana, no te quieres :(", 1)
                        elif answer == False:
                            print ("Eres una pizza de jamon")
                            lcd.text("Eres una pizza de jamon, que rarito =S",1)
                elif answer == False:
                    print ("Te gusta jugar al futbol?")
                    lcd.text("Te gusta jugar al futbol?", 1)
                    while True:
                        answer = 3
                        answer = Decision(answer)
                        if answer == True:
                            print ("Eres una pizza de Pepperoni")
                            lcd.text("Eres una pizza pepperoni, que basico :|", 1)
                        elif answer == False:
                            print ("Eres una pizza de queso")
                            lcd.text("Eres una pizza de queso, que aburrido -_-",1)
        elif answer == False:
            print ("Te gusta salir con amigos?")
            lcd.text("Te gusta salir con amigos?", 1)
            while True:
                answer = 3
                answer = Decision(answer)
                if answer == True:
                    print ("Tus amigos piensan que eres normal?")
                    lcd.text("Tus amigos piensan que eres normal?", 1)
                    while True:
                        answer = 3
                        answer = Decision(answer)
                        if answer == True:
                            print ("Eres una pizza de carnes")
                            lcd.text("Eres una pizza carnes, que buenos gustos :)", 1)
                        elif answer == False:
                            print ("Eres una pizza vegetariana")
                            lcd.text("Eres una pizza vegetariana, que triste vida u.u",1)
                elif answer == False:
                    print ("Juzgas a un libro por su portada?")
                    lcd.text("Juzgas a un libro por su portada?", 1)
                    while True:
                        answer = 3
                        answer = Decision(answer)
                        if answer == True:
                            print ("Eres una pizza Margueritta")
                            lcd.text("Eres una pizza Margueritta, te crees muy fancy uwu", 1)
                        elif answer == False:
                            print ("Eres una pizza mexicana")
                            lcd.text("Eres una pizza mexicana, ahuevo :D",1)
    
    pause()
    
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
