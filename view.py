import sys, pygame, model, constant

class py4view:

    #Takes in a board that represents the model.
    def __init__(self, board):
        #Represents the board / model
        self.__model = board
        

    def runGame(self):
        while 1:
            pygame.init()
            pygame.font.init()
            screen = pygame.display.set_mode(constant.SIZE)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.__model.AddPiece(0)
                    if event.key == pygame.K_1:
                        self.__model.AddPiece(1)
                    if event.key == pygame.K_2:
                        self.__model.AddPiece(2)
                    if event.key == pygame.K_3:
                        self.__model.AddPiece(3)
                    if event.key == pygame.K_4:
                        self.__model.AddPiece(4)
                    if event.key == pygame.K_5:
                        self.__model.AddPiece(5)
                    if event.key == pygame.K_6:
                        self.__model.AddPiece(6)
    
            for column in self.__model.getBoard():
                for box in column:
                    if box.getType() == constant.CHIPTYPE.none:
                        pygame.draw.rect(screen, constant.GREEN, [box.getX() * constant.BLOCKSIZE, box.getY() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE], 2)
                    elif box.getType() == constant.CHIPTYPE.player1:
                        pygame.draw.rect(screen, constant.RED, [box.getX() * constant.BLOCKSIZE, box.getY() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE])
                    elif box.getType() == constant.CHIPTYPE.player2:
                        pygame.draw.rect(screen, constant.BLUE, [box.getX() * constant.BLOCKSIZE, box.getY() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE])
                    pygame.draw.rect(screen, constant.GREEN, [box.getX() * constant.BLOCKSIZE, box.getY() * constant.BLOCKSIZE, constant.BLOCKSIZE, constant.BLOCKSIZE], 2)
            pygame.display.flip()
