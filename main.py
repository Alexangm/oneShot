from kivy.app import App
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

import random

from sqlite3 import connect
from custom_widgets import QButton
from styles import Styles


class Database:
    db=None
    @staticmethod
    def ConnectDatabase():
        Database.db = connect('dbenglish.db')
        cursor =  Database.db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id_user integer PRIMARY KEY, email text NOT NULL, name text NOT NULL, password text NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS words(id_word integer PRIMARY KEY, word text NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS profile(id_user integer, id_word integer, fl_conhecia integer, fl_favorita integer, fl_sabia integer DEFAULT 0)")
        cursor.execute("CREATE TABLE IF NOT EXISTS palavrasPortugues(id_word integer PRIMARY KEY, word text NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS palavrasQuiz(id_user integer, id_word integer PRIMARY KEY, fl_acerto integer)")
        Database.db.commit()
        print('pasosu do commit')
        print("Conectado com sucesso!")

    
    @staticmethod
    def droppalavrasQuiz():
        sql = "DROP TABLE palavrasQuiz"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        print("dropado com sucesso")
        return 1


    @staticmethod
    def updateWord(id_word, word):
        sql = "UPDATE words SET word = %s where id_word = %s"
        val = (f"{word}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 1
    
    @staticmethod
    def insertdata(email, name, password):
        sql = "INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"
        val = (f"{email}", f"{name}", f"{password}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    @staticmethod
    def isValid(email):
        sql = "SELECT * FROM users WHERE email=(%s)"
        val = (f"{email}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        print("aqui o result", result)
        if(result):
            return False
        else:
            return True


    @staticmethod
    def isExist(email, password):
        sql = "SELECT * FROM users WHERE email=%s and password = %s"
        val = (f"{email}", f"{password}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            return True
        else:
            return False
        

    @staticmethod
    def insertWord(word):
        sql = "INSERT INTO words (word) VALUES (%s)"
        val = (f"{word}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    def linkWordWithProfile(id_word, id_user, fav):
        sql = "SELECT * FROM profile WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            sql = "UPDATE profile SET fl_favorita = %s where id_word = %s and id_user = %s"
            val = (f"{fav}", f"{id_word}", f"{id_user}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result true'
        else:
            sql = "INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES (%s, %s, 0, %s)"
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result false'


    @staticmethod
    def insertQuiz(id_user, id_word, fl_acerto):
        sql = "SELECT * FROM palavrasQuiz WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            return 0
        else:
            sql = "INSERT INTO palavrasQuiz (id_user, id_word, fl_acerto) VALUES (%s, %s, %s)"
            val = (f"{id_user}", f"{id_word}", f"{fl_acerto}")
            print('DENTRO DO BD = ',sql, val)
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 1


    @staticmethod
    def insertPalavraPortugues(palavra):
        sql = "INSERT INTO palavrasPortugues (word) VALUES (%s)"
        val = (f"{palavra}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    @staticmethod
    def selectPalavraPortugues(id):
        sql = f"SELECT word FROM palavrasPortugues where id_word = %s"
        val = (f"{id}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]


    # retorna a palavra pelo id
    @staticmethod
    def selectWord(id):
        sql = "SELECT word FROM words where id_word = %s"
        val = (f"{id}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()
    

    @staticmethod
    def selectWordById(id):
        sql = "SELECT word FROM words where id_word = %s"
        val = (f"{id}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]

    @staticmethod
    def selectAllWords():
        sql = "SELECT * FROM words"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    @staticmethod
    def selectAllPortugueseWords():
        sql = "SELECT * FROM palavrasPortugues"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def changeUser(id_user, name, password):
        sql = "UPDATE users SET password = %s, name = %s where id_user = %s"
        val = (f"{password}", f"{name}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 'result true'
    

    @staticmethod
    def changePassword(id_user, password):
        sql = "UPDATE users SET password = %s where id_user = %"
        val = (f"{password}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 'result true'


    @staticmethod
    def changeName(id_user, name):
        sql = "UPDATE users SET name = %s where id_user = %s"
        val = (f"{name}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 'result true'


    @staticmethod
    def selectIdFromWord(word):
        sql = "SELECT id_word FROM words WHERE word=%s"
        val = (f"{word}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectNameById(id_user):
        sql = "SELECT name FROM users WHERE id_user=%s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]

    #retorna id pelo email
    @staticmethod
    def selectIdFromEmail(email):
        sql = "SELECT id_user FROM users WHERE email=%s"
        val = (f"{email}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectNameFromEmail(email):
        sql = "SELECT name FROM users WHERE email=%s"
        val = (f"{email}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectPasswordFromId(id_user):
        sql = "SELECT password FROM users WHERE id_user=%s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]

    
    @staticmethod
    def linkWordWithProfile(id_word, id_user, fav):
        sql = "SELECT * FROM profile WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            sql = "UPDATE profile SET fl_favorita = %s where id_word = %s and id_user = %s"
            val = (f"{fav}", f"{id_word}", f"{id_user}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result true'
        else:
            sql = "INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES (%s, %s, 0, %s)"
            val = (f"{id_user}", f"{id_word}", f"{fav}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result false'
        
    @staticmethod
    def linkWWP(id_word, id_user):
        sql = "SELECT * FROM profile WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        print("até aqui vai")
        if(result):
            return print('conexao existente')
        else:
            sql = "INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES (%s, %s, 0, 0)"
            val = (f"{id_user}", f"{id_word}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return print('conexao criada')


    @staticmethod
    def isFav(id_user, id_word):
        sql = "SELECT fl_favorita FROM profile WHERE (id_user=%s) AND (id_word = %s)"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if (result):
            Database.db.commit()
            return result[0][0]
        else:
            Database.db.commit()
            return -1

    @staticmethod
    def selectFavs(id_user):
        sql = "SELECT count(*) FROM profile where fl_favorita = '1' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectFavsWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_favorita = '1' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        

    @staticmethod
    def selectKnew(id_user):
        sql = "SELECT count(*) FROM profile where fl_conhecia = '1' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectKnewWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_conhecia = '1' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectConheciAqui(id_user):
        sql = f"SELECT count(*) FROM profile where fl_conhecia = '0' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectConheciAquiWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_conhecia = '0' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectSabia(id_user):
        sql = "SELECT count(*) FROM profile where fl_sabia = '1' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectSabiaWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_sabia = '1' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0

    @staticmethod
    def selectLearnHere(id_user):
        sql = "SELECT count(*) FROM profile where fl_sabia = 0 AND fl_conhecia = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectLearnHereWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_sabia = 0 AND fl_conhecia = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectQuizAcertos(id_user):
        sql = "SELECT count(*) FROM palavrasQuiz where fl_acerto = 1 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    
    @staticmethod
    def selectQuizErros(id_user):
        sql = "SELECT count(*) FROM palavrasQuiz where fl_acerto = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectQuizAcertoWords(id_user):
        sql = "SELECT w.word FROM palavrasQuiz p inner join words w on p.id_word = w.id_word where fl_acerto = 1 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0


    @staticmethod
    def selectQuizErroWords(id_user):
        sql = "SELECT w.word FROM palavrasQuiz p inner join words w on p.id_word = w.id_word where fl_acerto = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0

        

    @staticmethod
    def updateProfile(id_word, id_user, conhecia, sabia):
        sql = "UPDATE profile SET fl_conhecia = %s, fl_sabia = %s where id_word = %s and id_user = %s"
        val = (f"{conhecia}", f"{sabia}", f"{id_word}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 1
    

    @staticmethod
    def deleteUser(id_user):
        sql = "DELETE FROM profile WHERE id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        sql = "DELETE FROM users WHERE id_user = %s"
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 1


    @staticmethod
    def selectWordKnoledge(id_user, id_word):
        sql = "SELECT fl_conhecia, fl_sabia FROM profile where id_user = %s AND id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result[0][0] and result[0][1]:
            return 1
        if result[0][0] and not result[0][1]:
            return 2
        if not result[0][0] and not result[0][1]:
            return 3


#UTILS
def Draw():
    seed_day = 20231204
    random.seed(seed_day)
    return sorted(random.sample(range(531), 8))


def DrawQuiz():
    seed_yesterday = 20231204
    random.seed(seed_yesterday)
    numeros = sorted(random.sample(range(566), 8))
    return [numeros[0], numeros[1], numeros[3], numeros[5], numeros[7]]


def DrawQuizOptions():
    seed_yesterday = 20231204
    random.seed(seed_yesterday)
    lista = random.sample(range(423), 15)
    return lista


def API_request(word):
    #url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    #response = requests.get(url + word)
    #if response.status_code == 200:
    #api_dados = response.json()
    dados = {}
    #dado = api_dados[0]
    dados["word"] = 'palavra'
    dados["audios"] = 'audio'
    dados["definitions"] = 'definicao'
    dados["synonyms"] = 'sinonimo'
    dados["antonyms"] = 'antonimo'
    dados["definitions"] = {'definition':'oasioas', }
    dados["traducao"] = 'traducao'      
    dados["portugues"] = 'significado em portugues'
    return dados

def spans(word):
    dicionario = ['muito siginficiado foda', word]
    return dicionario


def remover_acentos_manual(palavra):
    mapa_acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ã': 'a', 'õ': 'o',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ç': 'c',
    }
    palavra_sem_acentos = ''.join(mapa_acentos.get(char, char) for char in palavra)
    return palavra_sem_acentos

    
def traduzir_com_linguee(word):
    return word + 'traduzidinha'
    

def API_audio(word):
    raudio = -1
    return raudio


#EDIT
Builder.load_string("""
#: import CTextInput custom_widgets
#: import CButton custom_widgets
<Edit>:
    name: 'edit'
    canvas.before:
        Color:
            rgba: 0.3, 0.45, 0.7, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        BoxLayout:
            size_hint: 1.0, 0.04
        BoxLayout:
            size_hint: 1, 0.34
            Image:
                source: 'logo.png'
        BoxLayout:
            size_hint: 1, 0.07
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: 'top'           
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                spacing: dp(10)
                height: self.minimum_height
                padding: [dp(30), 0, dp(30), 0] 
                Label:
                    id: email
                    font_size: '22sp'
                    size_hint_y: None
                    color: 1, 1, 1, 1   
                    halign: 'center'
                    text_size: self.size 
                    font_name: 'robotoblack.ttf'
                    size: self.texture_size
                CTextInput:
                    id: nome
                    hint_text: "nome"
                    text: ''
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                CTextInput:
                    id: senhaAtual
                    hint_text: 'senha atual'
                    max_length: 25
                    size_hint_y: None
                    password: True
                    height: dp(50)
                    multiline: False
                    on_text: root.name_check(self)
                CTextInput:
                    id: novaSenha
                    hint_text: 'nova senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                CTextInput:
                    id: cNovaSenha
                    hint_text: 'confirmar nova senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                EdButton:
                    text: 'Salvar'
                    background_color: root.blue
                    on_press: root.editData()
                    size_hint_y: None
                    height: dp(50)
                EdButton:
                    text: 'Cancelar'
                    on_press: root.switchToPerfil()
                    background_color: root.edit_color
                    size_hint_y: None
                    height: dp(50)
                EdButton:
                    text: 'Deletar conta'
                    on_press: root.delete()
                    background_color: root.delete_color
                    size_hint_y: None
                    height: dp(50)
                Label:
                    id: msgErro
                    text: ''
                    color: 0.3, 0, 0, 1   
                    haling: 'left'
                    text_size: self.size 
                    font_name: 'robotolight.ttf'

<Popup>:
    title: 'Tem certeza que deseja apagar a conta?'
    title_align: 'center'
    title_size: '28sp'
    size_hint: 0.8, 0.38
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: 0.7
            orientation: 'vertical'
            Label:
                id: confirm
                text: 'Confirme sua senha:'
                color: 1, 1, 1, 1   
                haling: 'left'
                font_size: '20sp'
                font_name: 'robotolight.ttf'
            CTextInput:
                id: confirmPassword
                hint_text: 'senha'
                max_length: 25
                size_hint_y: None
                height: dp(50)
                multiline: False
                password: True  
            Label:
                id: msgPop
                text: ''
                color: 0.9, 0.9, 0.9, 1   
                haling: 'left'
                font_size: '16sp'
                font_name: 'robotolight.ttf'                 
        BoxLayout:
            size_hint_y: 0.3
            orientation: 'horizontal'
            Button:
                text: 'Não'
                on_press: root.dismiss()
                font_size: '18sp'
                size_hint: 0.5, 0.7
            Button:
                text: 'Sim'
                font_size: '18sp'
                on_press: root.deleteAcc()
                size_hint: 0.5, 0.7           
""")


class popup(Popup):
    tela = ''
    delete_color = Styles.delete_red_color
    idUser = ''
    def deleteAcc(self):
        popup.idUser = Edit.idUser
        if(self.ids.confirmPassword.text == Database.selectPasswordFromId(popup.idUser)):
            Database.deleteUser(popup.idUser)
            self.dismiss()
            popup.tela.manager.current = 'login'
        else:
            self.ids.msgPop.text = 'Senha incorreta.'
            

class Edit(Screen):
    delete_color = Styles.delete_red_color
    edit_color = Styles.edit_color
    blue = Styles.primary_color
    idUser = ''
    password = ''
    def on_pre_enter(self, *args):
        Edit.idUser = Perfil.id
        self.ids.email.text = Perfil.email
        self.ids.nome.text = Perfil.nome
        self.ids.senhaAtual.text = ''
        self.ids.novaSenha.text = ''
        self.ids.cNovaSenha.text = ''


    def name_check(self, text_input):
        if(len(text_input.text) > 25):
            text_input.text = text_input.text[:-1]


    def space_check(self, text_input):
        text_input.text = text_input.text.replace(" ", "")


    def switchToPerfil(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Perfil'


    def delete(self):
        popup.tela = self
        popup().open()

    
    def editData(self):
        nome = self.ids.nome.text
        senhaAtual = self.ids.senhaAtual.text
        novaSenha = self.ids.novaSenha.text
        cNovaSenha = self.ids.cNovaSenha.text
        if novaSenha or cNovaSenha:
            if senhaAtual == Database.selectPasswordFromId(Edit.idUser):
                if novaSenha == cNovaSenha:
                    if len(novaSenha) > 7:
                        if nome:
                            Database.changeUser(Edit.idUser, nome, novaSenha)
                            self.manager.transition.direction = 'left'
                            self.manager.current = 'Perfil'
                        else:
                            Database.changePassword(Edit.idUser, novaSenha)
                            self.manager.transition.direction = 'left'
                            self.manager.current = 'Perfil'
                    else:
                        self.ids.msgErro.text = 'Nova senha deve ter pelo menos 8 caracteres.'
                else:
                    self.ids.msgErro.text = 'Senhas não coincidem!'
            else:
                self.ids.msgErro.text = 'Senha incorreta!'
        elif nome:
            if senhaAtual == Database.selectPasswordFromId(Edit.idUser):
                Database.changeName(Edit.idUser, nome)
                self.manager.transition.direction = 'left'
                self.manager.current = 'Perfil'
            else:
                self.ids.msgErro.text = 'Senha incorreta!'
        else:
            self.ids.msgErro.text = 'Informações incompletas!'


# ALBUM
Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Album>:
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size       
    name: 'Album'
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout: 
                size_hint_y: 0.105
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'left'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: (self.pos[0]+dp(12), self.pos[1])
                                size: self.size
                                source: 'DL.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    id: titulo
                    text: 'Quiz'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    font_size: '40sp'
                    size_hint: 1.0, 1.0
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'right'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: self.pos
                                size: self.size
                                source: 'menu.png'
                        id: menu
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: app.show_menu(menu)
            BoxLayout: 
                size_hint_y: 0.02 
            BoxLayout: 
                size_hint_y: 0.775
                BoxLayout:
                    orientation: 'horizontal'
                    BoxLayout: 
                        size_hint_x: 0.05 
                    ScrollView:
                        do_scroll_y: True
                        h_align: 'center'
                        bar_width: 0
                        size_hint: 0.9, 1
                        GridLayout:
                            spacing: dp(20)
                            id: role
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                    BoxLayout: 
                        size_hint_x: 0.05 
                        
            BoxLayout: 
                size_hint_y: 0.1    
""")


class Album(Screen):
    bg_color = Styles.primary_color
    div = Styles.primary_fundo
    divT = Styles.primary_fundo
    meaning = Styles.meaning_color
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo
    word_list = None
    botoes_list = []


    def on_pre_enter(self, *args):
        self.ids.titulo.text = Perfil.titulo
        if Album.word_list != 0:
            for btn in Album.botoes_list:
                self.ids.role.remove_widget(btn)
        if (Perfil.palavras) != 0:
            Album.word_list = sorted(Perfil.palavras)
            for i in range(len(Album.word_list)):
                self.generate(Album.word_list[i])
                

    def generate(self, palavra):
        btn = QButton(text=palavra)
        btn.bind(on_press=lambda instance: Album.switchToPalavra(self, palavra))
        Album.botoes_list.append(btn)
        self.ids.role.add_widget(btn)

    
    def switchToPalavra(self,palavra):
        Home.word = palavra
        Home.id_word = Database.selectIdFromWord(Home.word.lower())
        print(Home.word.lower())
        dados = API_request(Home.word.lower())
        Home.audio = dados['audios']
        Home.significado_en = dados['definitions']
        Home.traducao = dados['traducao']
        Home.significado_pt = dados['portugues']
        self.manager.transition.direction = 'left'
        self.manager.current = 'Palavra'
        
        
    def goToMenu(self):
        self.manager.current = 'Home'
        self.manager.transition.direction = 'right'


# QUIZ
Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Quiz>:
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size       
    name: 'Quiz'
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout: 
                size_hint_y: 0.105
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'left'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: (self.pos[0]+dp(12), self.pos[1])
                                size: self.size
                                source: 'dl.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    id: titulo
                    text: 'Quiz'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    font_size: '40sp'
                    size_hint: 1.0, 1.0
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'right'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: self.pos
                                size: self.size
                                source: 'menu.png'
                        id: menu
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: app.show_menu(menu)
            BoxLayout:
                size_hint_y: 0.895
                canvas.before:
                    Color:
                        rgba: root.div
                    RoundedRectangle:
                        pos: (root.x*0.015, root.y*0.74)
                        size: (root.x * 0.57, root.y*0.60)
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: 0.040   
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.032
                    BoxLayout:
                        orientantion: 'horizontal'
                        Label:
                            id: titulo
                            text: '            Qual a tradução de:'
                            halign: 'center'
                            valign: 'center'
                            font_name: 'robotomedium.ttf'
                            font_size: '28sp'
                            size_hint: 1.0, 1.0
                        Label:
                            id: score
                            text: '4/5'
                            halign: 'right'
                            valign: 'top'
                            font_name: 'robotomedium.ttf'
                            font_size: '22sp'
                            size_hint: 0.2, 1.0
                BoxLayout:
                    size_hint_y: 0.030  
                BoxLayout:
                    size_hint_y: 0.042
                    Label:
                        id: palavra
                        text: 'Amiable'
                        halign: 'center'
                        valign: 'center'
                        font_name: 'robotomedium.ttf'
                        font_size: '50sp'
                        size_hint: 1.0, 1.0
                BoxLayout:
                    size_hint_y: 0.18
                    canvas.before:
                        Color:
                            id: bola
                            rgba: (1,1,1,root.ellipse_opacity)
                        Ellipse:
                            pos: (root.x*0.075, root.y*0.42)
                            size: (root.x * 0.45, root.y*0.20)
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.15
                    size: self.minimum_size
                    padding: [dp(40),dp(-90)]
                    canvas.before:
                        Color:
                            rgba: root.meaning
                        Rectangle:
                            pos: (root.x*0.03, root.y*0.76)
                            size: (root.x * 0.54, root.y*0.35)
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o0
                                on_active: root.funcaoOpcao(self, 0)
                                group: 'grupo1'
                                width: dp(50)
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l0
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Corredor'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o1
                                on_active: root.funcaoOpcao(self, 1)
                                group: 'grupo1'
                                width: dp(60)
                                pos_hint: {'x': 0.1}
                                margin: [10, 10]
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l1
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Alfinete'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o2
                                on_active: root.funcaoOpcao(self, 2)
                                group: 'grupo1'
                                width: dp(70)
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l2
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Amável'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o3
                                on_active: root.funcaoOpcao(self, 3)
                                group: 'grupo1'
                                width: dp(70)
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l3
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Juramento'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.48
                BoxLayout:
                    size_hint_y: 0.11
                BoxLayout:
                    size_hint_y: 0.04
                    Label:
                        id: retorno
                        text: 'Correto!'
                        halign: 'center'
                        valign: 'center'
                        color: root.divT 
                        font_name: 'robotomedium.ttf'
                        font_size: '55sp'
                        size_hint: 1.0, 1.0
                BoxLayout:
                    size_hint_y: 0.116
                BoxLayout:
                    size_hint_y: 0.04
                    Label:
                        id: resposta
                        text: 'A palavra era Amável!'
                        halign: 'center'
                        valign: 'center'
                        color: root.divT 
                        font_name: 'robotomedium.ttf'
                        font_size: '30sp'
                        size_hint: 1.0, 1.0
                BoxLayout:
                    size_hint_y: 0.2
                    MButton:
                        id: botaoProx
                        text: 'Próxima'
                        size_hint_y: None
                        border: (0, 0, 0, 0)
                        background_normal: ''
                        background_color: rgba('#123456')
                        on_press: root.proxima()               
""")


class Quiz(Screen):
    x = Window.width
    y = Window.height
    ops = ''
    labs = ''
    word = ''
    id_word = ''
    id_user = ''
    significado_pt = ''
    significado_en = ''
    audio = ''
    traducao = ''
    bg_color = Styles.primary_color
    div = Styles.primary_fundo
    divT = Styles.primary_fundo
    meaning = Styles.meaning_color
    lista = ''
    palavraCorreta = ''
    opCerta = ''
    listaPalavras = DrawQuiz()
    listaNumerosQuiz = DrawQuizOptions()
    indexQuiz = 0
    acerto = 0
    erro = 0
    ellipse_opacity = NumericProperty(1)


    def on_pre_enter(self, *args):
        Quiz.id_user = Login.id_user
        if Quiz.acerto + Quiz.erro != 5:
            random.seed()
            Quiz.opCerta = random.randint(0, 3)
            Quiz.ops = self.ids.o0, self.ids.o1, self.ids.o2, self.ids.o3
            Quiz.labels = self.ids.l0, self.ids.l1, self.ids.l2, self.ids.l3
            Quiz.lista = ['Corredor', 'Alfinete', 'Juramento', 'Rabanete', 'Carro', 'Pindamonha', 'Garrafa', 'Quebrar', 'Sofrer', 'Mãe', 'Pai', 'Filho', 'Irmão', 'Cerveja', 'Tela', 
                'Teta', 'Veja', 'Vi', 'Verei', 'Verás', 'Vou', 'Cruzeiro', 'Vírus', 'Computador', 'Pessoa', 'Amaciante', 'Lula', 'Lento', 'Ladrão', 'Rabo', 'Homossexual', 'Hétero'
                , 'Adolescente', 'Corno']
            palavra_da_vez = Database.selectWordById(Quiz.listaPalavras[Quiz.indexQuiz]).capitalize()
            self.ids.palavra.text = palavra_da_vez
            self.ids.score.text = f'{Quiz.acerto + Quiz.erro + 1}/5'
            Quiz.palavraCorreta = traduzir_com_linguee(palavra_da_vez).capitalize()
            print('AQUI >>', Quiz.labels, Quiz.opCerta, Quiz.palavraCorreta)
            Quiz.labels[Quiz.opCerta].text = ' ' + Quiz.palavraCorreta
            indexPalavras = Quiz.indexQuiz * 3
            for i in range(4):
                if Quiz.opCerta != i:
                    Quiz.labels[i].text = ' ' + Database.selectPalavraPortugues(Quiz.listaNumerosQuiz[indexPalavras])
                    indexPalavras += 1
            print('preenter')
            Quiz.reset(self)


    def goToMenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Home'
        

    def funcaoOpcao(self, cb, num):
        if cb.active:
            Quiz.setBotao(self, num == Quiz.opCerta)
        for op in Quiz.ops:
            op.disabled = 1
    

    def reset(self):
        tativ = Quiz.acerto
        terro = Quiz.erro
        Quiz.r = 0
        for op in Quiz.ops:
            op.active = False
        Quiz.r = 1
        Quiz.acerto = tativ
        Quiz.erro = terro
        self.ids.retorno.text = ''
        self.ids.resposta.text = ''
        self.ellipse_opacity = 0
        self.ids.botaoProx.disabled = 1


    def setBotao(self, certo):
        print(self, "entrou aqui mais uma vez")
        self.ellipse_opacity = 1
        self.ids.botaoProx.disabled = 0 if Quiz.indexQuiz < 4 else 1
        if certo:
            Quiz.acerto += 1
            print('id=',  Quiz.id_user, 'palavra=', Quiz.listaPalavras[Quiz.indexQuiz], 'fl=', 1)
            Database.linkWWP(Quiz.listaPalavras[Quiz.indexQuiz], Quiz.id_user)
            Database.insertQuiz(Quiz.id_user, Quiz.listaPalavras[Quiz.indexQuiz], 1)
            self.ids.retorno.text = 'Correto!'
            self.ids.resposta.text = 'Parabéns!'
        else:
            Quiz.erro += 1
            Database.linkWWP(Quiz.listaPalavras[Quiz.indexQuiz], Quiz.id_user)
            Database.insertQuiz(Quiz.id_user, Quiz.listaPalavras[Quiz.indexQuiz], 0)
            self.ids.retorno.text = 'Errado!'
            self.ids.resposta.text = f'A palavra era {Quiz.palavraCorreta}!'
        if Quiz.acerto + Quiz.erro == 5:
            act = 'acertos' if Quiz.acerto > 1 else 'acerto'
            err = 'erros' if Quiz.erro > 1 else 'erro'
            self.ids.resposta.text = f'{self.ids.resposta.text}\nVocê obteve {Quiz.acerto} {act}.'

            
    def proxima(self):
        Quiz.indexQuiz += 1
        if Quiz.indexQuiz > 4:
            self.ids.botaoProx.disabled = 1
        else:
            Quiz.on_pre_enter(self)
            for op in Quiz.ops:
                op.disabled = 0
 

# PERFIL
Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Perfil>:
    name: 'Perfil'
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout: 
                size_hint_y: 0.105
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'left'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: (self.pos[0]+dp(12), self.pos[1])
                                size: self.size
                                source: 'dl.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    text: 'Perfil'
                    halign: 'center'
                    font_name: 'robotomedium.ttf'
                    font_size: '40sp'
                    size_hint: 1.0, 1.0
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'right'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: self.pos
                                size: self.size
                                source: 'menu.png'
                        id: menu
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: app.show_menu(menu)
            BoxLayout: 
                size_hint_y: 0.105
                spacing: dp(-10)
                orientation: 'horizontal'
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                BoxLayout:
                    size_hint_x: 0.05 
                BoxLayout:
                    size_hint_x: 0.54
                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                            size_hint_y: 0.4
                            id: pnome
                            text: '    Magnus Carlsen'
                            halign: 'left'
                            font_name: 'robotolight.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '34sp'
                            color: (0.9, 0.9, 1, 1)
                        Label:
                            size_hint_y: 0.3
                            id: pemail
                            text: '    MagzyBogues'
                            halign: 'left'
                            font_name: 'robotolightitalic.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '20sp' 
                            color: (0.9, 0.9, 1, 1)
                            italic: True
                        Label:
                            size_hint_y: 0.3
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 0.18, 0.9
                    Button:
                        size_hint_y: 0.95
                        on_press: root.switchToEdit()
                        background_normal: 'edit.png'
                    BoxLayout:
                        size_hint_y: 0.05    
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 0.18, 0.9
                    Button:
                        size_hint_y: 0.95
                        on_press: root.quit()
                        background_normal: 'sair.png'
                    BoxLayout:
                        size_hint_y: 0.05  
            BoxLayout:
                size_hint_y: 0.790
                orientation: 'vertical'
                spacing: dp(-15)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb1
                            text: 'Favoritas (17)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(1)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb2
                            text: 'Já conhecia (27)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(2)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb3
                            text: 'Conheci aqui (34)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(3)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb4
                            text: 'Já sabia o significado (18)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(4)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb5
                            text: 'Aprendi aqui (11)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(5)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb6
                            text: 'Quiz acertadas (36)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(6)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)
                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb7
                            text: 'Quiz erradas (20)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'
                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(7)
                BoxLayout:
                    size_hint_y: 0.125
""")

class Perfil(Screen):
    word = 'tela perfil, mudar'
    nome = None
    id = None
    email = None
    titulo = ''
    palavras = ''


    def changeRightTo(self):
        print('eu sou o self', Perfil.tela, Perfil.tela.name)
        #Screen.manager.current = 'Home'


    @staticmethod
    def getWord():
        return Perfil.word
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo


    def on_pre_enter(self, *args):
        Perfil.nome = Database.selectNameById(Login.id_user)
        Perfil.email = Login.getEmail()
        Perfil.id = Login.id_user
        #palavras = Draw()
        self.ids.pnome.text = Perfil.nome
        self.ids.pemail.text = Perfil.email
        self.ids.lb1.text = f'Favoritas ({Database.selectFavs(Perfil.id)})'
        self.ids.lb2.text = f'Já conhecia ({Database.selectKnew(Perfil.id)})'
        self.ids.lb3.text = f'Conheci aqui ({Database.selectConheciAqui(Perfil.id)})'
        self.ids.lb4.text = f'Já sabia o significado ({Database.selectSabia(Perfil.id)})'
        self.ids.lb5.text = f'Aprendi aqui ({Database.selectLearnHere(Perfil.id)})'
        self.ids.lb6.text = f'Quiz acertadas ({Database.selectQuizAcertos(Perfil.id)})'
        self.ids.lb7.text = f'Quiz erradas ({Database.selectQuizErros(Perfil.id)})'


    def addFav(self):
        pass


    def wordScreen(self, num):
        if num == 1:   
            Perfil.palavras = Database.selectFavsWords(Perfil.id)
            Perfil.titulo = 'Favoritas'
        if num == 2:   
            Perfil.palavras = Database.selectKnewWords(Perfil.id)
            Perfil.titulo = 'Já conhecia'
        if num == 3:   
            Perfil.palavras = Database.selectConheciAquiWords(Perfil.id)
            Perfil.titulo = 'Conheci aqui'
        if num == 4:   
            Perfil.palavras = Database.selectSabiaWords(Perfil.id)
            Perfil.titulo = 'Sabia o significado'
        if num == 5:   
            Perfil.palavras = Database.selectLearnHereWords(Perfil.id)
            Perfil.titulo = 'Aprendi aqui'
        if num == 6:   
            Perfil.palavras = Database.selectQuizAcertoWords(Perfil.id)
            Perfil.titulo = 'Quiz acertadas'
        if num == 7:   
            Perfil.palavras = Database.selectQuizErroWords(Perfil.id)
            Perfil.titulo = 'Quiz erradas'
        self.manager.transition.direction = 'left'
        self.manager.current = 'Album'


    def printValues(self):
        print('next', self.ids.next.pos)
        print('sound', self.ids.sound.pos)


    def goToMenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Home'


    def quit(self):
        self.manager.transition.direction = 'right'
        self.manager.current='login'
    

    def switchToEdit(self):
        self.manager.transition.direction = 'left'
        self.manager.current='edit'


#PALAVRA
Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Palavra>:
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size       
    name: 'Palavra'
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout: 
                size_hint_y: 0.105
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'left'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: (self.pos[0]+dp(12), self.pos[1])
                                size: self.size
                                source: 'dl.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    id: titulo
                    text: 'Serendipity'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    font_size: '40sp'
                    size_hint: 1.0, 1.0
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'right'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: self.pos
                                size: self.size
                                source: 'menu.png'
                        id: menu
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: app.show_menu(menu)
            BoxLayout:
                size_hint_y: 0.895
                canvas.before:
                    Color:
                        rgba: root.div
                    RoundedRectangle:
                        pos: (self.pos[0]+dp(12), self.pos[1]+dp(12))
                        size: (self.size[0]*0.95, self.size[1]*0.97)
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: 0.004       
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.090
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound()
                        halign: 'left'
                        valign: 'center'
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: traducao
                            text: 'Serendipidade'
                            halign: 'left'
                            valign: 'center'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        halign: 'right'
                        valign: 'center'
                        background_normal: 'star.png'
                        on_press: root.linkProfileAndWord()    
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.695
                    canvas.before:
                        Color:
                            rgba: root.meaning
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(24), self.pos[1]+dp(12))
                            size: (self.size[0]*0.90, self.size[1]*0.98)
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: 0.93
                        ScrollView:
                            do_scroll_y: True
                            Label:
                                id: significado
                                size_hint_y: None
                                halign: 'left'
                                valign: 'center'
                                height: self.texture_size[1]
                                text_size: self.width, None
                                padding: [dp(30),dp(10)]
                                font_name: 'robotomedium.ttf'  
                                font_size: '24sp'
                    BoxLayout:
                        size_hint_y: 0.07
                BoxLayout:
                    size_hint_y: 0.05
                    orientation: 'horizontal'
                    height: dp(60)
                    padding: dp(5)
                    padding_top: dp(10)
                    spacing: dp(8)
                    BoxLayout:
                        size_hint_x: 0.1
                    BoxLayout:
                        size_hint_x: 0.8
                        spacing: dp(10)
                        ToggleButton:
                            id: option1
                            group: 'options'
                            state: 'down'
                            text: 'Português'
                            on_press: root.on_checkbox_active(option1, 1)
                        ToggleButton:
                            id: option2
                            group: 'options'
                            state: 'normal'
                            text: 'Inglês'
                            on_press: root.on_checkbox_active(option2, 2)
                    BoxLayout:
                        size_hint_x: 0.1   
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.161
                    size: self.minimum_size
                    padding: [dp(20),dp(20)]
                    BoxLayout:
                        size_hint_y: 0.15
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: b1
                                group: 'seriea'
                                on_active: root.changeProfile(self, 1, 1)
                                width: dp(50)
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                size_hint: None, 1
                                size: self.texture_size
                                text: 'Conhecia a palavra e sabia o significado!'
                                font_size: '19sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.15
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: b2
                                group: 'seriea'
                                on_active: root.changeProfile(self, 1, 0)
                                width: dp(60)
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                size_hint: None, 1
                                size: self.texture_size
                                text: 'Conhecia essa palavra, mas não o significado!'
                                font_size: '19sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.15
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                group: 'seriea'
                                id: b3
                                on_active: root.changeProfile(self, 0, 0)
                                width: dp(70)
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                size_hint: None, 1
                                size: self.texture_size
                                text: 'Não conhecia a palavra.'
                                font_size: '19sp'
                                halign: 'left'
                                valign: 'center'
""")


class Palavra(Screen):
    word = ''
    id_word = ''
    id_user = ''
    teste = ''
    significado_pt = ''
    significado_en = ''
    audio = ''
    traducao = ''
    bg_color = Styles.primary_color
    div = Styles.primary_fundo
    meaning = Styles.meaning_color
    def on_pre_enter(self, *args):
        Palavra.id_user = Home.id_user
        Palavra.id_word = Home.id_word
        temp = Database.selectWordKnoledge(Palavra.id_user, Palavra.id_word)
        if(temp == 1):
            self.ids.b1.active = True
        if(temp == 2):
            self.ids.b2.active = True
        if(temp == 3):
            self.ids.b3.active = True
        Palavra.word = Home.word
        Palavra.significado_pt = ''
        for a in Home.significado_pt:
            Palavra.significado_pt = Palavra.significado_pt + a + '\n'
        Palavra.significado_en = ''
        for b in Home.significado_en.values():
            Palavra.significado_en = Palavra.significado_en + b + '\n'
        Palavra.audio = Home.audio
        Palavra.traducao = Home.traducao
        self.ids.significado.text = Palavra.significado_pt
        self.ids.titulo.text = Palavra.word
        self.ids.traducao.text = Palavra.traducao.capitalize()
        if Database.isFav(Home.id_user, Home.id_word) == 1:
            self.ids.star.background_normal = 'starPress.png'
        else:
            self.ids.star.background_normal = 'star.png'
        self.ids.option2.state = 'normal'
        self.ids.option1.state = 'down'


    def on_checkbox_active(self, checkbox, value):
        if value == 1:
            self.ids.option2.state = 'normal'
            self.ids.option1.state = 'down'
            print('Valor 1,', Palavra.significado_pt)
            self.ids.significado.text = Palavra.significado_pt
        if value == 2:
            self.ids.option1.state = 'normal'
            self.ids.option2.state = 'down'
            print('Valor 2,', Palavra.significado_en)
            self.ids.significado.text = Palavra.significado_en
        print(self.ids.option1.state, self.ids.option2.state)
        print(self.ids.option1.size, self.ids.option2.size)


    def goToMenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Home'


    def linkProfileAndWord(self):
        if (self.ids.star.background_normal == 'star.png'):
            Database.linkWordWithProfile(Home.id_word, Home.id_user, 1)
            self.ids.star.background_normal = 'starPress.png'
        else: 
            Database.linkWordWithProfile(Home.id_word, Home.id_user, 0)
            self.ids.star.background_normal = 'star.png'


    def reproduceSound(self):
        print(Palavra.teste)


    def changeProfile(self, cb, conhecia, sabia):
        Palavra.teste += 'A'
        print(Palavra.id_word, Palavra.id_user, conhecia, sabia)
        Database.updateProfile(Palavra.id_word, Palavra.id_user, conhecia, sabia)


# HOME
Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Home>:
    name: 'Home'
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout: 
                size_hint_y: 0.105
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'left'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: (self.pos[0]+dp(12), self.pos[1])
                                size: self.size
                                source: 'dl.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    text: 'Palavras'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    font_size: '40sp'
                    size_hint: 1.0, 1.0
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'right'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: self.pos
                                size: self.size
                                source: 'menu.png'
                        id: menu
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: app.show_menu(menu)
            BoxLayout:
                size_hint_y: 0.009
            BoxLayout:
                size_hint_y: 0.727
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound0
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(0)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p0
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s0
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(0)
                    Button:
                        size_hint: 0.15, 0.95
                        size: self.size
                        on_press: root.wordScreen(0)
                        background_normal: 'next.png'
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound1
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(1)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p1
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s1
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(1)
                    Button:
                        size_hint: 0.15, 0.95
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(1)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(2)
                        
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p2
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s2
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(2)   
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(2)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(3)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p3
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s3
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(3)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(3)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(4)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p4
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s4
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(4) 
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(4)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(5)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p5
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s5
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(5)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(5)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(6)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p6
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s6
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(6)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(6)
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(7)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p7
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s7
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(7)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(7)
            BoxLayout:
                size_hint_y: 0.009
            BoxLayout:
                size_hint_y: 0.15
""")


class Home(Screen):
    word = 'tela home, mudar'
    traducao = ''
    audios = []
    id_word = ''
    significado_pt = ''
    significado_en = ''
    id_palavras = ''
    stars = ''
    palavras = Draw()
    email = None
    senha = None
    id_user = None
    nome = None
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo

    @staticmethod
    def getWord():
        return Home.word
    

    def on_pre_enter(self, *args):
        Home.email = Login.getEmail()
        Home.senha = Login.getPassword()
        Home.id_user = Login.getIduser()
        Home.nome = Login.getNome()
        Home.id_palavras = self.ids.p0, self.ids.p1, self.ids.p2, self.ids.p3, self.ids.p4, self.ids.p5, self.ids.p6, self.ids.p7
        Home.stars = self.ids.s0, self.ids.s1, self.ids.s2, self.ids.s3, self.ids.s4, self.ids.s5, self.ids.s6, self.ids.s7
        palavras = Draw()
        print(palavras)
        for i, palavra in enumerate(palavras):
            iword = str(Database.selectWord(palavra)[0][0])
            Home.id_palavras[i].text = iword.capitalize()
            print(iword.capitalize())
            if Database.isFav(Home.id_user, Home.palavras[i]) == 1:
                Home.stars[i].background_normal = 'starPress.png'
            else:
                Home.stars[i].background_normal = 'star.png'


    def addFav(self):
        pass


    def linkProfileAndWord(self, idWord):
        if (Home.stars[idWord].background_normal == 'star.png'):
            Database.linkWordWithProfile(Home.palavras[idWord], Home.id_user, 1)
            Home.stars[idWord].background_normal = 'starPress.png'
        else: 
            Database.linkWordWithProfile(Home.palavras[idWord], Home.id_user, 0)
            Home.stars[idWord].background_normal = 'star.png'


    def wordScreen(self, idWord):
        Home.word = str(Database.selectWord(Draw()[idWord])[0][0]).capitalize()
        Home.id_word = Database.selectIdFromWord(Home.word.lower())
        print(Home.word.lower())
        dados = API_request(Home.word.lower())
        Home.audio = dados['audios']
        Home.significado_en = dados['definitions']
        Home.traducao = dados['traducao']
        Home.significado_pt = dados['portugues']
        Database.linkWWP(Home.palavras[idWord], Home.id_user)    
        self.manager.transition.direction = 'left'    
        self.manager.current = 'Palavra'


    def goToMenu(self):
        self.manager.current = 'Home'


    def reproduceSound(self, idWord):
        Database.linkWWP(Home.palavras[idWord], Home.id_user)


# SIGNUP
Builder.load_string("""
#: import CTextInput custom_widgets
#: import CButton custom_widgets
<Signup>:
    name: 'signup'
    canvas.before:
        Color:
            rgba: 0.3, 0.45, 0.7, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        BoxLayout:
            size_hint: 1.0, 0.04
        BoxLayout:
            size_hint: 1, 0.34
            Image:
                source: 'logo.png'
        BoxLayout:
            size_hint: 1, 0.07
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: 'top'           
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                spacing: dp(10)
                height: self.minimum_height
                padding: [dp(30), 0, dp(30), 0] 
                Label:
                    text: 'Crie sua conta'
                    font_size: '16sp'
                    size_hint_y: None
                    color: 1, 1, 1, 1   
                    halign: 'left'
                    text_size: self.size 
                    font_name: 'robotoblack.ttf'
                    size: self.texture_size
                CTextInput:
                    id: email
                    hint_text: "email"
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    on_text: root.space_check(self)
                CTextInput:
                    id: name
                    hint_text: 'nome'
                    max_length: 25
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    on_text: root.name_check(self)
                CTextInput:
                    id: password
                    hint_text: 'senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                CTextInput:
                    id: cpassword
                    hint_text: 'confirmar senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                CButton:
                    text: 'Criar conta'
                    on_press: root.createEntry()
                    size_hint_y: None
                    height: dp(50)
                Label:
                    id: msg
                    text: ''
                    color: 0.3, 0, 0, 1   
                    haling: 'left'
                    text_size: self.size 
                    font_name: 'robotolight.ttf'
""")

    
class Signup(Screen):
    def on_pre_enter(self, *args):
        self.ids.email.text = ''
        self.ids.name.text = ''
        self.ids.password.text = ''
        self.ids.cpassword.text = ''


    def createEntry(self):
        email = self.ids.email.text
        name = self.ids.name.text
        password = self.ids.password.text
        cpassword = self.ids.cpassword.text
        if (email == '' or password == '' or name =='' or cpassword == ''):
            self.ids.msg.text = 'Informações incompletas!'
        else: 
            if(len(password) > 7):
                if(password == cpassword):
                    if(Database.isValid(email)):
                        Database.insertdata(email, name, password)
                        self.manager.transition.direction = 'right'
                        self.manager.current = 'login'
                    else:
                        self.ids.msg.text = 'Email já cadastrado!'
                else:
                    self.ids.msg.text = 'As senhas não coincidem!'
            else:
                self.ids.msg.text = 'A senha deve ter pelo menos 8 caracteres.'   
            


    def name_check(self, text_input):
        if(len(text_input.text) > 25):
            text_input.text = text_input.text[:-1]


    def space_check(self, text_input):
        text_input.text = text_input.text.replace(" ", "")


# LOGIN
Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignupText custom_widgets                                        
<Login>:
    name: 'login'
    canvas.before:
        Color:
            rgba: 0.3, 0.45, 0.7, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        BoxLayout:
            size_hint: 1.0, 0.04

        BoxLayout:
            size_hint: 1.0, 0.34
            Image:
                source: 'logo.png'
        BoxLayout:
            size_hint: 1.0, 0.07
        AnchorLayout:
            size_hint: 1.0, 0.45
            anchor_y: 'top'
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: [dp(30), 0, dp(30), 0] 
                Label:
                    text: 'Acesse sua conta'
                    font_size: '16sp'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    text_size: self.size
                    size_hint_y: None
                    size: self.texture_size
                    color: 1, 1, 1, 1
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: 'e-mail'
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    hint_text: 'senha'
                CButton:
                    text: 'Entrar'
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.login()
                Label:
                    id: msg
                    text: ''
                    color: 0.5, 0.1, 0.1, 1   
                    haling: 'left'
                    text_size: self.size
        AnchorLayout:
            size_hint: 1.0, 0.10
            anchor_x: 'center'
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                Label:
                    text: 'Não possui uma conta?'
                    color: 1, 1, 1, 1
                    size_hint_x: None
                    size: self.texture_size

                SignupText:
                    text: ' Cadastre-se'
                    font_name: 'robotoblack.ttf'
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switchToSignUp()                            
""")



class Login(Screen):
    email = None
    password = None
    id_user = None
    nome = None
    

    @staticmethod
    def getEmail():
        return Login.email
    

    @staticmethod
    def getPassword():
        return Login.password


    @staticmethod
    def getIduser():
        return Login.id_user
    

    @staticmethod
    def getNome():
        return Login.nome

    
    def login(self):
        Login.email = self.ids.email.text
        Login.password = self.ids.password.text
        if (Login.email == '' or Login.password == ''):
            self.ids.msg.text = 'Informações incompletas!'    
        else:
            if(Database.isExist(Login.email, Login.password)):
                #self.ids.msg.text = 'Logado com sucesso!'
                Login.id_user = Database.selectIdFromEmail(Login.email)
                Login.nome = Database.selectNameFromEmail(Login.email)
                self.manager.transition.direction = 'left'
                self.manager.current = 'Home' 
            else:
                self.ids.msg.text = 'Email e/ou senha incorretos!'
            


    def switchToSignUp(self):
        self.manager.transition.direction = 'left'
        self.manager.current='signup'


    def on_pre_enter(self, *args):
        self.ids.email.text = ''
        self.ids.password.text = ''
        self.ids.msg.text = ''
        Login.email = None
        Login.password = None
        Login.id_user = None
        Login.nome = None


# MAIN
Window.softinput_mode="below_target"
Window.size = (480, 912)


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
    

class English(App):
    dropdown = None
    def show_menu(self, id):
        English.dropdown = DropdownMenu()
        English.dropdown.open(id)


English().run()
