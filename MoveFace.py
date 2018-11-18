import sys,tty,termios
from os import system,name

#this is the object that will be drawn on screen
face = [' - - -','| o o |','|  =  |',' - - -']

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

class Move:
    def __init__(self):
        self.__positionx = 100 #number of spaces from left to right
        self.__positiony = 20  #numer of carriage returns
    def getPositionX(self):
        return self.__positionx
    def getPositionY(self):
        return self.__positiony
    def moveUp(self):
        self.__positiony -= 1
    def moveDown(self):
        self.__positiony += 1
    def moveRight(self):
        self.__positionx += 1
    def moveLeft(self):
        self.__positionx -= 1
    def showMeOnScreen(self, image_array):
        clear()
        print(' ' * self.__positionx)
        for y in range(0,self.__positiony):
            print('')
            if (y == self.__positiony-1):
                for index in image_array:
                    print(' ' * self.__positionx + index)

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get(this_obj):
    inkey = _Getch()
    while (1):
        k = inkey().upper()
        #if k != '': break
        #return False
        if k == 'U':
            this_obj.moveUp()
            return True
        elif k == 'D':
            this_obj.moveDown()
            return True
        elif k == 'R':
            this_obj.moveRight()
            return True
        elif k == 'L':
            this_obj.moveLeft()
            return True
        elif k == '0':
            print('\n\nThank you for using this silly program. :-)\n\n')
            return False


def main():
    obj = Move()

    #Basic instructions:
    print('\nYou can move the object up/down/left/right using the keys U/D/L/R respectively.')
    print('Press 0 (zero) at anytime to exit.')

    while (get(obj) == True):
        obj.showMeOnScreen(face)


if __name__ == '__main__':
    main()