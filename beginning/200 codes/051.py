class MyClass:
    def sayHello(self):
        print('hi')

    def sayBye(self, name):
        print('%s, see you again!' %name)

obj = MyClass()
obj.sayHello()
obj.sayBye('Steve')
