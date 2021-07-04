## Object Oriented Programming

class Human:
    # Constructor - Method (class function) that runs when an object is instanciated
    def __init__(self, haircolor, eyecolor, skincolor):
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.skincolor = skincolor
        
    def get_haircolor(self):
        return self.haircolor

    def get_eyecolor(self):
        return self.eyecolor

    def get_skincolor(self):
        return self.skincolor

    def set_haircolor(self, new_haircolor):
        self.haircolor = new_haircolor

    def set_eyecolor(self, new_eyecolor):
        self.eyecolor = new_eyecolor

    def set_skincolor(self, new_skincolor):
        self.skincolor = new_skincolor