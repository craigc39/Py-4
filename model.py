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

    #returns the turn
    def get_turn(self):
        return self.__turn

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
            chiptype = constant.CHIPTYPE.player1
        else:
            player = 2
            chiptype = constant.CHIPTYPE.player2

        for i in range(constant.SIZEY - 1, -1, -1):
            if i == 0 and columnAdd[i].get_type() != constant.CHIPTYPE.none:
                print("You can't add here!")
                #Play turn again!
                break;
            elif columnAdd[i].get_type() == constant.CHIPTYPE.none:
                columnAdd[i].update_chip(player)
                self.check_for_win(column, i, chiptype)
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

    #Checks if a certain player has won after adding chip at position x, y
    def check_for_win(self, x, y, player):
        #Print out winner, end game
        
        #check the diagonal up right
        tempscorediagonalupright = 1
        for i in range(1, 4):
            if x-i >= 0 and y+i < constant.SIZEY:
                if self.__boardGridBoxes[x-i][y+i].is_type(player):
                    tempscorediagonalupright += 1
                else:
                    break

        for i in range(1, 4):
            if x+i < constant.SIZEX and y-i >=0:
                if self.__boardGridBoxes[x+i][y-i].is_type(player):
                    tempscorediagonalupright += 1
                else:
                    break
        
        if tempscorediagonalupright >= 4:
            #fix with correct player
            print("Player X wins!")
            self.__playing = False

        #check the diagonal down right
        tempscorediagonaldownright = 1
        for i in range(1, 4):
            if x-i >= 0 and y-i >= 0:
                if self.__boardGridBoxes[x-i][y-i].is_type(player):
                    tempscorediagonaldownright += 1
                else:
                    break

        for i in range(1, 4):
            if x+i < constant.SIZEX and y+i < constant.SIZEY:
                if self.__boardGridBoxes[x+i][y+i].is_type(player):
                    tempscorediagonaldownright += 1
                else:
                    break
        
        if tempscorediagonaldownright >= 4:
            #fix with correct player
            print("Player X wins!")
            self.__playing = False

        #check the left to right
        tempscorediagonalleftright = 1
        for i in range(1, 4):
            if x-i >= 0:
                if self.__boardGridBoxes[x-i][y].is_type(player):
                    tempscorediagonalleftright += 1
                else:
                    break

        for i in range(1, 4):
            if x+i < constant.SIZEX:
                if self.__boardGridBoxes[x+i][y].is_type(player):
                    tempscorediagonalleftright += 1
                else:
                    break
        
        if tempscorediagonalleftright >= 4:
            #fix with correct player
            print("Player X wins!")
            self.__playing = False

        #check the up to down
        tempscorediagonalupdown = 1
        for i in range(1, 4):
            if y-i >= 0:
                if self.__boardGridBoxes[x][y-i].is_type(player):
                    tempscorediagonalupdown += 1
                else:
                    break

        for i in range(1, 4):
            if y+i < constant.SIZEY:
                if self.__boardGridBoxes[x][y+i].is_type(player):
                    tempscorediagonalupdown += 1
                else:
                    break
        
        if tempscorediagonalupdown >= 4:
            #fix with correct player
            print("Player X wins!")
            self.__playing = False
