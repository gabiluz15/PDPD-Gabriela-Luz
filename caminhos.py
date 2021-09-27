import pickle
import matplotlib.pyplot as plt
import numpy as np

dados = pickle.load(open('./dados.pickle', 'rb'))

TF01 = dados[1]['TF01'][0,0] 

info = dados[2]['TF02']['info']

data = TF01['data']

speed1 = dados[1]['TF01'][0,0]['data']['speed_0p6'] 

moment= dados[1]['TF01'][0,0]['data']['speed_0p6'][0][0]['ipsilateral'][0][0]['ankle'][0][0]['moment'][0][0]

raw = moment['raw'][0][0]

  


x = np.linspace(0,1,1001)

plt.figure()
plt.plot(x,raw)
plt.show()
