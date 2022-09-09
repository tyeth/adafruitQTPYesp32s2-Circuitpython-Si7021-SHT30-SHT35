# adafruitQTPYesp32s2-Circuitpython-Si7021-SHT30-SHT35
Intended as a playground for local sensor testing and probably MQTT
Tested with CircuitPython 8.0.0-beta0 over wifi using web workflow (Need a .env file with wifi + portal settings), with one Sensiron SHT30/35 (not sure which) and one Silicon Integrated SI7021.

With thanks to Chris Balmer for his original code https://github.com/chrisbalmer/micropython-si7021,
adapted to lock/unlock the i2c bus for circuitpython here https://github.com/tyeth/micropython-si7021

You will need thesi7021.py file from my repo in the lib folder, along with the ciruitpython module adafruit_sht31d for your version of circuitpython