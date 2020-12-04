class Forest:

    def __init__(self):
        self.forest = open('input','r').read().split('\n')
        self.forest = [ x for x in self.forest if x ]
        self.length = len(self.forest)
        self.width = len(self.forest[0])
        self.x = 0
        self.y = 0
        self.path = []

    def next_pos(self, dx, dy):
        self.x += dx
        self.y += dy

        while self.y > (self.width - 1):
            self.y -= self.width

        while self.y < 0:
            self.y = self.width + self.y

    def get_path(self, dx, dy):
        self.path.append((self.x, self.y))
        while self.x < (self.length - 1):
            self.next_pos(dx, dy)
            self.path.append((self.x, self.y))

    def count_trees(self):
        trees = 0

        for x,y in self.path:
            trees += self.forest[x][y] == '#'

        return(trees)

steps = [(1,1), (1,3), (1,5), (1,7), (2,1)]

trees = 1

for x,y in steps:
    f = Forest()
    f.get_path(x, y)
    trees *= f.count_trees()

print(trees)
