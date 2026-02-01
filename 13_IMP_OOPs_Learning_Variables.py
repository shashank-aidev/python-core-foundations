class Counter:
    number_of_objects=0
    number_of_aciton_called=0

    def __init__(self,value):
        self.value=value
        Counter.number_of_objects+=1
    def Change(self):
        Counter.number_of_aciton_called+=1
        self.value = self.value + int(input("Enter the value to change : "))

    def Reset(self):
        # Counter.number_of_objects=0
        Counter.number_of_aciton_called+=1
    def show(self):
        print("Value is :",self.value,"\nActions : ",Counter.number_of_aciton_called,"\nObjects : ",Counter.number_of_objects)

info=Counter(4)
infof=Counter(6)
info.Change()
infof.Change()
# info.Reset()
# infof.Reset()
infof.show()
info.show()


