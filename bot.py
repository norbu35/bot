class Bot:
    init_pos = None
    prev_pos = None
    pos_x = None
    pos_y = None
    flag = None
    portal = None
    tree = None
    rock = None
    fire = None

    def __init__(self, req):
        self.init_pos = (req["pos"]["pos_x"], req["pos"]["pos_y"])
        self.pos_x = req["pos"]["pos_x"]
        self.pos_y = req["pos"]["pos_y"]
        self.portal = (req["portal"]["pos_x"], req["portal"]["pos_y"])
        self.flag = (req["flag1"]["pos_x"], req["flag1"]["pos_y"])
        self.tree = req["tree"]
        self.rock = req["rock"]

    def calc_next(self, req):
        self.is_u() and self.move_u()
        self.is_ur() and self.move_ur()
        self.is_r() and self.move_r()
        self.is_dr() and self.move_dr()
        self.is_d() and self.move_d()
        self.is_dl() and self.move_dl()
        self.is_l() and self.move_l()
        self.is_ul() and self.move_ul()

    def check_respawn(self):
        return self.pos_x == self.init_pos[0] and self.pos_y == self.init_pos[1]

    def mark_fire(self):
        if self.fire is None:
            self.fire = [(self.prev_pos[0], self.prev_pos[1])]
        else:
            self.fire.append(self.prev_pos[0], self.prev_pos[1])

    def check_flag(self)

    def is_u(self):
        return self.flag[0] == self.pos_x and self.flag[1] > self.pos_y

    def is_ur(self):
        return self.flag[0] > self.pos_x and self.flag[1] > self.pos_y

    def is_r(self):
        return self.flag[0] > self.pos_x and self.flag[1] == self.pos_y

    def is_dr(self):
        return self.flag[0] < self.pos_x and self.flag[1] < self.pos_y

    def is_d(self):
        return self.flag[0] == self.pos_x and self.flag[1] < self.pos_y

    def is_dl(self):
        return self.flag[0] < self.pos_x and self.flag[1] < self.pos_y

    def is_l(self):
        return self.flag[0] == self.pos_x and self.flag[1] < self.pos_y

    def is_ul(self):
        return self.flag[0] < self.pos_x and self.flag[1] > self.pos_y

    def move_u(self):
        self.pos_y += 1

    def move_ur(self):
        self.pos_x += 1
        self.pos_y += 1

    def move_r(self):
        self.pos_x += 1

    def move_dr(self):
        self.pos_x += 1
        self.pos_y -= 1

    def move_d(self):
        self.pos_y -= 1

    def move_dl(self):
        self.pos_x -= 1
        self.pos_y -= 1

    def move_l(self):
        self.pos_x -= 1

    def move_ul(self):
        self.pos_x -= 1
        self.pos_y += 1

    def next_move(self, req):
        self.pos_x = req["pos"]["pos_x"]
        self.pos_y = req["pos"]["pos_y"]

        if self.check_respawn():
            self.mark_fire()

        x = self.pos_x
        y = self.pos_y

        if self.prev_pos is None:
            self.prev_pos = (
                self.pos_x,
                self.pos_y,
            )  # storing previous position as a tuple
        else:
            self.prev_pos = (x, y)  # updating previous position

        return x, y
