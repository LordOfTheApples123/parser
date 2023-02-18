class Parser:
    text: str
    pos: int

    def __init__(self, text):
        self.text = text + '$'
        self.pos = 0

    @property
    def curr(self) -> str:
        return self.text[self.pos]

    def start(self) -> float:
        return self.expr()

    def expr(self) -> float:
        res = self.add()
        print(str(res))
        return res

    def add(self) -> float:
        res = self.mult()

        while (self.curr == '+') | (self.curr == '-'):
            if self.curr == '+':
                self.pos += 1
                res += self.mult()
            elif self.curr == "-":
                self.pos += 1
                res -= self.mult()
        return res

    def num(self) -> float:
        res = self.curr
        self.pos += 1
        while self.curr.isdigit():
            res += self.curr
            self.pos += 1
        return float(res)

    def mult(self) -> float:
        res = self.group()
        while (self.curr == '*') | (self.curr == '/'):
            if self.curr == '*':
                self.pos += 1
                res *= self.group()
            elif self.curr == '/':
                self.pos += 1
                res /= self.group()
        return res

    def group(self) -> float:
        if self.curr == '(':
            self.pos += 1
            res = self.expr()
            self.pos += 1
        else:
            res = self.num()

        return float(res)
