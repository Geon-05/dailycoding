import streamlit as st
import time
import numpy as np
from PIL import Image





import torch
import torch.nn as nn
import torch.optim as optim

# 1. 데이터셋만들기 / 불러오기

sentence = """
In the heart of a bustling city, where skyscrapers tower above and
people from all walks of life converge, there exists a small, unassuming
coffee shop that has become a beloved sanctuary for artists, writers, and
thinkers alike; a place where time seems to slow down, and the aroma of freshly
brewed coffee mingles with the gentle hum of conversation, inviting patrons
to linger a little longer, lost in thought or inspiration, while outside,
the world continues at its relentless pace, oblivious to the quiet magic brewing within.
"""

# 2. 데이터 전처리 / ',', '.' 등등 불필요요소를 제거한다.
sentence = sentence.lower().replace(',','').replace('.','').split()
print(len(sentence))



r = np.random.rand(10000)*3
theta = np.random.rand(10000)*2*np.pi
y = r.astype(int)
r = r * (np.cos(theta) + 1)
x1 = r * np.cos(theta)
x2 = r * np.sin(theta)
X = np.array([x1, x2]).T

train_X, train_y = X[:8000, :], y[:8000]
val_X, val_y = X[8000:9000, :], y[8000:9000]
test_X, test_y = X[9000:, :], y[9000:]

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1, 3, 1)
ax1.scatter(train_X[:, 0], train_X[:, 1], c=train_y, s=0.7)
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_title('Train Set Distribution')


ax2 = fig.add_subplot(1, 3, 2)
ax2.scatter(val_X[:, 0], val_X[:, 1], c=val_y)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_title('Validation Set Distribution')

ax3 = fig.add_subplot(1, 3, 3)
ax3.scatter(test_X[:, 0], test_X[:, 1], c=test_y)
ax3.set_xlabel('x1')
ax3.set_ylabel('x2')
ax3.set_title('Test Set Distribution')

plt.show()
