import time
from scipy import stats
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score
# 빅데이터 Format
# InvoiceNo : 6자리 숫자로 이루어진 거래 고유번호
#