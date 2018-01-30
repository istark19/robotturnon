import RoboPiLib as RPL
import setup
RPL.pinMode(16,RPL.INPUT)
PTW.state['d1'] = RPL.digitalRead(16)
PTW.post()
