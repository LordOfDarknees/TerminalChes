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
        result_text = "     " # tbh the spaces are since im to lazy to think of a way to align it

        # create the Characters side of the board
        character_decorator_side = ""
        for character in ascii_uppercase[0:self.rows]:
            character_decorator_side += character + " "

        character_decorator_side += "\n" # at the end adding a break
        # ------------------------------------------------
        # failed since the underscore characters are not the same size as other characters vvvv
        # decorator_underscore = ""
        # for i in character_decorator_side:
        #     decorator_underscore += "-"
        # decorator_underscore += "\n"
        # ^^^^^^^^

        result_text += character_decorator_side # Add header of the board
        # result_text += decorator_underscore

        for column_number,column in enumerate(self.field):
            column_text = f"{str(column_number + 1)} | "
            row_merged_text = ""

            # Get all the values of the column together to print it.
            for row in column:
                row_merged_text += row + " "

            # Merging all the text so print will only be used once.
            # ColumnNR rows ColumnNR example: ---> 1 | 0 1 2 3 4 5 6 7 | 1 <---
            result_text += f"{str(column_number + 1)} |  {row_merged_text} | {str(column_number + 1)}\n"



        print(result_text)

    # -----------------------------------------------------------------------------

    def get_player_choice(self):
        user_choice = ""
        while user_choice == "":
            unfiltered_input = input()
            

    # -----------------------------------------------------------------------------

    def switch_player(self):
        pass

    # -----------------------------------------------------------------------------

if __name__ == "__main__":
    chess = Chess()
    chess.display_field()