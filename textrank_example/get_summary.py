#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

global test_print
test_print=True
import codecs
import os
path1=os.path.abspath('.')   # the path of current file
#print(path1)
path2=os.path.abspath('..')  # the Upper path of current file
#print(path2)
import sys
sys.path.append(path2+str('\\')+str('textrank4zh'))
import TextRank4Keyword as TextRank4Keyword
import TextRank4Sentence as TextRank4Sentence

def get_summary(data,num,if_print):
    global test_print
    test_print=if_print

    text = data
    tr4w = TextRank4Keyword()
    final_data=[]

    tr4w.analyze(text=text, lower=True, window=2)  # py2: text-:utf8(str,unicode)，py3: utf8(bytes str)

    if (test_print):print('keywords：')
    for item in tr4w.get_keywords(20, word_min_len=1):
        if (test_print):print(item.word, item.weight)


    if (test_print):print('keyphrases：')
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
        if (test_print):print(phrase)

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')


    if (test_print):print('key_sentences：')
    for item in tr4s.get_key_sentences(num=num):
        if (test_print):print(item.index, item.weight, item.sentence)
        final_data.append(item.sentence)

    return final_data