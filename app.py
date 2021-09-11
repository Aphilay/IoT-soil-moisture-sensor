from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)


import time
#imports the ADC class to interact with a virtual analog to digital converter that can connect to a CounterFit sensor.
from counterfit_shims_grove.adc import ADC
#This statement imports the GroveRelay from the Grove Python shim libraries to interact with the virtual Grove relay.
from counterfit_shims_grove.grove_relay import GroveRelay


#create instance of the ADC class
adc = ADC()
#create a GroveRelay instance:
relay = GroveRelay(5)

while True:
    soil_moisture = adc.read(0)
    print("Soil moisture:", soil_moisture)
  
    time.sleep(5)

    if soil_moisture > 450:
        print("Soil Moisture is too low, turning relay on.")
        relay.on()
    else:
        print("Soil Moisture is ok, turning relay off.")
        relay.off()

    #to test the relay
    # relay.on()
    # time.sleep(.5)
    # relay.off()