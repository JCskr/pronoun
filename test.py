# more rule:
# 1). 与head是并列关系的词语
# action_word - '我', '想', '玩游戏' / '我', '想', '笑'
# another_pron - '你', '哥哥', '是', '谁' / '你', '哥', '是', '谁'


# sentence = '我不理你了你忘记我了'
# (['我', '不理', '你', '了', '你', '忘记', '我', '了'], '我主谓关系+核心关系你动宾关系-你主谓关系+我动宾关系-', '不理', '', '')
# {'pronoun_represent': '我主谓关系+核心关系你动宾关系-你主谓关系+我动宾关系-', 'head': '不理', 'another_pron': '', 'action_word': ''}
# sentence = '我不理你，你忘记我了'
# (['我', '不理', '你', '，', '你', '忘记', '我', '了'], '我主谓关系+核心关系你动宾关系-你主谓关系+我动宾关系-', '不理', '', '')
# {'pronoun_represent': '我主谓关系+核心关系你动宾关系-你主谓关系+我动宾关系-', 'head': '不理', 'another_pron': '', 'action_word': ''}


# sentence = '早餐我请你'
# (['早餐', '我', '请', '你'], '我主谓关系+核心关系你动宾关系-', '请', '', '')
# {'pronoun_represent': '我主谓关系+核心关系你动宾关系-', 'head': '请', 'another_pron': '', 'action_word': ''}
# sentence = '我请你吃早餐'
# (['我', '请', '你', '吃早餐'], '我主谓关系+核心关系你兼语-', '请', '', '吃早餐')
# {'pronoun_represent': '我主谓关系+核心关系你兼语-', 'head': '请', 'another_pron': '', 'action_word': '吃早餐'}

# sentence = '我是开玩笑的'
sentence = '我是在和你开玩笑'
# sentence = '我是和你开玩笑'
# 1	我	我	r	r	_	2	主谓关系	_	_
# 2	是	是	v	v	_	0	核心关系	_	_
# 3	和	和	p	p	_	5	状中结构	_	_
# 4	你	你	r	r	_	3	介宾关系	_	_
# 5	开玩笑	开玩笑	v	v	_	2	动宾关系	_	_
#
# (['我', '是', '和', '你', '开玩笑'], '我主谓关系+核心关系你介宾关系-', '是', '', '开玩笑')
# {'pronoun_represent': '我主谓关系+核心关系你介宾关系-', 'head': '是', 'another_pron': '', 'action_word': '开玩笑'}
# sentence = '我和你开玩笑的呢'
# 1	我	我	r	r	_	4	主谓关系	_	_
# 2	和	和	c	c	_	4	状中结构	_	_
# 3	你	你	r	r	_	2	介宾关系	_	_
# 4	开玩笑	开玩笑	v	v	_	0	核心关系	_	_
# 5	的	的	u	u	_	4	右附加关系	_	_
# 6	呢	呢	e	y	_	4	右附加关系	_	_
#
# (['我', '和', '你', '开玩笑', '的', '呢'], '我主谓关系+你介宾关系-核心关系', '开玩笑', '', '')
# {'pronoun_represent': '我主谓关系+你介宾关系-核心关系', 'head': '开玩笑', 'another_pron': '', 'action_word': ''}

from pyhanlp import HanLP
result = HanLP.parseDependency(sentence)
print(result)


from pronounMatch import hannlp_parse,pronoun_extract
print(hannlp_parse(sentence))
print(pronoun_extract.extract(sentence))


# from pronounMatch import PronounMatch
# file_path = 'D:\\pronounMatch\\pronoun_dependency_rule.txt'
# pronounmatch = PronounMatch(file_path)
# print('+' + str(pronounmatch.match(sentence)) + '+')


# assert 'rule_0' in pronounmatch.match('你喜欢什么?')['more_pronoun'].keys()
#
# assert 'rule_1' in pronounmatch.match('你喜欢我?')['more_pronoun'].keys()
# assert 'rule_1' in pronounmatch.match('你可以撩我吗?')['more_pronoun'].keys()
#
#
# assert 'rule_2' in pronounmatch.match('我猜你是男的')['more_pronoun'].keys()
# assert 'rule_2' in pronounmatch.match('你知道我是谁吗')['more_pronoun'].keys()
# assert 'rule_2' in pronounmatch.match('你猜我要去哪里')['more_pronoun'].keys()
# assert 'rule_2' in pronounmatch.match('你知道我是男还是女')['more_pronoun'].keys()
#
#
# assert 'rule_3' in pronounmatch.match('你给我买吃的')['more_pronoun'].keys()
# assert 'rule_3' in pronounmatch.match('你和我一起去北京')['more_pronoun'].keys()
#
#
# assert 'rule_4' in pronounmatch.match('你知道我老板')['more_pronoun'].keys()


