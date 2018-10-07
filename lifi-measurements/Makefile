INO = lifi-measurements.ino
CC = arduino
BOARD = arduino:avr:uno
PORT := $(shell ls /dev/tty* | grep "ttyACM")

upload:
	$(CC) -v --board $(BOARD) --port $(PORT) --upload $(INO)

verify: $(INO)
	$(CC) -v --board $(BOARD) --verify $< 

output: upload
	cat $(PORT)

