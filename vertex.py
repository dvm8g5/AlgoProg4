
class Vertex:
    def __init__(self, color: str = None, distance: int = None, predecessor: int = None, index: int = None):
        self.color = color
        self.distance = distance
        self.predecessor = predecessor
        self.index = index

    def get_color(self):
        return self.color

    def get_distance(self):
        return self.distance

    def get_predecessor(self):
        return self.predecessor

    def get_index(self):
        return self.index

    def set_color_white(self):
        self.color = 'W'
        return

    def set_color_gray(self):
        self.color = 'G'
        return

    def set_color_black(self):
        self.color = 'B'
        return

    def set_predecessor(self, new_predecessor):
        self.predecessor = new_predecessor
        return

    def set_distance(self, new_distance):
        self.distance = new_distance
        return

    def set_id(self, new_id: int):
        self.index = new_id
        return

    def reinit(self, color: str = None, distance: int = None, predecessor: int = None):
        self.color = color
        self.distance = distance
        self.predecessor = predecessor
