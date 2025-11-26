class Test():
    pass
class baseclass():
    def show(self):
        return "merhaba"

def add_attribute(self):
    self.b=10
test=type("test",(baseclass,),{"a":5,"add attribute":add_attribute})

t=Test()
# sonuc=Test()
# sonuc=Test
# sonuc=type(Test)
# sonuc=type(2)
# type(int)
# sonuc=type("2")
# sonuc=type(str)
sonuc=t.show()
sonuc=t.a
t.add_attribute
print(sonuc)