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
# sentence = '我是在和你开玩笑'
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

# sentence = '我女朋友贵姓'
# 1	我	我	r	r	_	2	定中关系	_	_
# 2	女朋友	女朋友	n	n	_	3	定中关系	_	_
# 3	贵姓	贵姓	n	n	_	0	核心关系	_	_
# sentence = '你女朋友贵姓'
# 1	你	你	r	r	_	2	定中关系	_	_
# 2	女朋友	女朋友	n	n	_	3	定中关系	_	_
# 3	贵姓	贵姓	n	n	_	0	核心关系	_	_

# sentence = '我的缺点是啥？'
# 1	我	我	r	r	_	3	定中关系	_	_
# 2	的	的	u	u	_	1	右附加关系	_	_
# 3	缺点	缺点	n	n	_	4	主谓关系	_	_
# 4	是	是	v	v	_	0	核心关系	_	_
# 5	啥	啥	r	r	_	4	动宾关系	_	_
# 6	？	？	wp	w	_	4	标点符号	_	_


# sentence = '我想我该去睡觉了'
# 1	我	我	r	r	_	2	主谓关系	_	_
# 2	想	想	v	v	_	0	核心关系	_	_
# 3	我	我	r	r	_	6	主谓关系	_	_
# 4	要	要	v	v	_	6	状中结构	_	_
# 5	去	去	v	v	_	6	状中结构	_	_
# 6	睡觉	睡觉	v	v	_	2	动宾关系	_	_
# 7	了	了	e	y	_	6	右附加关系	_	_

# sentence = '我想你应该去休息一下'

# sentence = '我想该去睡觉了'
sentence = '有你这句话我就放心了'
# 1	有	有	v	v	_	0	核心关系	_	_
# 2	你	你	r	r	_	4	定中关系	_	_
# 3	这	这	r	r	_	4	定中关系	_	_
# 4	句话	句话	q	q	_	1	动宾关系	_	_
# 5	我	我	r	r	_	7	主谓关系	_	_
# 6	就	就	d	d	_	7	状中结构	_	_
# 7	放心	放心	v	v	_	1	并列关系	_	_
# 8	了	了	e	y	_	7	右附加关系	_	_

sentence = '我说你干什么呢'
sentence = '你好你在干什么'


sentence = '我想去旅游，你呢？'

sentence = '那你知道我是谁吗？'

sentence = '小M，知道我是谁吗'

# sentence = '你知道我是谁吗？'

# sentence = '你觉得我是谁？'

# sentence = '知道我是谁吗'


sentence = '麻烦你帮我叫一辆出租车'
# 1	麻烦	麻烦	a	a	_	0	核心关系	_	_
# 2	你	你	r	r	_	3	主谓关系	_	_
# 3	帮	帮	v	v	_	1	并列关系	_	_
# 4	我	我	r	r	_	3	兼语	_	_
# 5	叫	叫	v	v	_	3	动宾关系	_	_
# 6	一辆	一辆	m	m	_	7	定中关系	_	_
# 7	出租车	出租车	n	n	_	5	动宾关系	_	_

sentence = '你帮我叫一辆出租车'

sentence = '你教我学一下韩语'
# sentence = '教我学一下韩语'

# sentence = '我该去睡觉了'
# 1	我	我	r	r	_	4	主谓关系	_	_
# 2	要	要	v	v	_	4	状中结构	_	_
# 3	去	去	v	v	_	4	状中结构	_	_
# 4	睡觉	睡觉	v	v	_	0	核心关系	_	_
# 5	了	了	e	y	_	4	右附加关系	_	_

sentence = '你没有弟弟吗？'

sentence = '你老婆呢'
sentence = '你知道我是谁吗'

sentence = '你是男还是女'

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


