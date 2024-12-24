class Bot:
    def next_move(self, req):
        # mock request
        # {
        #   'pos': {'pos_x': 2, 'pos_y': 5},
        #   'opp': {'pos_x': 9, 'pos_y': 2},
        #   'flag1': {'pos_x': 2, 'pos_y': 5},
        #   'flag2': {'pos_x': 9, 'pos_y': 2},
        #   'portal': {'pos_x': 3, 'pos_y': 3},
        #   'tree': [
        #               {'pos_x': 7, 'pos_y': 4},
        #               {'pos_x': 1, 'pos_y': 7},
        #               {'pos_x': 8, 'pos_y': 7}
        #           ],
        #   'rock': [
        #               {'pos_x': 8, 'pos_y': 4},
        #               {'pos_x': 9, 'pos_y': 3}
        #           ]
        # }

        # Extract positions
        pos = req["pos"]  # Player's position
        flag = req["flag1"]  # Player's flag
        opp = req["opp"]  # Opponent's position
        opp_flag = req["flag2"]  # Opponent's flag
        portal = req["portal"]  # Portal's position
        tree = req["tree"]  # Tree's positions array with 3
        rock = req["rock"]  # Rock's Array with 2

        # write bot logic here.....
        x = pos["pos_x"]
        y = pos["pos_y"]

        # return next move by x, y
        return x, y


bot1 = Bot(req)

while:
    bot1.next_move(req)
    bot2.next_move

