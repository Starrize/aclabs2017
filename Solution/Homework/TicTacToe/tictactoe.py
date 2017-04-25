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
    def copy(self):
        copia = State()
        copia.board = self.board.copy()
        return copia
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
    def _line_uniqueX(self,line):
        symbols = {self.board[point] for point in line}
        return symbols == {'X'}
    def all_in_a_rowX(self):
        lines = self._get_lines()
        return any(
            self._line_uniqueX(line)
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
    def smart_choose(self,state,symbol):
        return state.AImove(symbol)
class TicTacToeSmartAI():
    def _AImove_X(self,symbol,state):
        if self._winning_move(symbol,state) != None:
            return self._winning_move(symbol,state)
        if self._block_losing_move(symbol,state) != None:
            return self._block_losing_move(symbol,state)
        if self._opposite_corner(symbol,state) != None:
            return self._opposite_corner(symbol,state)
        if self._corner(state) != None:
            return self._corner(state)
        if self._center(state) != None:
            return self._center(state)
        if self._sides(state) != None:
            return self._sides(state)
    def _AImove_O(self,symbol,state):
        if self._winning_move(symbol,state) != None:
            return self._winning_move(symbol,state)
        if self._block_losing_move(symbol,state) != None:
            return self._block_losing_move(symbol,state)
        if self._opposite_corner(symbol,state) != None:
            return self._opposite_corner(symbol,state)
        if self._center(state) != None:
            return self._center(state)
        if self._corner(state) != None:
            return self._corner(state)
        if self._sides(state) != None:
            return self._sides(state)
    def choose(self,symbol,state):
        if symbol == Symbol.O:
            return self._AImove_O(symbol,state)
        return self._AImove_X(symbol,state)
    def _winning_move(self,symbol,state):
        for i in range(ord('a'),ord('c')+1):
            for j in range(ord('1'),ord('3')+1):
                point = Point.from_ag(chr(i)+chr(j))
                temp_board = state.copy()
                if temp_board.is_available(point):
                    temp_board.place(point,symbol)
                    if symbol == Symbol.X and temp_board.all_in_a_rowX():
                        return point
                    elif symbol == Symbol.O and temp_board.all_in_a_row():
                        return point
                
                    temp_board = state.copy()
        return None

    def _block_losing_move(self,symbol,state):
        opSymbol = Symbol.X
        if opSymbol == symbol:
            opSymbol = Symbol.O
        return self._winning_move(opSymbol,state)

    def _opposite_corner(self,symbol,state):
        punct1 = Point.from_ag('a1')
        punct2 = Point.from_ag('c3')
        if state.board[punct1] == symbol and state.board[punct2] == Symbol.EMPTY:
            return punct2
        elif state.board[punct1] == Symbol.EMPTY and state.board[punct2] == symbol:
            return punct1

        punct1 = Point.from_ag('a3')
        punct2 = Point.from_ag('c1')
        if state.board[punct1] == symbol and state.board[punct2] == Symbol.EMPTY:
            return punct2
        elif state.board[punct1] == Symbol.EMPTY and state.board[punct2] == symbol:
            return punct1

        return None

    def _corner(self,state):
        for i in ['a','c']:
            for j in ['1','3']:
                punct = Point.from_ag(i+j)
                if state.is_available(punct) == True:
                    return punct
        return None

    def _sides(self,state):
        punct = Point.from_ag('a2')
        if state.is_available(punct):
            return punct
        punct = Point.from_ag('b1')
        if state.is_available(punct):
           return punct
        punct = Point.from_ag('b3')
        if state.is_available(punct):
            return punct
        punct = Point.from_ag('c2')
        if state.is_available(punct):
            return punct
        return None

    def _center(self,state):
        punct = Point.from_ag('b2')
        if state.is_available(punct) == True:
            return punct
        return None
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

    def vsAI_X(self):
        aiSymbol = Symbol.X
        if self.symbol == aiSymbol:
            aiSymbol = Symbol.O
        self.state.place(TicTacToeSmartAI().choose(aiSymbol,self.state), aiSymbol)
        self.presentation.draw(self.state)
        for point in self.moves():
            self.state.place(point, self.symbol)
            self.presentation.draw(self.state)
            if self.done():
                break
            self.state.place(TicTacToeSmartAI().choose(aiSymbol,self.state), aiSymbol)
            self.presentation.draw(self.state)
            if self.done():
                break
    def vsAI_O(self):
        self.presentation.draw(self.state)
        aiSymbol = Symbol.X
        if self.symbol == aiSymbol:
            aiSymbol = Symbol.O
        for point in self.moves():
            self.state.place(point, self.symbol)
            self.presentation.draw(self.state)
            if self.done():	
                break
            self.state.place(TicTacToeSmartAI().choose(aiSymbol,self.state), aiSymbol)
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
        elif self.opponent == '2' and self.symbol == 'X':
            self.vsAI_O()
        else:
            self.vsAI_X()

if __name__ == '__main__':
    Game().run()