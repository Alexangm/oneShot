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
    dados = []
    if word == 'Accuse' or word == 'accuse':
        dados["word"] = 'Accuse'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. transitivo direto, bitransitivo e intransitivo e pronominal',
                                 'atribuir falta, infração ou crime a (alguém ou si próprio); culpar(-se), incriminar(-se).acusou o inocente sem dó nem piedade',
                                 'transitivo direto e pronominal ter ou exprimir julgamento moral desfavorável em relação a (alguém ou si próprio).',
                                 '"o passado criminoso acusa-os para sempre"',
                                 'Etmologia: do Latim accusare, “chamar a juízo”']
        dados["synonyms"] = ''
        dados["antonyms"] = ''
        #dados["definitions"] = {'definition':'oasioas', }
        dados["traducao"] = 'Acusar'      
        dados["portugues"] = ['1. Transitivo direto, bitransitivo e intransitivo e pronominal',
                                '2. Atribuir falta, infração ou crime a (alguém ou si próprio); culpar(-se), incriminar(-se).acusou o inocente sem dó nem piedade',
                                '3. Transitivo direto e pronominal ter ou exprimir julgamento moral desfavorável em relação a (alguém ou si próprio).',
                                '"o passado criminoso acusa-os para sempre"',
                                '4. Etmologia: do Latim accusare, “chamar a juízo”']
    if word == 'Affection' or word == 'affection':
        dados["word"] = 'Affection'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. noun',
                                'a gentle feeling of fondness or liking.',
                                '"she felt affection for the wise old lady"',
                                '2. the action or process of affecting or being affected.',
                                '"the affection of the drug soon began to wear off"']
        dados["synonyms"] = ''
        dados["antonyms"] = ''
        dados["traducao"] = 'Afeição'      
        dados["portugues"] = ['1. Substantivo',
                                '2. Sentimento suave de carinho ou simpatia.',
                                '"ela sentia afeição pela sábia senhora idosa"',
                                '3. Ação ou processo de afetar ou ser afetado.',
                                '"a afeição do medicamento logo começou a passar"']
    if word == 'Alleviate' or word == 'alleviate':
        dados["word"] = 'Alleviate'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. verb',
                                'make (suffering, deficiency, or a problem) less severe.',
                                '"he couldn\'t prevent her pain, only alleviate it"',
                                '2. mitigate; lessen.',
                                '"the measures taken did little to alleviate the crisis"']
        dados["synonyms"] = 'relieve, ease, mitigate, lessen, lighten'
        dados["antonyms"] = 'aggravate, intensify, worsen'
        dados["traducao"] = 'Aliviar'      
        dados["portugues"] = ['1. Verbo',
                                '2. Tornar (sofrimento, deficiência ou um problema) menos grave.',
                                '"ele não podia evitar a dor dela, apenas aliviá-la"',
                                '3. Mitigar; diminuir.',
                                '"as medidas tomadas pouco aliviaram a crise"']
    if word == 'Celebration' or word == 'celebration':
        dados["word"] = 'Celebration'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. noun',
                                'the action of marking one\'s pleasure at an important event or occasion by engaging in enjoyable, typically social, activity.',
                                '"the birth of a son called for a celebration"',
                                '2. the public performance of a sacrament or solemn ceremony with all appropriate ritual.',
                                '"the celebration of Mass"']
        dados["synonyms"] = 'festivity, festiveness, rejoicing, merrymaking'
        dados["antonyms"] = 'mourning, lamentation, solemnity'
        dados["traducao"] = 'Celebração'      
        dados["portugues"] = ['1. Substantivo',
                                '2. Ação de expressar prazer em um evento ou ocasião importante participando de atividades agradáveis, geralmente sociais.',
                                '"o nascimento de um filho exigia uma celebração"',
                                '3. A execução pública de um sacramento ou cerimônia solene com todo o ritual apropriado.',
                                '"a celebração da missa"']
    if word == 'Circulate' or word == 'circulate':
        dados["word"] = 'Circulate'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. verb',
                                'move or cause to move continuously or freely through a closed system or area.',
                                '"air is extracted from the greenhouse and circulated through underground pipes"',
                                '2. pass or cause to pass from place to place or person to person.',
                                '"we circulated a petition to save the historic building"']
        dados["synonyms"] = 'disseminate, distribute, spread, transmit'
        dados["antonyms"] = 'confine, retain, hoard'
        dados["traducao"] = 'Circular'      
        dados["portugues"] = ['1. Verbo',
                                '2. Mover-se ou fazer mover-se continuamente ou livremente através de um sistema fechado ou área.',
                                '"o ar é extraído da estufa e circulado por tubos subterrâneos"',
                                '3. Passar ou fazer passar de um lugar para outro ou de pessoa para pessoa.',
                                '"circulamos uma petição para salvar o edifício histórico"']
    if word == 'Mastery' or word == 'mastery':
        dados["word"] = 'Mastery'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. noun',
                                'comprehensive knowledge or skill in a particular subject or activity.',
                                '"his mastery of English was astonishing"',
                                '2. control or superiority over someone or something.',
                                '"her mastery of her emotions"']
        dados["synonyms"] = 'proficiency, expertise, command, skill'
        dados["antonyms"] = 'incompetence, ineptitude, ignorance'
        dados["traducao"] = 'Domínio'      
        dados["portugues"] = ['1. Substantivo',
                                '2. Conhecimento ou habilidade abrangente em um assunto ou atividade específica.',
                                '"seu domínio do inglês era surpreendente"',
                                '3. Controle ou superioridade sobre alguém ou algo.',
                                '"o domínio dela sobre suas emoções"']
    if word == 'Predicament' or word == 'predicament':
        dados["word"] = 'Predicament'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. noun',
                                'a difficult, unpleasant, or embarrassing situation.',
                                '"the club is in a financial predicament"',
                                '2. a category or type of situation, especially one that is awkward or difficult to deal with.',
                                '"we are faced with a moral predicament"']
        dados["synonyms"] = 'dilemma, quandary, plight, conundrum'
        dados["antonyms"] = 'solution, advantage, benefit'
        dados["traducao"] = 'Dilema'      
        dados["portugues"] = ['1. Substantivo',
                                '2. Uma situação difícil, desagradável ou embaraçosa.',
                                '"o clube está em uma situação financeira difícil"',
                                '3. Uma categoria ou tipo de situação, especialmente aquela que é difícil ou complicada de lidar.',
                                '"estamos diante de um dilema moral"']
    if word == 'Serendipity' or word == 'serendipity':
        dados["word"] = 'Serendipity'
        dados["audios"] = 'audio'
        dados["definitions"] = ['1. noun',
                                'the occurrence and development of events by chance in a happy or beneficial way.',
                                '"a fortunate stroke of serendipity"',
                                '2. the faculty or phenomenon of finding valuable or agreeable things not sought for.',
                                '"the element of serendipity in the invention of the X-ray"']
        dados["synonyms"] = 'fortuity, chance, luck, fortune'
        dados["antonyms"] = 'misfortune, bad luck, fate'
        dados["traducao"] = 'Serendipidade'      
        dados["portugues"] = ['1. Substantivo',
                                '2. A ocorrência e desenvolvimento de eventos por acaso de maneira feliz ou benéfica.',
                                '"um golpe afortunado de serendipidade"',
                                '3. A capacidade ou fenômeno de encontrar coisas valiosas ou agradáveis não procuradas.',
                                '"o elemento de serendipidade na invenção do raio X"']

def spans(word):
    if word == 'Accuse' or word == 'accuse':
        return 'Acusar' 
    if word == 'Affection' or word == 'affection':
        return  'Afeição' 
    if word == 'Alleviate' or word == 'alleviate':
        return 'Aliviar'
    if word == 'Celebration' or word == 'celebration':
        return 'Celebração'
    if word == 'Circulate' or word == 'circulate':
        return 'Circular'
    if word == 'Mastery' or word == 'mastery':
        return 'Domínio'  
    if word == 'Predicament' or word == 'predicament':
        return 'Dilema'
    if word == 'Serendipity' or word == 'serendipity':
        return 'Serendipidade'


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
