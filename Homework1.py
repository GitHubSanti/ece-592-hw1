import math

def pyramid(s):
        """

        """

def findSquares(s:int = 0, e:int = 0):
        """          
        Print numbers which are exact squares of an integer within range of two integers
        """
        squares = []
        if s > e:
                for num in range(e,s+1):
                        square_root = str(math.sqrt(num)).split('.')
                        if square_root[1] == '0':
                                squares.append(num)
        elif s < e:
                for num in range(s,e+1):
                        square_root = str(math.sqrt(num)).split('.')
                        if square_root[1] == '0':
                                squares.append(num)
        else:
                        square_root = str(math.sqrt(s)).split('.')
                        if square_root[1] == '0':
                                squares.append(num)
        print(squares)
        return squares

def calSalary(hours,r):
        """

        """

def calLetterGrade(points,gradescale):
        """

        """