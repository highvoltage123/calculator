import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import cmath
from kivy.lang import Builder

# set the app size
Window.size = (500,700)

Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = ''

        # create a button pressing funtion
    def button_press(self, button):
        # create a variable containig whatever is in there
        prior = self.ids.calc_input.text

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # function that receive every math sign and concatenate what appears to the input box
    def math_sign(self, sign):
        # create a variable that contain whatever is sitting there
        prior = self.ids.calc_input.text
        if "math ERROR" in prior:
            prior= ""
        # concatenate whatever sign is passed

        self.ids.calc_input.text = f'{prior}{sign}'

    # create a decimal function
    def dot(self):
        # container for anything sitting there
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            self.ids.calc_input.text = f"{prior}."
        elif "+" in prior and "." not in prior:
            pass
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # create the remove function to remove the latest character on text box
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # create positive or negative function for +/- button
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text =f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
    # function for equal button
    def equal(self):
        # create a variable that contain whatever is sitting there
        prior = self.ids.calc_input.text
        # use try block for error handling
        try:
            # evaluation of everything in the input box
            answer = eval(prior)
            # print the answer to the screen
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "math ERROR"

# run the application


class Calculator(App):

    def build(self):
        return MyLayout()


calculator = Calculator()
calculator.run()
