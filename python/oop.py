## Object Oriented Programming

class Human():
    # Constructor - Method (class function) that runs when an object is instanciated
    def __init__(self, haircolor, eyecolor, skincolor):
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.skincolor = skincolor
        
    def get_haircolor():
        return self.haircolor

    def get_eyecolor():
        return self.eyecolor

    def get_skincolor():
        return self.skincolor

    def set_haircolor(new_haircolor):
        self.haircolor = new_haircolor

    def set_eyecolor(new_eyecolor):
        self.eyecolor = new_eyecolor

    def set_skincolor(new_skincolor):
        self.skincolor = new_skincolor