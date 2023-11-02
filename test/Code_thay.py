#! /usr/bin/env python3
import sys
sys.path.append('/home/vinh/Desktop/test/Lora_Driver')

from Lora_Driver.IoT_Driver import mylora
Lora = mylora(verbose=False)
Lora.debug_on = 0


from time import sleep

Lora.set_freq(479)

while(1):
    val_sw1 = Lora.read_data(1,4)
    val_sw2 = Lora.read_data(1,5)
    val_sw3 = Lora.read_data(1,6)
    print(val_sw1, val_sw2, val_sw3)

    Lora.write_data(1,8,val_sw1)
    sleep(0.1)
    Lora.write_data(1,9,val_sw2)
    sleep(0.1)
    Lora.write_data(1,10,val_sw3)
    sleep(0.1)
