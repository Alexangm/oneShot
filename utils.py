import random

#SORTEIOS
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
    dicionario = ['muito siginficiado legal', word]
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
