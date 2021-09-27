
import pickle
import pandas as pd

df = pd.read_excel("./Subject Information.xlsx", skiprows = 1, skipfooter = 7)
df.drop('Unnamed: 0',inplace = True, axis = 1)

dados = pickle.load(open('./dados.pickle', 'rb'))

print(dados)
# def ad_linha_coluna(df):
        
#     for x in range(len(dados)):
#         i = x * 5
#         dfA = df.iloc[:i, ]
#         dfB = df.iloc[i:, ]
#         d = {'Subject Code': [df['Subject Code'][i],df['Subject Code'][i], df['Subject Code'][i],df['Subject Code'][i]],
#              'Age': [df['Age'][i], df['Age'][i], df['Age'][i], df['Age'][i]],
#              'Gender': [df['Gender'][i], df['Gender'][i],df['Gender'][i], df['Gender'][i]],
#              'Mass (kg)': [df['Mass (kg)'][i], df['Mass (kg)'][i],df['Mass (kg)'][i],df['Mass (kg)'][i]],                                                              
#              'Height (m)':  [df['Height (m)'][i], df['Height (m)'][i], df['Height (m)'][i], df['Height (m)'][i]],
#              'Amputation Side': [df['Amputation Side'][i], df['Amputation Side'][i],df['Amputation Side'][i],df['Amputation Side'][i]],
#              'Reason for Amputation': [df['Reason for Amputation'][i], df['Reason for Amputation'][i], df['Reason for Amputation'][i],df['Reason for Amputation'][i]],
#              'Age of Amputation': [df['Age of Amputation'][i],df['Age of Amputation'][i],df['Age of Amputation'][i],df['Age of Amputation'][i]],
#              'K-Level':[df['K-Level'][i], df['K-Level'][i], df['K-Level'][i], df['K-Level'][i]],
#              'Knee Prosthesis': [df['Knee Prosthesis'][i], df['Knee Prosthesis'][i], df['Knee Prosthesis'][i], df['Knee Prosthesis'][i]],
#              'Foot Prosthesis': [df['Foot Prosthesis'][i], df['Foot Prosthesis'][i], df['Foot Prosthesis'][i], df['Foot Prosthesis'][i]],
#              'Socket Suspension':[df['Socket Suspension'][i], df['Socket Suspension'][i], df['Socket Suspension'][i], df['Socket Suspension'][i]],
#              'Treadmill Training?': [df['Treadmill Training?'][i], df['Treadmill Training?'][i], df['Treadmill Training?'][i], df['Treadmill Training?'][i]],
#              'Handrails?': [df['Handrails?'][i], df['Handrails?'][i],df['Handrails?'][i], df['Handrails?'][i]]
#              }
       
#         df_inserido = pd.DataFrame(data = d)
#         df = dfA.append(df_inserido).append(dfB).reset_index(drop = True)
    
#     velocidades = [] 
#     k_2 = ['speed_0p4','speed_0p5','speed_0p6', 'speed_0p7','speed_0p8']
#     k_3 = ['speed_0p6', 'speed_0p8', 'speed_1p0', 'speed_1p2','speed_1p4'] 
    
#     for i in range(18):
#         if df['K-Level'][i] == "K2":
#             for f in range(5):
#                 velocidades.append(k_2[f])
#         else:
#             for f in range(5):
#                 velocidades.append(k_3[f])  
                
#     df['Speed'] = velocidades
#     df.drop([9],axis = 0, inplace = True)
#     df.reset_index(drop = True,inplace = True)
#     return df

# df = ad_linha_coluna(df)
# df.to_csv('Tabela_com_velocidade.csv')


# def selecionar(df, Subject_Code = "todos", gender = "todos", speedx= "todos", kLevel= "todos") :

#     print("Subject Code: "+ Subject_Code)

#     queryexpression= " "

#     if Subject_Code != "todos" :
#         queryexpression = queryexpression + 'Subject Code == @Subject_Code &' 

#     if gender != "todos" :
#         queryexpression= queryexpression + 'Gender =='+ gender + '&'

#     if speedx != "todos" :
#         queryexpression= queryexpression + ' Speed =="'+ speedx + '" &'

#     elif kLevel == 'todos' :

#         if queryexpression[-1].find("&") == 0:
#             queryexpression= queryexpression[0:-1]

#     if kLevel != "todos" :
#         queryexpression= queryexpression + ' K-Level =="'+ kLevel +'"' 
    
#     else :
    
#         if queryexpression[-1].find("&") == 0:
#             queryexpression= queryexpression[0:-1]

#     if queryexpression == " ":
#         w= df 
        
#     else:
#         w= df.query(queryexpression)
    
#     print(queryexpression)
    
#     return w


# x = selecionar(df, Subject_Code = "TF10", gender = "todos", speedx= "speed_0p6", kLevel= "todos")
# print(x)
