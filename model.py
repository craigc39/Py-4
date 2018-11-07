import constant, GridBox

#The model which represents the Connect4 Board. Stores the chips and boxes and whether the game is still going.
class Board:

    def __init__(self):
        #Represented as a list of lists of GridBoxes. Each list represents a column for the board from left to right.
        self.__boardGridBoxes = []
        #True if game is playing, False if not.
        self.__playing = False
        #Turn
        self.__turn = constant.TURN.neither
        

    #maybe add a start game which resets the game instead of init?
    def start_game(self):
        #GENERATE GRID BOXES HERE BASED ON SIZE OF BOARD
        tempBoxes = []
        for i in range(0, constant.SIZEX):
            tempColumnIn = []
            for j in range(0, constant.SIZEY):
                tempColumnIn += [GridBox.GridBox(i, j)]
            tempColumn = [tempColumnIn]
            tempBoxes += tempColumn
        self.__boardGridBoxes = tempBoxes
        self.__playing = True
        self.__turn = constant.TURN.player1
        
    #Returns a List of GridBox's for the board to fill.
    def get_board(self):
        return self.__boardGridBoxes

    #Adds a chip based on player turn at the column specified in column (0 to SIZEX - 1).
    def add_piece(self, column):
        #Check that it is a player turn
        if self.__turn == constant.TURN.neither:
            raise ValueError("Game must be started to place a chip!")
        
        #Check that a valid column was entered
        if column < 0 or column > constant.SIZEX - 1:
            raise ValueError("Incorrect column value entered when adding a chip!")

        #ADD PIECE!
        columnAdd = self.__boardGridBoxes[column]

        #Turn can't be neither, set correct player for placing chip
        if self.__turn == constant.TURN.player1:
            player = 1
        else:
            player = 2

        for i in range(constant.SIZEY - 1, -1, -1):
            if i == 0 and columnAdd[i].get_type() != constant.CHIPTYPE.none:
                print("You can't add here!")
                #Play turn again!
                break;
            elif columnAdd[i].get_type() == constant.CHIPTYPE.none:
                columnAdd[i].update_chip(player)
                self.advance_turn()
                break
        

    def advance_turn(self):
        if self.__turn == constant.TURN.neither:
            print("Game must be started!")
        elif self.__turn == constant.TURN.player1:
            self.__turn = constant.TURN.player2
        else:
            self.__turn = constant.TURN.player1

    def game_playing(self):
        return self.__playing

    #Checks if a certain player has won
    def check_for_win(self):
        #Print out winner, end game
        print("Player 1 wins!")
        self.__playing = False
