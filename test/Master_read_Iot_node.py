#! /usr/bin/env python3
import sys
sys.path.append('/home/pi/Destop/Code_V5/Lab_9_Lora/Demo/Lora_Driver')

from Lora_Driver.Iot_Driver import myLora
Lora = myLora(verbose=False)
Lora.debug_on = 0


from time import sleep

Lora.set_freq(434) #node 13

while(1):
    val_sw1 = Lora.read_data(1,4)
    val_sw2 = Lora.read_data(1,5)
    val_sw3 = Lora.read_data(1,6)
    print(val_sw1)
    print(val_sw2)
    print(val_sw3)

    Lora.write_data(1,9,val_sw1)
    Lora.write_data(1,8,val_sw2)
    sleep(0.1)