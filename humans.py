class Human:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def sayHello(self, message):
        print('👋', self.name, 'saluda diciendo: ', message)
    
    def saySomething(self, message):
        print('😃', self.name, 'dice:', message)


class Developer(Human):
    def __init__(self, name, lastname, age, language):
        super().__init__(name, lastname, age)
        self.language = language

    def sayYourLanguage(self):
        print('🤓', self.name, 'desarrolla en:', self.language)


class Tester(Human):
    def __init__(self, name, lastname, age, tool):
        super().__init__(name, lastname, age)
        self.tool = tool

    def sayYourTool(self):
        print('🤓', self.name, 'es especialista en testear con:', self.tool)


class ScrumMaster(Human):
    def __init__(self, name, lastname, age, methodology):
        super().__init__(name, lastname, age)
        self.methodology = methodology

    def sayYourMethodology(self):
        print('🤓', self.name, 'se especializa en la metodología agile:', self.methodology)
