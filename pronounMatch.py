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


def hannlp_parse(string):
    '''
    hannlp依存句法分析
    :param string:
    :return:
    '''

    result = HanLP.parseDependency(string)
    result = [ele.split("\t") for ele in str(result).strip().split("\n")]

    depend = []
    depend_loc = []
    fenci = []
    fenci_loc = []
    fenci_depend_loc = []
    postag = []
    for element in result:
        fenci.append(str(element[1]))
        fenci_loc.append(int(element[0]))
        postag.append(str(element[3]))
        depend.append((str(element[7])))
        depend_loc.append(int(element[6]))
        fenci_depend_loc.append((str(element[1]), int(element[6])))

    head_loc = depend.index('核心关系') + 1

    first_path = ''
    subject_word = ''
    subject_cnt = 0
    last_subject_loc = 0
    head_word = ''
    another_pron = ''
    another_pron_relate = ''
    action_word = ''
    for element in result:
        if int(element[0]) < int(element[6]):
            direction = '+'
        else:
            direction = '-'

        # path - sv
        if str(element[7]) in ['主谓关系','核心关系']:
            first_path += str(element[1]) + direction

            if str(element[7]) == '主谓关系':
                subject_word += str(element[1])
                subject_cnt += 1
                last_subject_loc = int(element[0]) - 1

            if str(element[7]) == '核心关系':
                head_word = str(element[1])

        # word -
        if str(element[1]) in fir_sec_pronouns and str(element[7]) not in ['主谓关系']:
            another_pron += str(element[1])
            another_pron_relate += str(element[7])

        # word -
        if str(element[7]) == '动宾关系' and str(element[3]) not in ['r'] and head_loc == int(element[6]):
            action_word = str(element[1])

    # 一个句子多个主谓关系，只保留最后一个主谓关系
    if subject_cnt > 1:
        return hannlp_parse(''.join(fenci[last_subject_loc:]))

    represent = {'f1':first_path}
    core_word = {'subject_word':subject_word, 'head_word':head_word,
                 'another_pron':another_pron, 'another_pron_relate':another_pron_relate,
                 'action_word':action_word}
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
            return {'third_person': fenci[fenci.index(list(third_)[0])]}

        # 第一人称和第二人称
        fir_sec = set.intersection(set(fenci), set(self.fir_sec_pronouns))
        if len(fir_sec):
            return {'represent': represent,
                    'core_word': core_word}

        no_pronoun = set.intersection(set(fenci), set(self.fir_sec_pronouns + self.third_pronouns))
        if no_pronoun:
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

        matchscore = 0
        if pronoun_sent1 and pronoun_sent2:
            if pronoun_sent1.get('represent') and pronoun_sent2.get('represent'):
                rule1 = pronoun_sent1.get('represent').get('f1')
                rule2 = pronoun_sent2.get('represent').get('f1')
                subject_word1 = pronoun_sent1.get('core_word').get('subject_word')
                subject_word2 = pronoun_sent2.get('core_word').get('subject_word')
                head_word1 = pronoun_sent1.get('core_word').get('head_word')
                head_word2 = pronoun_sent2.get('core_word').get('head_word')
                another_pron1 = pronoun_sent1.get('core_word').get('another_pron')
                another_pron2 = pronoun_sent2.get('core_word').get('another_pron')
                another_pron_relate1 = pronoun_sent1.get('core_word').get('another_pron_relate')
                another_pron_relate2 = pronoun_sent1.get('core_word').get('another_pron_relate')

                action_word1 = pronoun_sent1.get('core_word').get('action_word')
                action_word2 = pronoun_sent2.get('core_word').get('action_word')

                main_subject = subject_word1
                if rule1 == rule2:
                    matchscore += 200

                if subject_word1 != subject_word2:
                    if subject_word1 in self.topic_model and subject_word2 in self.topic_model and self.topic_model.similarity(subject_word1, subject_word2) > 0.6:
                        matchscore += 100
                    else:
                        if fuzz.ratio(subject_word1, subject_word2) > 50:
                            matchscore += 100
                        else:
                            return (sent2, 0)

                if head_word1 != head_word2:
                    if head_word1 in self.topic_model and head_word2 in self.topic_model and self.topic_model.similarity(head_word1, head_word2) > 0.6:
                        matchscore += 100
                    else:
                        if fuzz.ratio(head_word1, head_word2) > 60:
                            matchscore += 100
                        else:
                            return (sent2, 0)

                if matchscore >= 200:
                    if another_pron1 and another_pron2:

                        if another_pron1 == another_pron2:
                            matchscore += 50
                            if another_pron_relate1 == another_pron_relate2:
                                matchscore += 50
                        else:
                            # 如果主语不是代词，而且其他代词没有匹配上，则认为两者不匹配。 - 即在主语不是代词的情况下，其他代词非常重要。
                            if not main_subject or main_subject not in self.all_pronouns:
                                return (sent2, 0)

                    if action_word1 and action_word2:
                        if action_word1 == action_word2:
                            matchscore +=100
                        else:
                            if fuzz.ratio(action_word1, action_word2) > 0:
                                matchscore += 50
                            else:
                                return (sent2, 0)
                else:
                    return (sent2, 0)

        return (sent2, matchscore)

