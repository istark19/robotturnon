import RoboPiLib as RPL
import setup
import post_to_web as PTW
RPL.pinMode(16,RPL.INPUT)
PTW.state['d1'] = RPL.digitalRead(16)
PTW.post()
