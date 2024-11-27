class Chess:
    def __init__(self) -> None:
        
        # Maybe some day a bigger chessboard :)
        self.rows = 8
        self.columns = 8

        self.__emptyFieldCharacter = " "
        self.field = [" "]*self.rows*self.columns
        self.Players = ["White", "Black"]
        self.currentPlayer = self.Players[0]

    # -----------------------------------------------------------------------------

    def generate_field(self) -> list[list]:
        """
        Generates a Field by the set number of  column's and row's
        :return: list[list] For each column it generates the number of rows. Just look at the code yourself darn it
        """
        field = []
        for i in range(self.columns):
            column_list = []

            # Column for loop
            for x in range(self.rows):
                column_list.append(self.__emptyFieldCharacter)

            # After the column for loop
            field.append(column_list)

        return field

    # -----------------------------------------------------------------------------

    def display_field(self):
        # Find a way to display a field
        pass

    # -----------------------------------------------------------------------------


if __name__ == "__main__":
    chess = Chess()
    chess.displayField()