class Counter:
    def __init__(self,number):
        self.number=number
    def increment(self):
        self.number+=1
    def get_value(self):
        return self.number
c=Counter(10)
c.increment()
c.increment()
print(c.get_value())

class ListHolder:
    def __init__(self,lst):
        self.lst=lst
    def add_item(self,item):
        self.lst.append(item)
    def reset(self):
        self.lst=0
list=[1,2,3]
obj=ListHolder(list)
print(obj.add_item(99))
obj.reset()
print(list)

        