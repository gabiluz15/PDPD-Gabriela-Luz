from ezc3d import c3d
import os
import pandas as pd
import numpy as np
import scipy
from scipy import stats

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

def adicionar_colunas(df, dfmean, part):
    a =np.arange(0,89)
    indices = np.where(df['Subject Code']==part)[0]
    #indices  = indices[:3]
    print(indices)
    print(dfmean['tempo_dir'].values)
  
    df.loc[indices,"media_dir"] = dfmean['tempo_dir'].values
  
    df.loc[indices,"media_esq"] = dfmean['tempo_esq'].values
    
    df.reset_index(drop = True,inplace = True)
    return df

def soma_tempo(inst_e,inst_d,event_e,event_d):

    
    for i in range(len(event_e)-1):
        if len(event_e[i]) != len(event_e[i+1]):
            if len(event_d[i]) != len(event_d[i+1]):
                if len(inst_e) %2 == 0 and len(inst_d) %2 == 0:
                    tempoE=0
                    j=0
                    while j < len(inst_e):
                        tempoE += inst_e[j+1] - inst_e[j]
                        j += 2
                    j = 0
                    tempoD=0
                    j=0
                    while j < len(inst_d):
                        tempoD += inst_d[j+1] - inst_d[j]
                        j += 2
                
                    return tempoE/(len(inst_e)/2),tempoD/(len(inst_d)/2)
                else:
                    return 0,0
            return 0,0
        return 0,0


files = os.listdir('./passando/TF20/Vicon Workspace/')

tempodir = []
tempoesq=[]
eventodir =[]
eventoesq=[]
velocity = []
df = pd.read_csv("./passando/Df_novoFinal.csv")



for file in files:
    if file[-3:] == "c3d" and file[0] in '01tT':
        print(file)
        c = c3d('./passando/TF20/Vicon Workspace/'+file)
        
        
        
        point_data = c['data']['points']
        points_residuals = c['data']['meta_points']['residuals']
        analog_data = c['data']['analogs']
        meta_points = c['data']['meta_points']
        perna = c['parameters']['EVENT']['CONTEXTS']['value']
        instantes = c['parameters']['EVENT']['TIMES']['value'][1,:]
        eventos = c['parameters']['EVENT']['DESCRIPTIONS']['value']
        
        n=len(eventos)//2
        direita_event = np.array(eventos[:n])
        direita_inst = instantes[:n]
        esquerda_event = np.array(eventos[n:])
        esquerda_inst = instantes[n:] 
        
        # adicionar_colunas(df)
        
        inst_e,event_e,inst_d,event_d = organiza_dado(esquerda_inst,direita_inst,esquerda_event,direita_event)
        
        inst_e,event_e,inst_d,event_d = retira_dado(event_d, inst_d, event_e, inst_e)
        
        tempoE,tempoD = soma_tempo(inst_e,inst_d,event_e,event_d)
        
        tempodir.append(tempoD)
        tempoesq.append(tempoE)
        
        velocity.append(file[:-7])
        

listadir = []
listaesq = []
vel = []
for i  in range(len(tempodir)):
    if tempodir[i] != 0:
        listadir.append(tempodir[i])
        listaesq.append(tempoesq[i])
        vel.append(velocity[i])
        
T = stats.ttest_rel(listadir, listaesq, axis=0, nan_policy='propagate', alternative='two-sided')
listaT = []
listaClass = []
for i in range(len(tempodir)):
    listaT.append(T[1])
    if T[1] >= 0.05:
        listaClass.append("Igual")
    else:
        listaClass.append("Diferente")
    
    
dftempos = pd.DataFrame({'velocidade':vel, 'tempo_dir':listadir, 'tempo_esq':listaesq})
dfmean = dftempos.groupby('velocidade').mean()

#df['Speed'] = df['Speed'].str.split('_').str.get(1)
part = 'TF20'
dfnovo = adicionar_colunas(df, dfmean, part)


# se menor 0.05, é diferente. Fazer coluna P


def adicionaP(part,df,listaT):
    indices = np.where(df['Subject Code']==part)[0]
    #T = stats.ttest_rel(listadir, listaesq, axis=0, nan_policy='propagate', alternative='two-sided')
    
    listaClass = []
    for i in range(len(listaT)):
        
        if listaT[i] >= 0.05:
            listaClass.append("Igual")
        else:
            listaClass.append("Diferente")
            
    df.loc[indices,"P"] = listaT
    df.loc[indices,"Classificação"] = listaClass
    
    df.reset_index(drop = True,inplace = True)
    
    return df
    

v = np.unique(vel)
listaT =[]
for z in range(len(v)):
    tempoDireita = dftempos.query("velocidade == @v[@z]")['tempo_dir']
    tempoEsquerda = dftempos.query("velocidade == @v[@z]")['tempo_esq']
    T = stats.ttest_rel(tempoDireita.values, tempoEsquerda.values, axis=0, nan_policy='propagate', alternative='two-sided')
    listaT.append(T[1])

dfnovo = adicionaP(part,df,listaT)

for i in dfnovo:
    if "Unnamed" in i:
        df.drop(columns=[i],inplace=True)
#df.drop(index = 82, inplace = True)  
dfnovo.to_csv("./passando/Df_novoFinal.csv")




