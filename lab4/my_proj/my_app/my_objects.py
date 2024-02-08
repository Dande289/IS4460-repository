class vehicle():
    def __init__(self, make, model, year, color, sound):
        self.type = 'generic vehicle'
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.sound = sound


class car (vehicle):
    def __init__(self, color, sound):
        self.color = color
        self._sound = sound
        self.wheels = 4
    
    def honk(self):
        return self._sound

class motorcycle (vehicle):
    def __init__(self, color, sound, make, year):
        self.color= color
        self.sound = sound
        self.make = make
        self.year = year
        self.wheels = 2      

