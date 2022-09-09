import board
import busio
import adafruit_sht31d
import time
print("Hello World!")

#create i2c interface
i2c = busio.I2C(board.SCL, board.SDA)

import si7021
try:
    temp_sensor = si7021.Si7021(i2c)
    print('Serial:              {value}'.format(value=temp_sensor.serial))
    print('Identifier:          {value}'.format(value=temp_sensor.identifier))
    print('Temperature:         {value}'.format(value=temp_sensor.temperature))
    print('Relative Humidity:   {value}'.format(
        value=temp_sensor.relative_humidity))

    temp_sensor.reset()
    print('\nModule reset.\n')

    print('Temperature:         {value}'.format(value=temp_sensor.temperature))
    print('Relative Humidity:   {value}'.format(
        value=temp_sensor.relative_humidity))

    print('Fahrenheit:          {value}'.format(
        value=si7021.convert_celcius_to_fahrenheit(temp_sensor.temperature)))
finally:
    print("si7021 done")


try:
#create sensor and set single-shot read mode
#sensors = (adafruit_sht31d.SHT31D(i2c),adafruit_sht31d.SHT31D(i2c,0x45))
#sensors[0].mode = adafruit_sht31d.MODE_SINGLE
#sensors[1].mode = adafruit_sht31d.MODE_SINGLE
    sensor=adafruit_sht31d.SHT31D(i2c)

    i=1
    loopcount = 0
    while True:
        i = (i==0)
        #sensor = sensors[i]
        print("(%1f,%2f,\"#%d\")" % (sensor.temperature, sensor.relative_humidity,i))
        #    loopcount += 1

        print('Temperature:         {value}'.format(value=temp_sensor.temperature))
        print('Relative Humidity:   {value}'.format(
            value=temp_sensor.relative_humidity))

        print('Fahrenheit:          {value}'.format(
            value=si7021.convert_celcius_to_fahrenheit(temp_sensor.temperature)))
        time.sleep(2)
        # every 10 passes turn on the heater for 1 second
        #    if loopcount == 10:
        #        loopcount = 0

finally:
    print("done")
    #d    

#
#