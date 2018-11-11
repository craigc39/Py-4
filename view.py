import sys, pygame, model, constant

class py4view:

    #Takes in a board that represents the model.
    def __init__(self, board):
        #Represents the board / model
        self.__model = board
        

    def run_game(self):
        pygame.init()
        pygame.font.init()
        myfont = pygame.font.SysFont('Times New Roman', 30)
        screen = pygame.display.set_mode(constant.SIZE)
        while self.__model.game_playing():
            eventgo = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.__model.add_piece(0)
                        eventgo = True
                    if event.key == pygame.K_2:
                        self.__model.add_piece(1)
                        eventgo = True
                    if event.key == pygame.K_3:
                        self.__model.add_piece(2)
                        eventgo = True
                    if event.key == pygame.K_4:
                        self.__model.add_piece(3)
                        eventgo = True
                    if event.key == pygame.K_5:
                        self.__model.add_piece(4)
                        eventgo = True
                    if event.key == pygame.K_6:
                        self.__model.add_piece(5)
                        eventgo = True
                    if event.key == pygame.K_7:
                        self.__model.add_piece(6)
                        eventgo = True
            #update view whenever a piece is added before checking for win!, will need to fix model for this
            if eventgo:
                screen.fill(constant.BLACK)
                for column in self.__model.get_board():
                    for box in column:
                        if box.get_type() == constant.CHIPTYPE.player1:
                            pygame.draw.rect(screen, constant.RED, [box.get_x() * constant.BLOCKSIZE, box.get_y() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE])
                        elif box.get_type() == constant.CHIPTYPE.player2:
                            pygame.draw.rect(screen, constant.YELLOW, [box.get_x() * constant.BLOCKSIZE, box.get_y() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE])
                        pygame.draw.rect(screen, constant.BLUE, [box.get_x() * constant.BLOCKSIZE, box.get_y() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE], 2)
                if self.__model.get_turn() == constant.TURN.player1:
                    textsurface = myfont.render("Turn: Player 1", False, constant.RED)
                else:
                    textsurface = myfont.render("Turn: Player 2", False, constant.YELLOW)
                screen.blit(textsurface,(0,constant.SIZEY * constant.BLOCKSIZE))
                pygame.display.flip()
                eventgo = False
                if not self.__model.game_playing():
                    exit()

