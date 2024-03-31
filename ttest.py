import sys
import spacy
from tqdm import tqdm as tq


spacy_en = spacy.load('en_core_web_sm')
#text = 'Geu Roo is a young autistic man. He works for his father’s business  \“Move To Heaven.\” Their job is to arrange items left by deceased people. One day, Geu Roo\'s own father dies. Geu Roo is left alone, but his uncle Sang Koo suddenly appears in front of him. Sang Koo is a cold man. He was a martial artist who fought in underground matches. He went to prison because of what happened at his fight. Sang Koo now becomes Geu Roo’s guardian. They run \“Move To Heaven\” together.'
text = 'Geu Roo is a young autistic man. '

# 1. "" 따옴표 ' 홀따옴표 파이썬 텍스트 인식 처리 


for token in spacy_en.tokenizer(text):
    print(text)        


#spaCy를 이용해 토큰화를 수행하면 기본적으로 토큰외에도 PoS(품사), lemma등의 정보를 알 수 있다.
for token in spacy_en.tokenizer(text):
    print(f"token: {token.text}, PoS: {token.pos_}, lemman: {token.lemma_}")