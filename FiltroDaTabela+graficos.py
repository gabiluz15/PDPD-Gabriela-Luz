import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./Tabela_com_velocidade.csv")

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
    
    w.reset_index(inplace=True)
    return w

x = selecionar(df, Subject_Code='TF08')
print(x)
dados = pickle.load(open('./dados2.pickle', 'rb'))
#print(x.loc[0, 'Subject Code'])

moment = dados[x.loc[1, 'Subject Code']][x.loc[1, 'Subject Code']][0,0]['data'][x.loc[1, 'Speed']][0][0]['ipsilateral'][0][0]['ankle'][0][0]['moment'][0][0]


raw = moment['raw'][0][0]
x=np.arange(1001)
plt.figure()
plt.title("Ipsilateral ankle - moment(Nm/kg)")
plt.plot(x,raw)
plt.show()

avg = moment['avg'][0][0]
x=np.arange(1001)
plt.figure()
plt.plot(x,avg)
plt.title("Avarage of ipsilateral ankle - moment(Nm/kg)")
plt.show()

stdev = moment['stdev'][0][0]
x=np.arange(1001)
plt.figure()
plt.plot(x,stdev)
plt.show()