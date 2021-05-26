"""
@author Santiago Sepulveda

Following script was created with the four functions:
pyramid(s)
findSquares(s:int = 0, e:int = 0)
calSalary(hours,r)
calLetterGrade(points,gradescale)

"""
import math

def pyramid(s):
        """
        Prints a “message pyramid” for the input message string starting from the first character in the string.
        """
        pyramid = ''
        for letter in s:
                pyramid += letter
                print(pyramid)

def findSquares(s:int = 0, e:int = 0):
        """          
        Return list of squares. Print numbers which are exact squares of an integer within range of two integers. 
        s is starting integer, e is ending integer.
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
                                squares.append(s)
        print(squares)
        return squares

def calSalary(h:float,r:float = 20):
        """
        Return the salary in float. h is number of hours and r is the hourly rate.

        """
        if h < 0:
                print("Not valid Hours")
                return -1
        elif h >= 0 and h <= 40:
                salary = lambda h,r : h*r
                return salary
        else:
                salary = lambda h,r : 40*r + (h-40)*(r*1.2)
                return salary

def calLetterGrade(points,gradescale):
        """

        """