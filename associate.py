# -*- coding: utf-8 -*-
import os
import pymorphy2 as pm
import warnings
import gensim
from gensim.test.utils import datapath
from semantic import getWordWithTag

warnings.filterwarnings('ignore')

directory = os.path.dirname(__file__)
model = gensim.models.KeyedVectors.load_word2vec_format(datapath(directory + '/model.bin'), binary=True)

m = pm.MorphAnalyzer()


# возвращает список пар <слово_тег, косинусная близость>
def getAssociate(word):
    res = ''
    if word == '':
        return res

    lemma = getWordWithTag(word.lower(), m)
    try:
        res = '['
        for x in model.most_similar(positive=lemma):
            res += '{"word": "' + x[0].split('_')[0] + '", "cos":' + str(x[1]) + '},\n'
        res = res[0: len(res) - 2] + ']'
    except Exception:
        res = '{error: "notFound"}'
    return res
