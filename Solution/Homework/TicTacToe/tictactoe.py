"""
Simple game using MVC pattern.
"""
import collections
import sys
import random

_Point = collections.namedtuple('Point', 'horizontal,vertical')


class Point(_Point):
    @classmethod
    def from_ag(cls, notation):
        ag = notation.lower().strip()
        return cls(ord(ag[0]) - ord('a'),
                   ord(ag[1]) - ord('1'))

    @property
    def as_ag(self):
        return '{}{}'.format(chr(self.horizontal + ord('a')),
                             self.vertical + 1)


class Symbol(object):
    X = 'X'
    O = 'O'
    EMPTY = ' '


class State(object):
    def __init__(self, size=3):
        self.board = collections.defaultdict(lambda: Symbol.EMPTY)
        self.size = size

    def place(self, point, symbol):
        assert isinstance(point, Point)
        self.board[point] = symbol

    def __getitem__(self, key):
        return self.board[key]
    def is_available(self,point):
        return self.board[point.horizontal,point.vertical] == Symbol.EMPTY
    def symbols(self):
        return [symbol for point, symbol in self.items()]

    def is_full(self):
        return all([s != Symbol.EMPTY for s in self.symbols()])

    def _get_lines(self):
        horizontals = [
            [Point(h,v) for v in range(self.size)]
            for h in range(self.size)
        ]
        verticals = [
            [Point(v,h) for v in range(self.size)]
            for h in range(self.size)
        ]
        diagonals = [
            [Point(x, x) for x in range(self.size)],
            [Point(self.size - 1 - x, x) for x in range(self.size)]
        ]
        lines = horizontals + verticals + diagonals
        return lines

    def _line_unique(self, line):
        symbols = {self.board[point] for point in line}
        return symbols in ({Symbol.X}, {Symbol.O})

    def all_in_a_row(self):
        lines = self._get_lines()
        return any(
            self._line_unique(line)
            for line in lines
        )


    def items(self):
        return [(Point(h, v), self.board[(h, v)])
                for h in range(self.size)
                for v in range(self.size)]


class Presentation(object):
    def __init__(self, mode='text'):
        self.mode = mode

    def _draw(self, state):
        layout = """
  *-*-*-*
3 |{2}|{5}|{8}|
  *-*-*-*
2 |{1}|{4}|{7}|
  *-*-*-*
1 |{0}|{3}|{6}|
  *-*-*-*
   a b c
tictactoe> """
        output = layout.format(*state.symbols())
        print (output, end=' ')

    def draw(self, state, method=None):
        method = method or self._draw
        method(state)

class TicTacToeAI:
    def __init__(self):
        pass

    def choose(self,state):
        x = random.choice('abc')
        y = random.choice('123')
        point = Point.from_ag(x + y)
        while state.is_available(point) == False:
            x = random.choice('abc')
            y = random.choice('123')
            point = Point.from_ag(x + y)
        return point
class Game(object):
    def __init__(self):
        self.state = State()
        self.presentation = Presentation()
        self.symbol = Symbol.EMPTY
    def _get_move(self):
        try:
            line = sys.stdin.readline()
        except ValueError:
            print (' Move must be like, a2')
            return self._get_move()
        return Point.from_ag(line)

    def moves(self):
        while True:
            yield self._get_move()

    def done(self):
        return self.state.all_in_a_row() or self.state.is_full()
    
    def vsPlayer(self):
        self.presentation.draw(self.state)
        for point in self.moves():
            self.state.place(point, self.symbol)
            self.presentation.draw(self.state)
            if self.symbol == Symbol.X:
                self.symbol = Symbol.O
            else:
                self.symbol = Symbol.X
            if self.done():
                break
    
    def vsAI(self):
        self.presentation.draw(self.state)
        if self.symbol == Symbol.X:
            aiSymbol = Symbol.O
        else: 
            aiSymbol = Symbol.X
        for point in self.moves():
            self.state.place(point, self.symbol)
            self.presentation.draw(self.state)
            if self.done():
                break
            
            self.state.place(TicTacToeAI().choose(self.state), aiSymbol)
            self.presentation.draw(self.state)
            if self.done():
                break
			

    def run(self):
        print('1.vs Player\n2.vs AI')
        self.opponent = sys.stdin.readline().split()[0]
        print('Alegeti simbolul pe care doriti sa il folositi:')
        self.symbol = sys.stdin.readline().split()[0]
        if self.opponent == '1':
            self.vsPlayer()
        else:
            self.vsAI()

if __name__ == '__main__':
    Game().run()