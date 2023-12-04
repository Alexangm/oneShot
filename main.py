from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from login import Login
from signup import Signup
from mydatabase import Database
from home import Home
from palavra import Palavra
from perfil import Perfil
from quiz import Quiz
from album import Album
from kivy.uix.dropdown import DropDown
from edit import Edit


#Window.size = (480, 800)
#Window.size = (480, 912)
Window.softinput_mode="below_target"
print('Tamanho da tela', Window.size)

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            Database.ConnectDatabase()
        except Exception as e:
            print('aqui fora')
            print(e)

        home = Home()
        login = Login()
        signup = Signup()
        palavra = Palavra()
        perfil = Perfil()
        quiz = Quiz()
        album = Album()
        edit = Edit()
        self.add_widget(login)
        self.add_widget(signup)
        self.add_widget(home)
        self.add_widget(palavra)
        self.add_widget(perfil)
        self.add_widget(quiz)
        self.add_widget(album)
        self.add_widget(edit)


class DropdownMenu(DropDown):
    def changeTo(self, where):
        English.dropdown.dismiss()
        App.get_running_app().root.transition.direction = 'left'
        App.get_running_app().root.current= where
    


class English(App):  # mesmo nome que o .kv
    dropdown = None
    def show_menu(self, id):
        English.dropdown = DropdownMenu()
        English.dropdown.open(id)




English().run()
#Database.ConnectDatabase()
#print(Database.selectWord(9))
#print(Database.selectPalavraPortugues(15))
#resultado = Database.selectLearnHere(4)
#print(resultado)
#print(Database.isFav(4, 212))

# palavraQuiz > idUser word is_acerto

#with open('chatgpt-palavras.txt', 'r', encoding='utf-8') as arquivo_entrada:
#    linhas = arquivo_entrada.readlines()
#i=0
#for linha in linhas:
#    i = i+1
#    print("Palavra", linha[:-1], i, "atualizada!")
#    Database.updateWord(i, linha[:-1])
