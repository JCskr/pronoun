import regex as re
from fuzzywuzzy import fuzz
from pyhanlp import HanLP

first_person = ["我"]

first_person_collection = ["我们"]

second_person = ["你"]

second_person_collection = ["你们"]

third_person = ["他",
                "她"]

third_person_collection = ["他们",
                           "她们"]

fir_sec_pronouns = first_person + first_person_collection + second_person + second_person_collection
third_pronouns = third_person + third_person_collection
all_pronouns = fir_sec_pronouns + third_pronouns


def hannlp_parse(string):
    '''
    hannlp依存句法分析
    :param string:
    :return:
    '''

    result = HanLP.parseDependency(string)
    result = [ele.split("\t") for ele in str(result).strip().split("\n")]

    fenci = []
    first_path = ''
    prons = ''
    pron_cnt = 0
    words = []
    for element in result:
        fenci.append(str(element[1]))

        if int(element[0]) < int(element[6]):
            direction = '+'
        else:
            direction = '-'

        if str(element[7]) not in ['左附加关系', '右附加关系','标点符号']:
            first_path += str(element[7]) + direction

            # cnt -
            if str(element[1]) in all_pronouns:
                prons += str(element[1])
                pron_cnt += 1
            else:
                words.append(str(element[1]))

    represent = {'f1': first_path}
    core_word = {'words':words,'prons':prons,'pron_cnt': pron_cnt}
    return fenci, represent, core_word


class PronounExtract(object):

    def __init__(self):
        self.fir_sec_pronouns = fir_sec_pronouns
        self.third_pronouns = third_pronouns

    def extract(self, orig_sent):
        '''
        匹配代词
        :param sentence:
        :return:
        '''
        fenci, represent, core_word = hannlp_parse(orig_sent)

        # 第三人称
        third_ = set.intersection(set(fenci), set(self.third_pronouns))
        if len(third_):
            return {'third_person': fenci[fenci.index(list(third_)[0])],
                    'core_word': core_word}

        # 第一人称和第二人称
        fir_sec = set.intersection(set(fenci), set(self.fir_sec_pronouns))
        if len(fir_sec):
            return {'represent': represent,
                    'core_word': core_word}

        no_pronoun = set.intersection(set(fenci), set(self.fir_sec_pronouns + self.third_pronouns))
        if not no_pronoun:
            return


pronoun_extract = PronounExtract()


class PronounMatch(object):

    def __init__(self, topic_model):
        self.topic_model = topic_model
        self.all_pronouns = fir_sec_pronouns + third_pronouns

    def match_score(self, sent1, sent2):
        '''
        :param sent1:
        :param sent2:
        :return:
        '''
        pronoun_sent1 = pronoun_extract.extract(sent1)
        pronoun_sent2 = pronoun_extract.extract(sent2)

        matchscore = 1
        if pronoun_sent1 and pronoun_sent2:
            if pronoun_sent1.get('represent') and pronoun_sent2.get('represent'):
                rule1 = pronoun_sent1.get('represent').get('f1')
                rule2 = pronoun_sent2.get('represent').get('f1')
                words1 = pronoun_sent1.get('core_word').get('words')
                words2 = pronoun_sent2.get('core_word').get('words')
                prons1 = pronoun_sent1.get('core_word').get('prons')
                prons2 = pronoun_sent2.get('core_word').get('prons')

                if rule1 == rule2:
                    if prons1 != prons2:
                        matchscore = 0
                    else:
                        value_ = len(words1)
                        for i,j in zip(words1,words2):
                            if i in self.topic_model and j in self.topic_model and self.topic_model.similarity(
                            i, j) < 0.4:
                                value_ -= 1
                            elif fuzz.ratio(i, j) < 50:
                                value_ -= 1
                        if value_ < len(words1):
                            matchscore = 0

        return (matchscore, sent2)

