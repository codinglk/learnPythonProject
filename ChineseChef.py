# Chinese Chef class, Inheritance example
from Chef import Chef


class ChineseChef(Chef):

# override function in python

    def make_special_dish(self):
        print("The chef makes a king cake")

    def make_fried_rice(self):
        print("The chef makes fried rice")
