#import neccessary libaries
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


Window.clearcolor = (0, 0, 0, 1)
Builder.load_file("./calculator.kv") 

Window.size = (350, 550)
#create Classes
class CalculatorWidget(Widget):
    def clear(self): 
        self.ids.input_box.text = "0"

    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "Err" in prev_number:
            prev_number = ""

        if prev_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    def signs(self, sign):
            prev_number = self.ids.input_box.text
            self.ids.input_box.text = f"{prev_number}{sign}"

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number =prev_number[:-1]
        self.ids.input_box.text = prev_number

    def results(self):
        prev_number = self.ids.input_box.text
        
        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "Err"

    def pos_neg(self):
        prev_number = self.ids.input_box.text

        if "-" in prev_number:
            self.ids.input_box.text = prev_number.replace("-", "")

        else:
            self.ids.input_box.text = f"-{prev_number}"
   

       

class CalculatorApp(App):
    def build(self):
         return CalculatorWidget()

if __name__ ==  "__main__":
    CalculatorApp().run()
#at this point a blank app window should open when you debug

#we would now go back to the top before the classes to set a window size
#next we load the calculator.kv file using the methon Buildre.load_file()
#we then go to the calculator,kv file and write all our design of the calculator widget.



