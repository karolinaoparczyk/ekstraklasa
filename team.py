class Team:

    def __init__(self, name, points):
        self.name = name
        self.score = points

    def add_points(self, points):
        self.score = self.score + points