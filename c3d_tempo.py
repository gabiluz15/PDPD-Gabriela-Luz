from ezc3d import c3d
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = os.listdir('./ViconWorkspace5/')
trials= []
for file in files:
    if file[-3:] == "c3d" and file[0] in '01tT':
        #print(file)
        c = c3d('./ViconWorkspace5/'+file)
        trials.append(c)

c=trials[-1]
df = pd.read_csv("./Tabela_com_velocidade.csv")
#c3d("./Vicon1/"+files[0])

#print(c['parameters']['POINT']['USED']['value'][0]);  # Print the number of points used
point_data = c['data']['points']
points_residuals = c['data']['meta_points']['residuals']
analog_data = c['data']['analogs']
meta_points = c['data']['meta_points']
perna = c['parameters']['EVENT']['CONTEXTS']['value']
instantes = c['parameters']['EVENT']['TIMES']['value'][1,:]
eventos = c['parameters']['EVENT']['DESCRIPTIONS']['value']



def calcula_tempo():
    
    tempo_r = 0
    tempo_l = 0
    n = -1
    i = 0
    
    while i < len(instantes)/2: 
        n += 2
        tempo_r += instantes[n]-instantes[n-1]
        i += 2
        
    while n < len(instantes):
        tempo_l += instantes[n]-instantes[n-1]
        n += 2     
        
    print('tempo_r =', tempo_r,'\ntempo_l =', tempo_l)
n=len(eventos)//2
direita_event = np.array(eventos[:n])
direita_inst = instantes[:n]
esquerda_event = np.array(eventos[n:])
esquerda_inst = instantes[n:] 

def retira_dado(direita_event,direita_inst,esquerda_event,esquerda_inst):
    
    if direita_event[0] == 'The instant the toe leaves the ground':
        direita_event = direita_event[1:]
        direita_inst = direita_inst[1:]
    if direita_event[-1] == 'The instant the heel strikes the ground':
        direita_event = direita_event[:-1]
        direita_inst = direita_inst[:-1]

    if esquerda_event[0] == 'The instant the toe leaves the ground':
        esquerda_event = esquerda_event[1:]
        esquerda_inst = esquerda_inst[1:]
    if esquerda_event[-1] == 'The instant the heel strikes the ground':
        esquerda_event = esquerda_event[:-1]
        esquerda_inst = esquerda_inst[:-1]
        
    return esquerda_inst, esquerda_event ,direita_inst,direita_event

def organiza_dado(esquerda_inst,direita_inst,esquerda_event,direita_event):
    
    esquerda_index = np.argsort(esquerda_inst, axis=- 1, kind=None, order=None)
    esquerda_inst = esquerda_inst[esquerda_index]
    esquerda_event = esquerda_event[esquerda_index]
    
    dir_index = np.argsort(direita_inst, axis=- 1, kind=None, order=None)
    direita_inst = direita_inst[dir_index]
    direita_event = direita_event[dir_index]
    return esquerda_inst, esquerda_event ,direita_inst,direita_event

def adicionar_colunas(df,tempoE,tempoD):
    a =np.arange(0,89)
    df['d_trial1']= tempoD
    df['d_trial2']= a
    df['d_trial3']= a
    df['d_trial4']= a
    df["media_dir"] = a
    
    df['e_trial1']= tempoE
    df['e_trial2']= a
    df['e_trial3']= a
    df['e_trial4']= a
    df["media_esq"] = a
    
    df.reset_index(drop = True,inplace = True)
    return df

def soma_tempo(inst_e,inst_d):
    i=0
    tempoE=0
    while i < len(inst_e):
        tempoE += inst_e[i+1]-inst_e[i]
        i += 2
    i = 0
    tempoD=0
    while i < len(inst_d):
        tempoD += inst_d[i+1]-inst_d[i] 
        i += 2
    
    return tempoE,tempoD



inst_e,event_e,inst_d,event_d = organiza_dado(esquerda_inst,direita_inst,esquerda_event,direita_event)

inst_e,event_e,inst_d,event_d = retira_dado(event_d, inst_d, event_e, inst_e)

tempoE,tempoD = soma_tempo(inst_e,inst_d)

dfnovo = adicionar_colunas(df, tempoE,tempoD)

#plt.plot(point_data[0,:])
    