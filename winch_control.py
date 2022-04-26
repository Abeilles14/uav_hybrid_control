import time
import sys
import mecanum
import drive
import math
import logging
import odroid_wiringpi as wpi
from pwm import PWM
from constants import *
from motor_specs import MOTORS
from TB9051FTG import TB9051FTG
from PCA9685 import PCA9685
from utils import remap_range
from PID_controller import PID
from encoder import Encoder

logging.getLogger("Adafruit_I2C.Device.Bus.{0}.Address.{1:#0X}".format(0, 0X40)).setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
uaslog = logging.getLogger("UASlogger")

PIN_A = 27
PIN_B = 23
PIN_X = 26
PIN_Y = 10

PIN_LJSX = 25
PIN_LJSY = 29

class WinchControl:
    def __init__(self):
        uaslog.info("Starting Motor Drive System init...")

        ######################
        # INIT REMOTE VALUES #
        ######################
        self.ljs_x = 0.0
        self.ljs_y = 0.0
        self.ljs_sw = 1
        self.rjs_x = 0.0
        self.rjs_y = 0.0
        self.rjs_sw = 1

        ##################
        # INIT GPIO PINS #
        ##################
        self.init_gpio()

        ############
        # INIT PWM #
        ############
        uaslog.debug("Init PWM...")
        self.pwm = PWM(address=I2C_CHIP, busnum=I2C_BUS, debug=False)
        self.pwm.setPWMFreq(FREQUENCY)

        ###############
        # INIT MOTORS #
        ###############
        
        # DC BRUSHED
        self.pololu_0 = TB9051FTG(channel=CHANNEL0, freq=300, pin_in=MOTORS["pololu_0"]["enc_pins"], pin_out=MOTORS["pololu_0"]["driver_pins"], single=True)
        self.pololu_0.reset(self.pwm)

        uaslog.info("Motor Drive System init complete! Starting main routine...")
    
    def loop(self):
        uaslog.info("Starting Winch Control Test...")
        uaslog.info("Joystick will control winch motor to go up or down.")
        try:
            while True:
                # READ JOYSTICK
                raw_ljs_x = wpi.analogRead(PIN_LJSX)
                raw_ljs_y = wpi.analogRead(PIN_LJSY)

                self.ljs_x, self.ljs_y = remap_range(raw_ljs_x, raw_ljs_y)

                if self.ljs_y < THRESHOLD_HIGH and self.ljs_y > THRESHOLD_LOW:
                    self.ljs_y = 0.0
                if self.ljs_x < THRESHOLD_HIGH and self.ljs_x > THRESHOLD_LOW:
                    self.ljs_x = 0.0
                
                print(f"sX: {self.ljs_x:.4f}, sY: {self.ljs_y:.4f}")

                if self.ljs_y > THRESHOLD_HIGH + 0.1:
                    self.pololu_0.forward(self.pwm, dutycycle=WINCH_DC_SPEED)
                elif self.ljs_y < THRESHOLD_LOW - 0.1:
                    self.pololu_0.backward(self.pwm, dutycycle=WINCH_DC_SPEED)
                else:
                    self.pololu_0.backward(self.pwm, dutycycle=0)

        except KeyboardInterrupt:
            uaslog.info("Joystick Control Test Complete!")
            self.cleanup()
            sys.exit(0)

    def init_gpio(self):
        uaslog.info("Init GPIO...")
        # unexport pins
        for pin in range(0, 256):
            file = open("/sys/class/gpio/unexport","w")
            file.write(str(pin))

        # setup wpi
        wpi.wiringPiSetup()
        
        # set pin mode
        for pin in GPIO_IN:
            wpi.pinMode(pin, wpi.INPUT)
            wpi.pullUpDnControl(pin, wpi.GPIO.PUD_UP)

        for pin in GPIO_OUT:
            wpi.pinMode(pin, wpi.OUTPUT)
            # init out pins low
            wpi.digitalWrite(pin, 0)
        uaslog.info("Init GPIO complete!")

    def cleanup(self):
        uaslog.info("Cleaning up driver system...")
        # reset motors
        self.pololu_0.reset(self.pwm)
        
        # unexport pins
        for pin in range(0, 256):
            file = open("/sys/class/gpio/unexport","w")
            file.write(str(pin))

        uaslog.info("Driver system cleanup complete!")