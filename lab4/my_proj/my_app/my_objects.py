class vehicle():
    def __init__(self):
        self.type = 'generic vehicle'


class car (vehicle):
    def __init__(self, color, sound):
        self.color = color
        self._sound = sound
        self.wheels = 4

class motorcycle(vehicle):
    def __init__(self, color, sound):
        self.color= color
        self_sound = sound
        self.wheels = 2      

