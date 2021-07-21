from humans import Developer, Tester, ScrumMaster


def createHuman():
    name = input('📝 ¿Como se llama?: ')
    lastname = input('📝 ¿Y el apellido?: ')
    age = input('📝 ¿Cuantos años tiene?: ')

    print('\n🧑‍💻 ¡Ahora, a elegir un rol en IT!')
    print('1) Desarrollador')
    print('2) QA Tester')
    print('3) Scrum Master')
    role = input('\n📝 Ingresa el número de la opción elegida: ')

    if role in ('1', '2', '3'):
        if role == '1':
            language = input('\n🛠 En que lenguaje desarrolla: ')
            return Developer(name, lastname, age, language)
        if role == '2':
            tool = input('\n🛠 Con que herramienta testea: ')
            return Tester(name, lastname, age, tool)
        if role == '3':
            methodology = input('\n🛠 Cual es su metodología agile preferida: ')
            return ScrumMaster(name, lastname, age, methodology)


def init():
    print('🙇 ¡Creemos un humano! \n')
    newHuman = createHuman()
    message = input('\n\n📯 Genial, ahora ingresa un saludo personalizado: ')

    print('\n----------------------------------------------------')
    newHuman.sayHello(message)
    print('----------------------------------------------------\n')

    saySomething = input('\n🗣 Quieres que diga algo mas? S / [N]: ')

    while(saySomething == 'S'):
        message = input('\n📝 Ingresa un mensaje: ')
        print('\n----------------------------------------------------')
        newHuman.saySomething(message)
        print('----------------------------------------------------\n')
        saySomething = input('\n🗣 Quieres que diga algo mas? S / [N]: ')
        

    print('\n----------------------------------------------------')
    print('----------------------------------------------------\n')

    print('🏁🏁🏁 ¡Hemos finalizado! 🏁🏁🏁\n')
    print('📋 El nuevo humano se llama', newHuman.name, 'su apellido es',
          newHuman.lastname, 'y tiene', newHuman.age, 'años de edad.\n')

    currentType = type(newHuman).__name__
    
    if(Developer.__name__ == currentType):
        newHuman.sayYourLanguage()
    if(Tester.__name__ == currentType):
        newHuman.sayYourTool()
    if(ScrumMaster.__name__ == currentType):
        newHuman.sayYourMethodology()
    print('\n----------------------------------------------------')
    print('----------------------------------------------------\n')
    

init()
