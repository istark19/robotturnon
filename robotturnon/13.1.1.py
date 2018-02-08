import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 17
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()

  if RPL.digitalRead(sensor_pin) == 1:
     print "hello"
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(0,1000)
    
  if RPL.digitalRead(sensor_pin) == 0:
     print "yeah"
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(0,0)

