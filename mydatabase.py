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

Database.ConnectDatabase()
if (Database.isEmpty()):
    palavrasIngles = ["abandoned","abdomen","aberrant","abhorrent","ability","abnormal","abode","abolish","abominable","aboriginal","abound","abrasive","abrupt","absence","absolute",
                  "absorbent","abstain","abstract","absurd","abundant","academia","accelerate","accent","accessible","accidental","accomplish","accordance","accountant","accumulate",
                  "accurate","accuse","achieve","acidic","acquaintance","acquire","adaptable","adhesive","admirable","adore","adorn","adventurous","affection","affirmative",
                  "aggressive","agonize","agreeable","airplane","alarming","alcohol","alertness","alienate","allegiance","alleviate","alliance","allocate","alluring","alphabet",
                  "alteration","amazing","ambition","ambiguous","ambitious","ameliorate","amendment","amiable","amplitude","analogous","analytical","ancestor","ancient","angelic",
                  "anguish","animated","annihilate","annoyance","apologize","appalling","appealing","appetite","apprehend","arbitrary","architect","ardent","aristocrat","aromatic",
                  "articulate","ascend","aspiration","assassinate","assertive","assistance","assumption","astonishing","atmosphere","atrocious","attentive","attractive","authentic",
                  "authority","automatic","auxiliary","availability","avaricious","avenue","awakening","awkward","backpack","barricade","beautiful","beneficial","bewilder","bizarre",
                  "boundary","bountiful","breathtaking","brigade","brilliant","buoyant","calculate","candid","capability","capacity","captivating","caricature","catalyst",
                  "celebration","ceremonial","challenge","champion","chaotic","charitable","chase","chastise","chivalrous","circulate","clandestine","clarity","coalesce","collaborate",
                  "collective","colossal","combatant","comfortable","commander","commemorate","commendable","commiserate","compassion","compatible","compensate","competitive",
                  "compliment","comprehensive","compromise","conceivable","conclusive","condemn","conditional","confidant","confident","conformity","confrontation","confuse","congruent",
                  "conquer","conscientious","consequence","conservative","considerate","consistent","constitute","constructive","contemplate","contradict","contribute","controversy",
                  "convenient","conviction","cooperate","cordial","corroborate","cosmopolitan","courageous","covetous","credibility","criterion","cruelty","cumulative","curiosity",
                  "cynical","dauntless","deception","decipher","decrease","dedicate","defensive","deficiency","definite","delectable","delightful","democracy","demolish","demonstrate",
                  "denounce","dependence","deplorable","depreciate","derivative","desirable","determination","devastate","differentiate","dignity","dilemma","dimension","diplomatic",
                  "discreet","disposition","distinction","divulge","dominance","dormant","dubious","durable","eccentric","education","effectiveness","efficacy","effortless","elaborate",
                  "electrify","elegance","eloquent","elucidate","emancipate","embark","embellish","embrace","emerge","empower","encompass","encounter","endurance","energetic","enlighten",
                  "enormous","enthusiastic","envisage","equilibrium","erosion","erratic","essential","establish","ethereal","evaluate","evasive","evident","exaggerate","exceed",
                  "exceptional","exemplary","exhaustive","exhilarate","expansive","expedite","exquisite","extensive","extravagant","facilitate","fantastic","fascinate","feasible",
                  "ferocious","finagle","flourish","forthcoming","fortunate","fragrance","frustrate","fundamental","generosity","genuine","gigantic","glamorous","gleaming","graceful",
                  "gracious","grateful","gregarious","guarantee","habitat","harmonious","hedonistic","heighten","hereditary","heroic","hesitate","hideous","homogeneous","honesty",
                  "horrendous","horror","humiliate","hypothesize","illuminate","immaculate","imminent","immortal","impartial","impeccable","impede","imperative","imperial","impervious",
                  "implement","imposing","impressive","incentive","inclusive","incredible","indefatigable","indispensable","indulgence","industrious","infallible","infinite",
                  "influential","ingenious","inherent","inhibit","innovate","inquisitive","insightful","insinuate","inspiration","integrity","integrate","intense","interact","intercede",
                  "intermittent","intricate","intriguing","invincible","irresistible","irrevocable","isolate","jubilant","judicious","juxtapose","lament","landmark","laudable",
                  "lavish","legendary","legitimate","leverage","liability","luminous","luxurious","magnitude","malicious","manifest","manipulate","marvelous","mastery","meander",
                  "mediate","melancholy","mellifluous","memorable","meticulous","miraculous","misanthrope","momentous","monumental","morality","morphology","motivate","mysterious",
                  "narrative","navigate","nefarious","negligible","neurotic","noble","nonchalant","nonetheless","noteworthy","nourish","noxious","numinous","nurture","objective",
                  "oblivion","obnoxious","obscurity","obstacle","obstinate","occasional","ominous","ornamental","outrageous","outstanding","overcome","overwhelm","palatable","paradoxical",
                  "paramount","parsimonious","passionate","pathetic","patience","penchant","perceptive","perennial","perfection","permeate","perspective","pertinent","philanthropy",
                  "picturesque","pinnacle","pious","plausible","plethora","poignant","ponder","portray","pragmatic","precarious","precise","predicament","preferable","prejudice",
                  "preposterous","prestigious","prevail","pristine","profound","progressive","prolific","prominent","propagate","prosperity","providence","prowess","prudent","punctual",
                  "purify","quintessential","radical","ramification","rapture","rational","reassure","receptive","reconciliation","refinement","reflection","relentless","reluctant",
                  "remarkable","renowned","replenish","replicate","resilient","resolve","restraint","reticent","reverence","rigorous","robust","rudimentary","salient","sanctuary",
                  "scintillate","seclusion","serendipity","serene","shimmer","spontaneous","stalwart","stimulate","strategic","suave","sublime","subtle","successive","suffice","sumptuous",
                  "superb","supernatural","surpass","surreptitious","susceptible","synchronize","tangible","teem","temperance","tenuous","terminate","terrific","theoretical",
                  "threshold","thrive","tranquil","transform","transient","transparent","trepidation","triumphant","ultimate","uncanny","undermine","undulate","unprecedented",
                  "uplift","urbane","validate","versatile","vibrant","vigilant","virtuous","visionary","vivacious","volatile","vulnerable","wholesome","wondrous","zenith"]
    for word in palavrasIngles:
        Database.insertWord(word)
    print("Palavras em inglês inseridas!")
    palavrasPT = ["Abacaxi","Abajur","Abóbora","Abraço","Açúcar","Adeus","Adesivo","Adolescente","Advogado","Aeroplano","Agulha","Alegria","Alface","Almofada","Amarelo","Amigo",
                  "Amor","Anel","Animal","Antena","Aparador","Apelido","Apito","Apresentação","Arco-íris","Arroz","Arte","Asa","Assado","Aventura","Azul","Bala","Balança","Balde",
                  "Bambu","Banho","Barco","Barraca","Barulho","Basquete","Bateria","Bebida","Beijo","Beleza","Berinjela","Bicicleta","Bilhete","Biscoito","Bolacha","Bola","Bolo",
                  "Bomba","Boneca","Borracha","Botão","Branco","Brilho","Brinquedo","Broto","Cabelo","Caçador","Café","Caixa","Calça","Cama","Caminho","Caneca","Caneta","Canela",
                  "Capa","Capitão","Carro","Carta","Casa","Casamento","Castelo","Céu","Chave","Cheiro","Chocolate","Chuva","Cidade","Círculo","Classe","Clube","Coelho","Coisa",
                  "Colher","Comida","Computador","Concha","Confusão","Coração","Corrida","Cortina","Criança","Cuidado","Curioso","Dado","Dança","Decisão","Dedo","Dentista","Depois",
                  "Deserto","Desenho","Desfile","Destino","Dia","Diamante","Dicionário","Diferente","Dinheiro","Direção","Disco","Doce","Doido","Domingo","Dono","Dormir","Dragão",
                  "Drible","Durante","E-mail","Efeito","Elegante","Elefante","Elevador","Embarcação","Emoção","Encanto","Encontro","Energia","Enfeite","Engrenagem","Enigma",
                  "Entrada","Envelope","Escada","Escola","Escova","Escuridão","Esfera","Espelho","Espuma","Estação","Estrela","Estudante","Exame","Exemplo","Experiência","Fada",
                  "Fazenda","Fechadura","Felicidade","Feriado","Ferro","Festa","Fio","Flor","Fogo","Folha","Fome","Forma","Fotografia","Fruta","Fumaça","Futebol","Gaiola",
                  "Galinha","Garfo","Garrafa","Gato","Gelado","Gelatina","Gelo","Gente","Girafa","Giro","Globo","Golfinho","Gosto","Grama","Gravata","Guarda-chuva","Guerra",
                  "Guitarra","Gula","Guri","Hora","Hospital","Hotel","Ilha","Ilusão","Imaginação","Impacto","Incentivo","Inicial","Inocente","Inseto","Inteiro","Inverno","Isca",
                  "Janela","Jantar","Jardim","Jato","Jogo","Joia","Jornal","Jovem","Juventude","Lábio","Ladrão","Lagarto","Lago","Lanche","Lanterna","Laranja","Larva","Leão",
                  "Leite","Leitura","Lenço","Leque","Letra","Levantar","Liberdade","Licença","Limão","Linda","Língua","Lista","Livro","Lobo","Locutor","Longe","Louco","Luar",
                  "Lugar","Luz","Maçã","Mágico","Mala","Mamão","Mandarim","Mandioca","Manga","Máquina","Mar","Marca","Marcador","Mármore","Mariposa","Marmelada","Martelo","Máscara",
                  "Massa","Medo","Meia","Melancia","Melhor","Melodia","Melro","Memória","Menina","Mente","Mercado","Mestre","Meu","Mexer","Mezanino","Milagre","Minuto","Missão",
                  "Misto","Modelo","Moderno","Molho","Momento","Monstro","Montanha","Montar","Morango","Morte","Mosca","Mudo","Mundo","Música","Nada","Nascimento","Nascer",
                  "Natureza","Navegar","Névoa","Neve","Ninho","Nível","Noite","Nome","Número","Oceano","Oito","Olhar","Onda","Orelha","Orgulho","Ouro","Página","País","Palavra",
                  "Palhaço","Pão","Papel","Parque","Passarinho","Passeio","Pássaro","Pato","Pátio","Pau","Pedra","Pégaso","Peixe","Pena","Pente","Pequeno","Perdão","Perfume",
                  "Perigo","Perfeito","Pérola","Pessoal","Pétala","Piano","Pimenta","Pingente","Pintar","Piscina","Piso","Planeta","Planta","Plástico","Poema","Poesia","Poder",
                  "Poltrona","Porco","Porta","Prato","Prima","Princesa","Prisão","Proa","Professor","Projeto","Pronto","Próprio","Proteger","Publicidade","Pudim","Pular","Pulmão",
                  "Pulsar","Pura","Purificar","Quadro","Qualidade","Quarto","Quase","Queijo","Quente","Querer","Questão","Quieto","Quilo","Química","Quisera","Raio","Rápido","Rato",
                  "Realidade","Recado","Receber","Recife","Reflexo","Regra","Relógio","Renda","Rente","Repetir","Repouso","Resposta","Retorno","Riqueza","Risco","Riso","Riqueza",
                  "Rolo","Ronda","Rosa","Rosto","Roupa","Rua","Ruído","Saber","Sabor","Saco","Sagrado","Salada","Salário","Salsicha","Saltar","Sábado","Sábio","Sacola","Salto",
                  "Sapato","Saudade","Segredo","Seis","Selva","Semana","Semente","Sentido","Serpente","Seta","Setembro","Silêncio","Simples","Sinal","Sino","Sintonia","Síntese",
                  "Sítio","Socorro","Sol","Soldado","Sombra","Sonhar","Sorriso","Sorte","Suavidade","Subir","Sucata","Sucesso","Suficiente","Sugestão","Sujeira","Susto","Tábua",
                  "Tarefa","Tartaruga","Telefone","Tempestade","Tempo","Tenda","Tenente","Terça-feira","Terno","Teste","Tigre","Tilintar","Tinta","Tio","Tirar","Toalha","Todavia",
                  "Tomate","Topo","Torre","Trabalho","Tradição","Trago","Traje","Três","Triângulo","Trocar","Troféu","Trombeta","Trovão","Truque","Tubarão","Tudo","Tule","Turma",
                  "Túnel","Turno","Um","Último","Umbigo","Unha","Universo","Urso","Uva","Vaca","Vaga","Vaidade","Vai","Valsa"]
    for palavra in palavrasPT:
        Database.insertPalavraPortugues(palavra)
    print("Palavras em portugues inseridas!")
