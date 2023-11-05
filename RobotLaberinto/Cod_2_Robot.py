from machine import Pin
import time

#0 = NUMERO DEL PIN
sensor_izquierdo = Pin(0, Pin.IN)
sensor_central = Pin(0, Pin.IN)
sensor_derecho = Pin(0, Pin.IN)

motor_izquierdo = Pin(0, Pin.OUT)
motor_derecho = Pin(0, Pin.OUT)

def avanzar():
    motor_izquierdo.on()
    motor_derecho.on()

def retroceder():
    motor_izquierdo.off()
    motor_derecho.off()

def girar_izquierda():
    motor_izquierdo.off()
    motor_derecho.on()

def girar_derecha():
    motor_izquierdo.on()
    motor_derecho.off()

def detener():
    motor_izquierdo.off()
    motor_derecho.off()

def resolver_laberinto():
    while True:
        izquierdo = sensor_izquierdo.value()
        central = sensor_central.value()
        derecho = sensor_derecho.value()

        if izquierdo == 0 and central == 1 and derecho == 0:
            avanzar()
        elif izquierdo == 1 and central == 0 and derecho == 1:
            retroceder()
            time.sleep(1)
            girar_izquierda()
            time.sleep(0.5)
        elif izquierdo == 1 and central == 1 and derecho == 0:
            girar_izquierda()
        elif izquierdo == 0 and central == 1 and derecho == 1:
            girar_derecha()
        elif izquierdo == 1 and central == 1 and derecho == 1:
            detener()
            break

resolver_laberinto()
