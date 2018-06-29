# @program - camStick
# This will be for the rig
# to look into high nest

from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()

    camera.start_preview()
    sleep(10)
    camera.stop_preview()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Shuting down")
        #GPIO.cleanup() #Will need this when we implement LEDs
sys.exit(0)
