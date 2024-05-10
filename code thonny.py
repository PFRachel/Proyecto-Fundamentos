import board  # se importa la biblioteca
import digitalio  # se importa la biblioteca
import time   # se importa la biblioteca
import busio  # se importa la biblioteca
import analogio  # se importa la biblioteca
import random   # se importa la biblioteca

# SE NOMBRAS LOS PINES 
data_pin = board.GP18
clock_pin = board.GP19

jugador_1 =0
jugador_2 =0
jugador_1 == False
jugador_2 == False


paleta_uno_pin = board.GP4
paleta_dos_pin = board.GP6
paleta_tres_pin = board.GP9
paleta_cuatro_pin = board.GP10
paleta_cinco_pin = board.GP11
paleta_seis_pin = board.GP12

# Configura el pin del buzzer
buzzer_pin = board.GP21

poten = board.GP26
potenciometro = analogio.AnalogIn(poten)



buzzer = digitalio.DigitalInOut(buzzer_pin)
buzzer.direction = digitalio.Direction.OUTPUT

# configura el pin de las paletas 
paleta_uno = digitalio.DigitalInOut(paleta_uno_pin)
paleta_uno.direction = digitalio.Direction.INPUT
paleta_uno.pull = digitalio.Pull.DOWN

paleta_dos = digitalio.DigitalInOut(paleta_dos_pin)
paleta_dos.direction = digitalio.Direction.INPUT
paleta_dos.pull = digitalio.Pull.DOWN

paleta_tres = digitalio.DigitalInOut(paleta_tres_pin)
paleta_tres.direction = digitalio.Direction.INPUT
paleta_tres.pull = digitalio.Pull.DOWN

paleta_cuatro = digitalio.DigitalInOut(paleta_cuatro_pin)
paleta_cuatro.direction = digitalio.Direction.INPUT
paleta_cuatro.pull = digitalio.Pull.DOWN

paleta_cinco = digitalio.DigitalInOut(paleta_cinco_pin)
paleta_cinco.direction = digitalio.Direction.INPUT
paleta_cinco.pull = digitalio.Pull.DOWN

paleta_seis = digitalio.DigitalInOut(paleta_seis_pin)
paleta_seis.direction = digitalio.Direction.INPUT
paleta_seis.pull = digitalio.Pull.DOWN
#configuracion de los data y del colck para los LEDS 
data = digitalio.DigitalInOut(data_pin)
data.direction = digitalio.Direction.OUTPUT

clock = digitalio.DigitalInOut(clock_pin)
clock.direction = digitalio.Direction.OUTPUT

# Botón
button_pin = board.GP5
button = digitalio.DigitalInOut(button_pin)
button.switch_to_input(pull=digitalio.Pull.DOWN)

lista = ["Start", "Settings", "Info", "About"]

def index_map(pot_value, list_length):
    max_pot_value = 65535
    index = int(pot_value / max_pot_value * list_length)
    return min(index, list_length - 1)

while True:
    lectura = potenciometro.value
    
    new_index = index_map(lectura, len(lista))
    print(lista[new_index])

    if button.value:
        selected_value = lista[new_index]
        print("Last pick:", selected_value)
        break

    time.sleep(0.1)
    
    

# programa 
def iniciar_leds():
    clock.value = 0
    data.value = 1
    clock.value = 1
    time.sleep(0.1)
    
    for i in range(16):
        clock.value = 0
        data.value = 0
        clock.value = 1
        time.sleep(0.1)
        
#iniciar_leds()
def poner_led(led_encender):
    clock.value = 0
    data.value = 1
    clock.value = 1
    
    for i in range(led_encender):
        clock.value = 0
        data.value = 0
        clock.value = 1
        

while True:
    
    uno = paleta_uno.value
    dos = paleta_dos.value
    tres = paleta_tres.value
    cuatro = paleta_cuatro.value
    cinco = paleta_cinco.value
    seis = paleta_seis.value
    print(f'{uno},{dos},{tres},{cuatro},{cinco},{seis}')
    if jugador_1 == True:
        
        while i <5:
            portero = random.randint(0,3)
            if uno and portero == 0:
                poner_led(portero)
                gol = 0
            elif dos and portero == 1:
                poner_led(portero)
                gol = 0
            elif tres and portero == 2:
                poner_led(portero)
                gol = 0
            elif cuatro and portero == 3:
                poner_led(portero)
                gol = 0
            else:
                poner_led(portero)
                buzzer.value = True  # Enciende el buzzer
                time.sleep(0.5)  # Espera medio segundo
                buzzer.value = False  # Apaga el buzzer
                iniciar_leds()
                gol = 1
                
    if jugador_2 == True:
        while i <5:
            portero = random.randint(0,3)
            if uno and portero == 0:
                poner_led(portero)
                gol = 0
            elif dos and portero == 1:
                poner_led(portero)
                gol = 0
            elif tres and portero == 2:
                poner_led(portero)
                gol = 0
            elif cuatro and portero == 3:
                poner_led(portero)
                gol = 0
            else:
                poner_led(portero)
                buzzer.value = True  # Enciende el buzzer
                time.sleep(0.5)  # Espera medio segundo
                buzzer.value = False  # Apaga el buzzer
                iniciar_leds()
                gol = 1
                
        

        
    time.sleep(0.5)   
    

    
    
    