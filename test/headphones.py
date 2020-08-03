from test.switch import Switch


class Headphones:

    def __init__(self):
        self.switch = Switch()

    def turn_on(self):
        self.switch.swich(True)
        print(self.switch.state)

    def toggle(self):
        self.switch.swich(~self.switch.state)

