import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import imdb


# 데이터 로드 (단어 인덱스 포함)
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# word_index는 단어를 정수 인덱스로 매핑한 딕셔너리
word_index = imdb.get_word_index()

# 인덱스:단어 매핑을 위한 딕셔너리 생성
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# 첫 번째 리뷰를 디코딩
decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

print(decoded_review)
