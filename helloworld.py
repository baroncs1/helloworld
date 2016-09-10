class HelloWorld:
    def __init__(self,name):
        self.name=name
        self.number=1
    def __add__(self,other):
        return HelloWorld(self.name+other.name)
    def getName(self):
        return self.name
        
myHelloWorld=HelloWorld('egysztring')
yourHelloWorld=HelloWorld('megegysztring')
ourHelloWorld=myHelloWorld+yourHelloWorld
