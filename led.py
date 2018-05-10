from gpiozero import LED, Button 
from time import sleep

led = LED(17)
button = Button(16)

while True:
    button.wait_for_press()
    print("LED on")
    led.on()
    print("LED off")
    led.off()

