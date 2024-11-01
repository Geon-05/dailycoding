import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

# 준비하기. import library

import streamlit as st
import torch
import torch.nn as nn
import torch.optim as optim
import re

# 1. 데이터셋만들기 / 불러오기
st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")

# 제목 및 설명
st.title('딥러닝 스타터')
st.text('1. 데이터셋 만들기 / 불러오기')
st.code('''
sentence = """
In the heart of a bustling city, where skyscrapers tower above and
people from all walks of life converge, there exists a small, unassuming
coffee shop that has become a beloved sanctuary for artists, writers, and
thinkers alike; a place where time seems to slow down, and the aroma of freshly
brewed coffee mingles with the gentle hum of conversation, inviting patrons
to linger a little longer, lost in thought or inspiration, while outside,
the world continues at its relentless pace, oblivious to the quiet magic brewing within.
"""

# 테스트 텍스트
"""
안녕하세요. 반갑습니다. 전처리가 확실하게 되었는지 확인해 볼까요?
"""
        ''',
        language='python')

# 데이터 입력
sentence_user = st.text_area('데이터를 입력하세요.')
sentence_user = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", sentence_user)
sentence_user = sentence_user.split()
st.text(f'전처리 후 테스트용 샘플의 개수 : {len(sentence_user)}')
st.text(sentence_user)

# 사전 생성
vocab = list(set(sentence_user))
word2index = {tkn: i for i, tkn in enumerate(vocab, 1)}
word2index['<unk>'] = 0

# 수치화된 데이터를 단어로 바꾸기 위한 사전
index2word = {v: k for k, v in word2index.items()}

# 데이터 변환
def build_data(sentence, word2index):
    encoded = [word2index.get(token, 0) for token in sentence]
    input_seq, label_seq = encoded[:-1], encoded[1:]
    input_seq = torch.LongTensor(input_seq).unsqueeze(0)
    label_seq = torch.LongTensor(label_seq).unsqueeze(0)
    return input_seq, label_seq

X, Y = build_data(sentence_user, word2index)

# 네트워크 클래스 정의
class Net(nn.Module):
    def __init__(self, vocab_size, input_size, hidden_size, batch_first=True):
        super(Net, self).__init__()
        self.embedding_layer = nn.Embedding(num_embeddings=vocab_size, embedding_dim=input_size)
        self.rnn_layer = nn.RNN(input_size, hidden_size, batch_first=batch_first)
        self.linear = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        output = self.embedding_layer(x)
        output, hidden = self.rnn_layer(output)
        output = self.linear(output)
        return output.view(-1, output.size(2))

# 하이퍼 파라미터 설정
vocab_size = len(word2index)
input_size = st.text_input('input_size 입력', max_chars=5, placeholder='input_size')
hidden_size = st.text_input('hidden_size 입력', max_chars=5, placeholder='hidden_size')
input_size = int(input_size) if input_size else 10
hidden_size = int(hidden_size) if hidden_size else 20

# 모델 생성 및 학습 설정
model = None
if st.button('입력'):
    st.text('모델을 생성합니다.')
    model = Net(vocab_size, input_size, hidden_size, batch_first=True)
    loss_function = nn.CrossEntropyLoss()
    optimizer = optim.Adam(params=model.parameters())
    st.success("모델이 생성되었습니다.")

# 예측 버튼 기능
if st.button('예측'):
    if model is not None:
        st.text('임의예측을 시행합니다.')
        output = model(X)
        st.write("예측 결과 텐서:", output[0])
        st.write("예측 결과 개수:", len(output))
        st.write("예측 결과 형태:", output.shape)
    else:
        st.warning("먼저 모델을 생성하세요.")