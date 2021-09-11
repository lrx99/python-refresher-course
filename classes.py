class Character:
    alive = True
    def __init__(self, name):
        self.name = name
class Intro(Character):
    def __init__(self, name):
        super().__init__(name)

    def intro(self):
        print("Hi I am " + self.name +".")
class Item(Character):
    def __init__(self, name, item_name):
        super().__init__(name)
        self.item_name = item_name

    def whositem(self):
        print("This is " + self.name + "'s " + self.item_name + ".")

name = input("Who are you : ")
intro = Intro(name)
intro.intro()
item = Item(name, item_name="Excalibur")
item.whositem()
