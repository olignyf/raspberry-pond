import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Voltage divider to read 12V battery voltage (which could go up to 20V with solar panel connected)
R1 = 204
R2 = 98
VOLTAGE_DIVIDER_RATIO = (R1 + R2) / R2
# VOLTAGE_DIVIDER_RATIO = 1

i2c = busio.I2C(3,2)

# Create the ADS object and specify the gain
ads = ADS.ADS1115(address=0x48, i2c=i2c)
#ads = Adafruit_ADS1x15.ADS1015(address=0x48, bus=1)
ads.gain = 2/3

chan = AnalogIn(ads, ADS.P0)

# Continuously print the values
while True:
    try:
        voltage = chan.voltage*VOLTAGE_DIVIDER_RATIO
        print(f"A0 Voltage: {voltage:0.2f}V")
    except Exception as e:
        print(f"Failed to read", e)
        time.sleep(10)
    time.sleep(1)

