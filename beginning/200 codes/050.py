class MyClass:
    var = 'hi!'
    def sayHello(self):
        param1 = 'hi'
        self.param2 = 'hello'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
#obj.param1
