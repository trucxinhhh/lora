#! /usr/bin/env python3
import sys
sys.path.append('/home/pi/Destop/Code_V5/Lab_9_Lora/Demo/Lora_Driver')

from Lora_Driver.Iot_Driver import myLora
Lora = myLora(verbose=False)
Lora.debug_on = 0
Lora.debug_on = 0

from time import sleep

Lora.set_freq(444)

while(1):
    val_sw1 = Lora.read_data(1,4)
    print(val_sw1)

    Lora.write_data(1,9,val_sw1)
    sleep(0.1)