import sys
from calculations import suma, power, minus, Dictionary

if __name__ == '__main__':
    x, sign, y = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    f = Dictionary[sign]
    f(x, y)
