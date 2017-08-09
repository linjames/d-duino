from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
from network import WLAN,STA_IF

sta_if = WLAN(STA_IF)

i2c = I2C(sda=Pin(5), scl=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)

if sta_if.isconnected():
    oled.text("connected", 0, 0)
    oled.text(sta_if.ifconfig()[0],0,10)
else:
    oled.text("not connected", 0, 0)

oled.show()
    
