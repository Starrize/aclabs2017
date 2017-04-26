class Fibonacci(object):
    def __init__(self,max):
        self.max = max
        self.x1=1
        self.x2=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.x1 > self.max):
            raise StopIteration()
        temp = self.x1 + self.x2
        self.x2 = self.x1
        self.x1 = temp
        return self.x2
        #self.x1, self.x2 = self.x1 + self.x2, self.x1