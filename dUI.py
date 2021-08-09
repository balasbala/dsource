from PyQt5 import QtCore,QtGui,QtWidgets
from dsource import Ui_form
from RGB import RGB_set
from Temp_Humid import SI7006_TH
from amb_RGB import BH1745
from DAC import MCP4725
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys

class pihatui(QtWidgets.QMainWindow,Ui_form):
    
    def __init__(self):
        super(pihatui,self).__init__()
        self.ui = Ui_form()
        self.rgb = RGB_set()
        self.th = SI7006_TH()
        self.amb_rgb = BH1745()
        self.dac = MCP4725()
        self.ui.setupUi(self)
        self.ui.button_RED.toggled.connect(self.button_RED)
        self.ui.button_GREEN.toggled.connect(self.button_GREEN)
        self.ui.button_BLUE.toggled.connect(self.button_BLUE)
        self.ui.button_refresh.pressed.connect(self.temp_humid_amb)
        self.ui.slider.valueChanged.connect(self.changeValue)
        self.ui.keypad_0.pressed.connect(self.key_0)
        self.ui.keypad_1.pressed.connect(self.key_1)
        self.ui.keypad_2.pressed.connect(self.key_2)
        self.ui.keypad_3.pressed.connect(self.key_3)
        self.ui.keypad_4.pressed.connect(self.key_4)
        self.ui.keypad_5.pressed.connect(self.key_5)
        self.ui.keypad_6.pressed.connect(self.key_6)
        self.ui.keypad_7.pressed.connect(self.key_7)
        self.ui.keypad_8.pressed.connect(self.key_8)
        self.ui.keypad_9.pressed.connect(self.key_9)
        self.ui.keypad_star.pressed.connect(self.key_star)
        self.ui.keypad_hash.pressed.connect(self.key_hash)
        self.ui.keypad_a.pressed.connect(self.key_A)
        self.ui.keypad_b.pressed.connect(self.key_B)
        self.ui.keypad_c.pressed.connect(self.key_C)
        self.ui.keypad_d.pressed.connect(self.key_D)
        '''self.ui.label_amb_red.setStyleSheet("color:rgb(self.redvalue,0,0)")
        self.ui.label_amb_green.setStyleSheet("color:rgb(0,self.greenvalue,0)")
        self.ui.label_amb_blue.setStyleSheet("color:rgb(0,0,self.bluevalue)")
        self.ui.label_amb_red.setStyleSheet("color:rgb(255,0,0)")'''
        
        
    def button_RED(self,value):
            if(value == True):
                print("RED is Selected")
                self.rgb.RED_toggle(1)
                self.ui.label_RED.setText("RED ON")
            else:
                print("RED is De_Seleced")
                self.rgb.RED_toggle(0)
                self.ui.label_RED.setText(" RED OFF")

    def button_GREEN(self,value):
            if(value == True):
                print("GREEN is Selected")
                self.rgb.GREEN_toggle(1)
                self.ui.label_GREEN.setText("GREEN ON")
            else:
                print("GREEN is De_Seleced")
                self.rgb.GREEN_toggle(0)
                self.ui.label_GREEN.setText("GREEN OFF")

    def button_BLUE(self,value):
            if(value == True):
                print("BLUE is Selected")
                self.rgb.BLUE_toggle(1)
                self.ui.label_BLUE.setText("BLUE ON")
            else:
                print("BLUE is De_Seleced")
                self.rgb.BLUE_toggle(0)
                self.ui.label_BLUE.setText("BLUE OFF")
    
    def temp_humid_amb(self):
        
        temperature = self.th.temperature_read()
        self.ui.button_temp.setText(f"{round(temperature,2)} *C")
        humidity = self.th.humidity_read()
        self.ui.button_humid.setText(f"{round(humidity,2)}%")

        red = self.amb_rgb.readRED()
        green = self.amb_rgb.readGREEN()
        blue = self.amb_rgb.readBLUE()
        redvalue = red/257
        greenvalue = green/257
        bluevalue = blue/257
        '''self.ui.button_amb_b.setStyleSheet("color:rgb(0,0,bluevalue)")
        self.ui.label_amb_red.setStyleSheet("color:rgb(self.redvalue,0,0)")
        self.ui.label_amb_green.setStyleSheet("color:rgb(0,self.greenvalue,0)")
        self.ui.label_amb_blue.setStyleSheet("color:rgb(0,0,self.bluevalue)")'''
        self.ui.button_amb_r.setText(str(round(red,2)))
        self.ui.button_amb_g.setText(str(round(green,2)))
        self.ui.button_amb_b.setText(str(round(blue,2)))
         
    def changeValue(self, value):
        voltage = value*41
        self.dac.dac_write(voltage)
        print(value)
        
    def key_0(self):
        str = self.ui.keypadLCD.text()
        str += '0'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_1(self):
        str = self.ui.keypadLCD.text()
        str += '1'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_2(self):
        str = self.ui.keypadLCD.text()
        str += '2'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_3(self):
        str = self.ui.keypadLCD.text()
        str += '3'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_4(self):
        str = self.ui.keypadLCD.text()
        str += '4'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_5(self):
        str = self.ui.keypadLCD.text()
        str += '5'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_6(self):
        str = self.ui.keypadLCD.text()
        str += '6'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_7(self):
        str = self.ui.keypadLCD.text()
        str += '7'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_8(self):
        str = self.ui.keypadLCD.text()
        str += '8'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_9(self):
        str = self.ui.keypadLCD.text()
        str += '9'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_A(self):
        str = self.ui.keypadLCD.text()
        str += 'A'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_B(self):
        str = self.ui.keypadLCD.text()
        str += 'B'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_C(self):
        str = self.ui.keypadLCD.text()
        str += 'C'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_D(self):
        str = self.ui.keypadLCD.text()
        str += 'D'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_star(self):
        str = self.ui.keypadLCD.text()
        str += '*'
        self.ui.keypadLCD.setText(str)
        print(str)
        
    def key_hash(self):
        str = self.ui.keypadLCD.text()
        str += '#'
        self.ui.keypadLCD.setText(str)
        print(str)
        
  
    
app = QtWidgets.QApplication(sys.argv)
window = pihatui()
window.show()
sys.exit(app.exec_())