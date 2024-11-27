from string import  ascii_uppercase

class Chess:
    def __init__(self) -> None:
        
        # Maybe some day a bigger chessboard :)
        self.rows = 8
        self.columns = 8

        self.__emptyFieldCharacter = " "
        # self.field = [" "]*self.rows*self.columns
        self.field = self.generate_field()
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
                # column_list.append(self.__emptyFieldCharacter)
                column_list.append(str(x)) # For testing use. displays count in each cell
            # After the column for loop
            field.append(column_list)

        return field

    # -----------------------------------------------------------------------------

    def display_field(self):
        # Find a way to display a field
        result_text = "    " # tbh the spaces are since im to lazy to think of a way to align it

        # Add header of the board
        for character in ascii_uppercase[0:self.rows]:
            result_text += character + " "
        # at the end adding a break
        result_text += "\n"

        for column_number,column in enumerate(self.field):
            column_text = f"{str(column_number + 1)} | "
            row_merged_text = ""

            # Get all the values of the column together to print it.
            for row in column:
                row_merged_text += row + " "

            # Merging all the text so print will only be used once.
            result_text += column_text + row_merged_text + "\n"

        print(result_text)

    # -----------------------------------------------------------------------------

    def get_player_choice(self):
        pass

    # -----------------------------------------------------------------------------

    def switch_player(self):


    # -----------------------------------------------------------------------------

if __name__ == "__main__":
    chess = Chess()
    chess.display_field()