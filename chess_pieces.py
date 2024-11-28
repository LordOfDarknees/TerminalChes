
class Pawn:
    def __init__(self, team:str):
        self.symbol = "P"
        self.timesUsed = 0
        self.team = team
        self.direction = "" # up or down white would be down

    def move_validation(self, new_position: tuple, current_position: tuple) -> bool:
        # Prevent moving in the X axis
        if not new_position[0] == current_position[0]:
            return False

        # Prevent stepping on the same spot
        if new_position == current_position:
            return False

        if














