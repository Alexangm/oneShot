from sqlite3 import connect
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
    def insertdata(email, name, password):
        sql = 'INSERT INTO users (email, name, password) VALUES (?, ?, ?)'
        val = (f'{email}', f'{name}', f'{password}')
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    @staticmethod
    def alterTableProfile():
        sql = 'ALTER TABLE profile ADD COLUMN fl_sabia integer DEFAULT 0'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit() 

    @staticmethod
    def isValid(email):
        sql = f'SELECT * FROM users WHERE email="{email}"'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if(result):
            return False
        else:
            return True

    @staticmethod
    def isExist(email, password):
        sql = f'SELECT * FROM users WHERE email="{email}" and password = "{password}"'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if(result):
            return True
        else:
            return False
        

    @staticmethod
    def insertWord(word):
        sql = f"INSERT INTO words (word) VALUES ('{word}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()


    def linkWordWithProfile(id_word, id_user, fav):
        sql = f'SELECT * FROM profile WHERE id_user="{id_user}" and id_word = "{id_word}"'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if(result):
            sql = f"UPDATE profile SET fl_favorita = {fav} where id_word = ({id_word}) and id_user = ({id_user})"
            cursor = Database.db.cursor()
            cursor.execute(sql)
            Database.db.commit()
            return 'result true'
        else:
            sql = f'INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES ({id_user}, {id_word}, 0, {fav})'
            cursor = Database.db.cursor()
            cursor.execute(sql)
            Database.db.commit()
            return 'result false'



    @staticmethod
    def insertQuiz(id_user, id_word, fl_acerto):
        sql = f'SELECT * FROM palavrasQuiz WHERE id_user="{id_user}" and id_word = "{id_word}"'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if(result):
            return 0
        else:
            sql = f"INSERT INTO palavrasQuiz (id_user, id_word, fl_acerto) VALUES ({id_user}, {id_word}, {fl_acerto})"
            cursor = Database.db.cursor()
            cursor.execute(sql)
            Database.db.commit()
            return 1


    @staticmethod
    def insertPalavraPortugues(palavra):
        sql = f"INSERT INTO palavrasPortugues (word) VALUES ('{palavra}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()


    @staticmethod
    def selectPalavraPortugues(id):
        sql = f"SELECT word FROM palavrasPortugues where id_word = ({id})"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]


    # retorna a palavra pelo id
    @staticmethod
    def selectWord(id):
        sql = f"SELECT word FROM words where id_word = ({id})"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()
    

    @staticmethod
    def selectWordById(id):
        sql = f"SELECT word FROM words where id_word = ({id})"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]

    @staticmethod
    def selectAllWords():
        sql = f"SELECT * FROM words"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()
    

    @staticmethod
    def changeUser(id_user, name, password):
        sql = f"UPDATE users SET password = '{password}', name = '{name}' where id_user = ('{id_user}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return 'result true'
    

    @staticmethod
    def changePassword(id_user, password):
        sql = f"UPDATE users SET password = '{password}' where id_user = ('{id_user}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return 'result true'


    @staticmethod
    def changeName(id_user, name):
        sql = f"UPDATE users SET name = '{name}' where id_user = ('{id_user}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return 'result true'


    @staticmethod
    def selectIdFromWord(word):
        sql = f"SELECT id_word FROM words WHERE word=('{word}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectNameById(id_user):
        sql = f"SELECT name FROM users WHERE id_user=('{id_user}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]

    #retorna id pelo email
    @staticmethod
    def selectIdFromEmail(email):
        sql = f"SELECT id_user FROM users WHERE email=('{email}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectNameFromEmail(email):
        sql = f"SELECT name FROM users WHERE email=('{email}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectPasswordFromId(id_user):
        sql = f"SELECT password FROM users WHERE id_user=('{id_user}')"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return cursor.fetchall()[0][0]

    
    @staticmethod
    def linkWordWithProfile(id_word, id_user, fav):
        sql = f'SELECT * FROM profile WHERE id_user="{id_user}" and id_word = "{id_word}"'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if(result):
            sql = f"UPDATE profile SET fl_favorita = {fav} where id_word = ({id_word}) and id_user = ({id_user})"
            cursor = Database.db.cursor()
            cursor.execute(sql)
            Database.db.commit()
            return 'result true'
        else:
            sql = f'INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES ({id_user}, {id_word}, 0, {fav})'
            cursor = Database.db.cursor()
            cursor.execute(sql)
            Database.db.commit()
            return 'result false'
        
    @staticmethod
    def linkWWP(id_word, id_user):
        sql = f'SELECT * FROM profile WHERE id_user="{id_user}" and id_word = "{id_word}"'
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if(result):
            return print('conexao existente')
        else:
            sql = f'INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES ({id_user}, {id_word}, 0, 0)'
            cursor = Database.db.cursor()
            cursor.execute(sql)
            Database.db.commit()
            return print('conexao criada')


    @staticmethod
    def isFav(id_user, id_word):
        sql = f"SELECT fl_favorita FROM profile WHERE (id_user={id_user}) AND (id_word = {id_word})"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result):
            Database.db.commit()
            return result[0][0]
        else:
            Database.db.commit()
            return -1

    @staticmethod
    def selectFavs(idUser):
        sql = f"SELECT count(*) FROM profile where fl_favorita = ({1}) AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectFavsWords(idUser):
        sql = f"SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_favorita = ({1}) AND id_user = {idUser} order by 1"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        

    @staticmethod
    def selectKnew(idUser):
        sql = f"SELECT count(*) FROM profile where fl_conhecia = ({1}) AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectKnewWords(idUser):
        sql = f"SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_conhecia = ({1}) AND id_user = {idUser} order by 1"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectConheciAqui(idUser):
        sql = f"SELECT count(*) FROM profile where fl_conhecia = ({0}) AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectConheciAquiWords(idUser):
        sql = f"SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_conhecia = ({0}) AND id_user = {idUser} order by 1"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectSabia(idUser):
        sql = f"SELECT count(*) FROM profile where fl_sabia = ({1}) AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectSabiaWords(idUser):
        sql = f"SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_sabia = ({1}) AND id_user = {idUser} order by 1"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0

    @staticmethod
    def selectLearnHere(idUser):
        sql = f"SELECT count(*) FROM profile where fl_sabia = 0 AND fl_conhecia = 0 AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectLearnHereWords(idUser):
        sql = f"SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_sabia = 0 AND fl_conhecia = 0 AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectQuizAcertos(idUser):
        sql = f"SELECT count(*) FROM palavrasQuiz where fl_acerto = 1 AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    
    @staticmethod
    def selectQuizErros(idUser):
        sql = f"SELECT count(*) FROM palavrasQuiz where fl_acerto = 0 AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectQuizAcertoWords(idUser):
        sql = f"SELECT w.word FROM palavrasQuiz p inner join words w on p.id_word = w.id_word where fl_acerto = 1 AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0


    @staticmethod
    def selectQuizErroWords(idUser):
        sql = f"SELECT w.word FROM palavrasQuiz p inner join words w on p.id_word = w.id_word where fl_acerto = 0 AND id_user = {idUser}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
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
        sql = f"UPDATE profile SET fl_conhecia = {conhecia}, fl_sabia = {sabia} where id_word = ({id_word}) and id_user = ({id_user})"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return 1
    

    @staticmethod
    def deleteUser(id_user):
        sql = f"DELETE FROM profile WHERE id_user = {id_user}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        sql = f"DELETE FROM users WHERE id_user = {id_user}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        return 1


    @staticmethod
    def selectWordKnoledge(id_user, id_word):
        sql = f"SELECT fl_conhecia, fl_sabia FROM profile where id_user = {id_user} AND id_word = {id_word}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        Database.db.commit()
        if result[0][0] and result[0][1]:
            return 1
        if result[0][0] and not result[0][1]:
            return 2
        if not result[0][0] and not result[0][1]:
            return 3


    @staticmethod
    def genericQuery(id_user, id_word):
        sql = f"SELECT fl_conhecia, fl_sabia FROM profile where id_user = {id_user} AND id_word = {id_word}"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        Database.db.commit()
        if result[0][0] and result[0][1]:
            return 1
        if result[0][0] and not result[0][1]:
            return 2
        if not result[0][0] and not result[0][1]:
            return 3
