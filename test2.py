from pyhanlp import HanLP

# sentence = '你女朋友是什么名字'
# sentence = '你到底是男是女'
# from pyhanlp import HanLP
# result = HanLP.parseDependency(sentence)
# print(result)
#
# sentence = '我们是朋友吗'
# sentence = '你到底是男是女？'
# from pyhanlp import HanLP
# result = HanLP.parseDependency(sentence)
# print(result)
#
# sentence = '原来住在上海，现在住在北京'
# from pyhanlp import HanLP
# result = HanLP.parseDependency(sentence)
# print(result)
sentence = '这些都会是我的'
result = HanLP.parseDependency(sentence)
print(result)

sentence = '我的名字是什么'
result = HanLP.parseDependency(sentence)
print(result)


你的缺点是？
你的缺点是什么？
'什么','啥' - 可省略的部分？



# from pronoun_filter import pronoun_extract
# # sentence = ''
# # print(pronoun_extract.extract(sentence))
#
# sentence = '谁造出你的'
# print(pronoun_extract.extract(sentence))

