#!/usr/bin/env python3

import time
import sys
from SX127x.LoRa import *
from SX127x.board_config import BOARD

BOARD.setup()
BOARD.reset()
#parser = LoRaArgumentParser("Lora tester")


class mylora(LoRa):
	payload = 0
	debug_on = 0
	tx_mode = 0
	def __init__(self, verbose=False):
		super(mylora, self).__init__(verbose)
		self.set_mode(MODE.SLEEP)
		self.set_dio_mapping([0] * 6)
		self.var=0
		#self.set_sync_word(0xa0)s
		self.set_pa_config(pa_select=1)
		assert(self.get_agc_auto_on() == 1)

	def on_rx_done(self):
		BOARD.led_on()
		if self.debug_on:
			print("\nRxDone")
		self.clear_irq_flags(RxDone=1)
		self.payload = self.read_payload(nocheck=True)
		if self.debug_on:
			print ("Receive: ")
			print(bytes(self.payload).decode("utf-8",'ignore')) # Receive DATA
		BOARD.led_off()
		time.sleep(0.01) # Wait for the client be ready
		self.var=1

	def on_tx_done(self):
		print("\nTxDone")
		BOARD.led_on()
		BOARD.led_off()
		print(self.get_irq_flags())

	def on_cad_done(self):
		print("\non_CadDone")
		print(self.get_irq_flags())

	def on_rx_timeout(self):
		print("\non_RxTimeout")
		print(self.get_irq_flags())

	def on_valid_header(self):
		print("\non_ValidHeader")
		print(self.get_irq_flags())

	def on_payload_crc_error(self):
		print("\non_PayloadCrcError")
		print(self.get_irq_flags())

	def on_fhss_change_channel(self):
		print("\non_FhssChangeChannel")
		print(self.get_irq_flags())

	def write_data(self, node_add, reg_add, data):
		if self.debug_on:
			print ("Send: data")
		#			   | 0 |	1  | 2 |   3  |  4  |  5  | 6 | 7 |
		# data frame = |255|NodeAdd|CMD|RegAdd|DataH|DataL|CRC|254|
		dataH = (data & 0xff00) >> 8
		dataL = data & 0x00ff
		data_send = [255,node_add,1,reg_add,dataH,dataL,0,254]
		if self.debug_on:
			print (data_send)
		self.write_payload(data_send) # Send data
		self.set_mode(MODE.TX)
		time.sleep(0.1) # there must be a better solution but sleep() works
		#self.reset_ptr_rx()
		#self.set_mode(MODE.RXCONT) # Receiver mode
		#time.sleep(0.01)
		
	def read_data(self, node_add, reg_add):
		self.var=0
		#			   | 0 |	1  | 2 |   3  |  4  |  5  | 6 | 7 |
		# data frame = |255|NodeAdd|CMD|RegAdd|DataH|DataL|CRC|254|
		data_send = [255,node_add,0,reg_add,0,0,0,254]
		if self.debug_on:
			print (data_send)
		self.write_payload(data_send) # Send data
		self.set_mode(MODE.TX)
		time.sleep(0.11) # there must be a better solution but sleep() works
		self.reset_ptr_rx()
		self.set_mode(MODE.RXSINGLE) # Receiver mode
		start_time = time.time()
		while (time.time() - start_time < 5 and self.var==0): # wait until receive data or 10s
			pass
		if (self.var==1):
			dataH = self.payload[2]
			dataL = self.payload[3]
		else:
			dataH = 0
			dataL = 0
		return (dataH*256+dataL)
	
