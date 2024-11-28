from time import sleep
from string import  ascii_uppercase

class Chess:
    def __init__(self, row_count: int=8, column_count:int = 8) -> None:
        
        # Maybe some day a bigger chessboard :)
        self._rows = row_count
        self._columns = column_count

        self._emptyFieldCharacter = " "
        self._allUsedLetters:list[str] = list(ascii_uppercase[0:self._rows])
        print(self._allUsedLetters)
        # self.field = [" "]*self.rows*self.columns
        self.dataField = self.generate_field(row_count, column_count)
        self.displayField = self.dataField

        self._Players = ["White", "Black"]
        self.currentPlayer = self._Players[0]
        
        self._sleepTime = 0.15 # Used to the while loop ain't running to fast

    def start_game(self):
        while True:
            self.display_field()
            self.set_piece()

    # -----------------------------------------------------------------------------

    @staticmethod
    def generate_field(rows, columns) -> list[list]:
        """
        Generates a Field by the set number of  column's and row's
        :return: list[list] For each column it generates the number of rows. Just look at the code yourself darn it
        """
        field = []
        for i in range(columns):
            column_list = []

            # Column for loop
            for x in range(rows):
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
        for character in ascii_uppercase[0:self._rows]:
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

        for column_number,column in enumerate(self.dataField):
            row_merged_text = ""

            # Get all the values of the column together to print it.
            for row in column:
                row_merged_text += row + " "

            # Merging all the text so print will only be used once.
            # ColumnNR rows ColumnNR example: ---> 1 | 0 1 2 3 4 5 6 7 | 1 <---
            result_text += f"{str(column_number + 1)} |  {row_merged_text} | {str(column_number + 1)}\n"

        print(result_text)

    # -----------------------------------------------------------------------------

    # TODO finish the get_player_choice method to filter the input and return use full info
    def get_player_choice(self):
        _blank_dict = {
            "row1": None,
            "column1": None
        }
        user_choice = _blank_dict

        while True:
            print("LoopStarted\n")
            sleep(self._sleepTime)
            _unfiltered_input = input()
            # Skip directly if there are less than 2 characters
            if len(_unfiltered_input) < 1:

                print("TriggeredSkip")
                continue

            for character in _unfiltered_input:
                # Check for the Character part of the position
                if user_choice["row1"] is None and character.upper() in self._allUsedLetters:
                    # Saving the position to use it as a row identifier
                    user_choice["row1"] = self._allUsedLetters.index(character.upper())
                    
                elif user_choice["row1"] is None and not character.isdigit() and character != " ":
                    # Character is not a letter that is used in the game ;>
                    pass
                
                # Check for the Digit part of the position
                if user_choice["column1"] is None and character.isdigit() and len(self.field) >= int(character) and not int(character)<= 0:
                    user_choice["column1"] = int(character) - 1 # subtracting 1 to make it usable in a list


            # check if all has been filled out
            print(list(user_choice.values()))
            if not None in list(user_choice.values()): # Check if any
                break
            else:
                user_choice = _blank_dict  # Resetting it since it wasn't filled out properly

        return user_choice
                    



    # -----------------------------------------------------------------------------

    # TODO write how to switch between player 1 and 2
    def switch_player(self):
        pass

    # -----------------------------------------------------------------------------

    def set_piece(self):
        choice_dict = self.get_player_choice()

        self.dataField[choice_dict["column1"]][choice_dict["row1"]] = "x"

    # -----------------------------------------------------------------------------



if __name__ == "__main__":
    chess = Chess()
    chess.start_game()