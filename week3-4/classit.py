class YearsAfter():
    def __init__(self,e):
        self.first = e
    def __iter__(self):
        return self
    def __next__(self):
        if self.first <= 3000:
            then = self.first
            self.first += 1
            return then
        else:
            raise StopIteration
w = int(input())
years = YearsAfter(w)
myiter = iter(years)
#print(next(myiter))
#print(next(myiter))
for q in myiter:
    print(q)
