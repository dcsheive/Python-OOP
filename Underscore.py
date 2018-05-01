class Underscore:
    def map(self, arr, function):
        for i in range(0,len(arr)):
            arr[i] = function(arr[i])
        return arr

    def reduce(self, arr, function):
        sum = 0
        for i in range(0,len(arr)):
            sum+= function(arr[i])
        return sum

    def find(self, arr, function):
        for i in range(0,len(arr)):
            if function(arr[i]):
                return arr[i]
        return False

    def filter(self, arr, function):
        newList= []
        for i in range(0,len(arr)):
            if function(arr[i]):
                newList.append(arr[i])
        if newList:
            return newList
        else:
            return False

    def reject(self, arr, function):
        newList = []
        for i in range(0, len(arr)):
            if not function(arr[i]):
                newList.append(arr[i])
        if newList:
            return newList
        else:
            return False
_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
print(_.filter([1, 33, 5, 6, 992], lambda x: x % 3 == 0))
print(_.map([1, 2, 3], lambda x: x * 3))
print(_.reduce([1, 23, 4, 5], lambda x: x * 2))
print(_.find([1, 33, 5, 5, 993], lambda x: x % 3 == 0))
print(_.reject([1, 33, 5, 6, 992], lambda x: x % 3 == 0))
print(_.filter([1,2,3,455,68,91,-2],lambda x: x%3==0))
print(_.filter([1,2,3,455,68,91,-2],lambda x: x>2))
print(_.filter([1,2,3,455,68,91,-2],lambda x: x<0))
print(_.filter([1,2,3,455,68,91,-2],lambda x: x!=1))


