class MathDojo:
    def __init__(self):
        self.value = 0
    def add(self, *args):
        for i in args:
            if type(i) is list:
                val = 0
                for j in i:
                    val +=j
                i= val
            if type(i) is tuple:
                val = 0
                for j in i:
                    val += j
                self.value += val
                continue
            self.value += i
        return self
    def subtract(self, *args):
        for i in args:
            if type(i) is list:
                val = 0
                for j in i:
                    val += j
                i = val
            if type(i) is tuple:
                val = 0
                for j in i:
                    val += j
                self.value -= val
                continue
            self.value -= i
        return self
    def result(self):
        print(self.value)
        self.value = 0
md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
md.add((1), 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], (1.1,2.3)).result()
