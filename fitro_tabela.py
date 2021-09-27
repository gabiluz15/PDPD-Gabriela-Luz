import pickle
import pandas as pd
import numpy as np

df = pd.read_excel("./Subject Information.xlsx", skiprows = 1, skipfooter = 7)
df.drop('Unnamed: 0',inplace = True, axis = 1)

# dados = pickle.load(open('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dados.pickle', 'rb'))

def ad_linha_coluna(df):
        
    for x in range(len(df)):
        
        i = x * 5
        dfA = df.iloc[:i, ]
        dfB = df.iloc[i:, ]
        d = {'Subject Code': [df['Subject Code'][i],df['Subject Code'][i], df['Subject Code'][i],df['Subject Code'][i]],
              'Age': [df['Age'][i], df['Age'][i], df['Age'][i], df['Age'][i]],
              'Gender': [df['Gender'][i], df['Gender'][i],df['Gender'][i], df['Gender'][i]],
              'Mass (kg)': [df['Mass (kg)'][i], df['Mass (kg)'][i],df['Mass (kg)'][i],df['Mass (kg)'][i]],                                                              
              'Height (m)':  [df['Height (m)'][i], df['Height (m)'][i], df['Height (m)'][i], df['Height (m)'][i]],
              'Amputation Side': [df['Amputation Side'][i], df['Amputation Side'][i],df['Amputation Side'][i],df['Amputation Side'][i]],
              'Reason for Amputation': [df['Reason for Amputation'][i], df['Reason for Amputation'][i], df['Reason for Amputation'][i],df['Reason for Amputation'][i]],
              'Age of Amputation': [df['Age of Amputation'][i],df['Age of Amputation'][i],df['Age of Amputation'][i],df['Age of Amputation'][i]],
              'K-Level':[df['K-Level'][i], df['K-Level'][i], df['K-Level'][i], df['K-Level'][i]],
              'Knee Prosthesis': [df['Knee Prosthesis'][i], df['Knee Prosthesis'][i], df['Knee Prosthesis'][i], df['Knee Prosthesis'][i]],
              'Foot Prosthesis': [df['Foot Prosthesis'][i], df['Foot Prosthesis'][i], df['Foot Prosthesis'][i], df['Foot Prosthesis'][i]],
              'Socket Suspension':[df['Socket Suspension'][i], df['Socket Suspension'][i], df['Socket Suspension'][i], df['Socket Suspension'][i]],
              'Treadmill Training?': [df['Treadmill Training?'][i], df['Treadmill Training?'][i], df['Treadmill Training?'][i], df['Treadmill Training?'][i]],
              'Handrails?': [df['Handrails?'][i], df['Handrails?'][i],df['Handrails?'][i], df['Handrails?'][i]]
              }
       
        df_inserido = pd.DataFrame(data = d)
        df = dfA.append(df_inserido).append(dfB).reset_index(drop = True)
    
    velocidades = [] 
    k_2 = ['speed_0p4','speed_0p5','speed_0p6', 'speed_0p7','speed_0p8']
    k_3 = ['speed_0p6', 'speed_0p8', 'speed_1p0', 'speed_1p2','speed_1p4'] 
    
    for i in range(len(df)):
        if df['K-Level'][i] == "K2":
            velocidades.append(k_2[i%5])
        else:
            velocidades.append(k_3[i%5])  
                
    df['Speed'] = velocidades
    df.drop([9],axis = 0, inplace = True)
    df.reset_index(drop = True,inplace = True)
    return df

df = ad_linha_coluna(df)
df.to_csv('Tabela_com_velocidade.csv')


def selecionar(df, Subject_Code = "todos", age = "todos", gender = "todos", mass = "todos", 
                height = "todos", side = "todos", reason = "todos", age_amp = "todos",
                knee  = "todos", foot = "todos", socket = "todos", treadmill = "todos",
                handrails = "todos", speedx= "todos", kLevel= "todos") :

    print("Subject Code: "+ Subject_Code)

    queryexpression= " "

    if Subject_Code != "todos" :
        queryexpression = queryexpression + '`Subject Code` == @Subject_Code &' 

    if age != "todos" :
        queryexpression= queryexpression + '`Age` == @age &'

    if gender != "todos" :
        queryexpression= queryexpression + 'Gender == @gender &'
    
    if mass != "todos" :
        queryexpression= queryexpression + '`Mass (kg)` == @mass &'    

    if height != "todos" :
        queryexpression= queryexpression + '`Height (m)` == @height &'
    
    if side != "todos" :
        queryexpression= queryexpression + '`Amputation Side` == @side &'
        
    if reason != "todos" :
        queryexpression= queryexpression + '`Reason for Amputation` == @reason &'
        
    if age_amp != "todos" :
        queryexpression= queryexpression + '`Age of Amputation` == @age_amp &'
    
    if knee != "todos" :
        queryexpression= queryexpression + '`Knee Prosthesis` == @knee &'
        
    if foot != "todos" :
        queryexpression= queryexpression + '`Foot Prosthesis` == @foot &'

    if socket != "todos" :
        queryexpression= queryexpression + '`Socket Suspension` == @socket &'

    if treadmill != "todos" :
        queryexpression= queryexpression + '`Treadmill Training?` == @treadmill &'

    if handrails != "todos" :
        queryexpression= queryexpression + '`Handrails?` == @handrails &'

    if speedx != "todos" :
        queryexpression= queryexpression + ' Speed == @speedx  &'

    elif kLevel == 'todos':

        if queryexpression[-1].find("&") == 0:
            queryexpression= queryexpression[0:-1]

    if kLevel != "todos" :
        queryexpression= queryexpression + ' `K-Level` == @kLevel ' 
    
    else :
    
        if queryexpression[-1].find("&") == 0:
            queryexpression= queryexpression[0:-1]
    print(queryexpression)
    if queryexpression == " ":
        w= df         
    else:
        w= df.query(queryexpression)
    
    
    return w

x = selecionar(df, speedx= "speed_0p6", kLevel= "K2",handrails ="No")
print(x)
