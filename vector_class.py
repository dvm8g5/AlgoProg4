class vertex:
    color = None
    distance = None
    predesesor = None

    def get_color(self):
        return self.color
    def get_distance(self):
        return self.distance
    def get_predessesor(self):
        return self.predesesor

    def set_color_white(self):
        self.color = 'W'
        return
    def set_color_gray(self):
        self.color = 'G'
        return
    def set_color_black(self):
        self.color = 'B'
        return

    def set_predessesor(self, new_predessesor):
        self.predesesor = new_predessesor
        return

    def set_distance(self, new_distance):
        self.distance = new_distance
        return
