# Register Addresses
MODE1           = 0x00
MODE2           = 0x01
SUBADR1         = 0x02
SUBADR2         = 0x03
SUBADR3         = 0x04
ALLCALLADR      = 0x05
LED0_ON_L       = 0x06
LED0_ON_H       = 0x07
LED0_OFF_L      = 0x08
LED0_OFF_H      = 0x09
LED1_ON_L       = 0x0A
LED1_ON_H       = 0x0B
LED1_OFF_L      = 0x0C
LED1_OFF_H      = 0x0D
LED2_ON_L       = 0x0E
LED2_ON_H       = 0x0F
LED2_OFF_L      = 0x10
LED2_OFF_H      = 0x11
LED3_ON_L       = 0x12
LED3_ON_H       = 0x13
LED3_OFF_L      = 0x14
LED3_OFF_H      = 0x15
LED4_ON_L       = 0x16
LED4_ON_H       = 0x17
LED4_OFF_L      = 0x18
LED4_OFF_H      = 0x19
LED5_ON_L       = 0x1A
LED5_ON_H       = 0x1B
LED5_OFF_L      = 0x1C
LED5_OFF_H      = 0x1D
LED6_ON_L       = 0x1E
LED6_ON_H       = 0x1F
LED6_OFF_L      = 0x20
LED6_OFF_H      = 0x21
LED7_ON_L       = 0x22
LED7_ON_H       = 0x23
LED7_OFF_L      = 0x24
LED7_OFF_H      = 0x25
LED8_ON_L       = 0x26
LED8_ON_H       = 0x27
LED8_OFF_L      = 0x28
LED8_OFF_H      = 0x29
LED9_ON_L       = 0x2A
LED9_ON_H       = 0x2B
LED9_OFF_L      = 0x2C
LED9_OFF_H      = 0x2D
LED10_ON_L      = 0x2E
LED10_ON_H      = 0x2F
LED10_OFF_L     = 0x30
LED10_OFF_H     = 0x31
ALLLED_ON_L     = 0xFA
ALLLED_ON_H     = 0xFB
ALLLED_OFF_L    = 0xFC
ALLLED_OFF_H    = 0xFD
PRESCALE        = 0xFE

# Channels
CHANNEL0 = [LED0_ON_L, LED0_ON_H, LED0_OFF_L, LED0_OFF_H]
CHANNEL1 = [LED1_ON_L, LED1_ON_H, LED1_OFF_L, LED1_OFF_H]
CHANNEL2 = [LED2_ON_L, LED2_ON_H, LED2_OFF_L, LED2_OFF_H]
CHANNEL3 = [LED3_ON_L, LED3_ON_H, LED3_OFF_L, LED3_OFF_H]
CHANNEL4 = [LED4_ON_L, LED4_ON_H, LED4_OFF_L, LED4_OFF_H]
CHANNEL5 = [LED5_ON_L, LED5_ON_H, LED5_OFF_L, LED5_OFF_H]
CHANNEL6 = [LED6_ON_L, LED6_ON_H, LED6_OFF_L, LED6_OFF_H]
CHANNEL7 = [LED7_ON_L, LED7_ON_H, LED7_OFF_L, LED7_OFF_H]
CHANNEL8 = [LED8_ON_L, LED8_ON_H, LED8_OFF_L, LED8_OFF_H]
CHANNEL9 = [LED9_ON_L, LED9_ON_H, LED9_OFF_L, LED9_OFF_H]
CHANNEL10 = [LED10_ON_L, LED10_ON_H, LED10_OFF_L, LED10_OFF_H]

# I2C parameter defaults
I2C_BUS = 0
I2C_DEV = "/dev/i2c-0"
I2C_CHIP = 0x40

# PCA9685
COUNTER_SIZE = 4096.0
CLK = 25000000.0

# ACTUONIX L16-100-63-6-R SPECS
STROKE = 100.0    # mm
DC_RANGE = 30.0   # %
