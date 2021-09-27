import scipy.io as sp
import pickle

dado = dict()

dado['TF01'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF01/Matlab Workspace/TF01_DATA.mat') 
dado['TF02'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF02/Matlab Workspace/TF02_DATA.mat')
dado['TF05'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF05/Matlab Workspace/TF05_DATA.mat')
dado['TF06'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF06/Matlab Workspace/TF06_DATA.mat')
dado['TF07'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF07/Matlab Workspace/TF07_DATA.mat')
dado['TF08'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF08/Matlab Workspace/TF08_DATA.mat')
dado['TF09'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF09/Matlab Workspace/TF09_DATA.mat')
dado['TF10'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF10/Matlab Workspace/TF10_DATA.mat')
dado['TF11'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF11/Matlab Workspace/TF11_DATA.mat')
dado['TF12'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF12/Matlab Workspace/TF12_DATA.mat')
dado['TF13'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF13/Matlab Workspace/TF13_DATA.mat')
dado['TF14'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF14/Matlab Workspace/TF14_DATA.mat')
dado['TF15'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF15/Matlab Workspace/TF15_DATA.mat')
dado['TF16'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF16/Matlab Workspace/TF16_DATA.mat')
dado['TF17'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF17/Matlab Workspace/TF17_DATA.mat')
dado['TF18'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF18/Matlab Workspace/TF18_DATA.mat')
dado['TF19'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF19/Matlab Workspace/TF19_DATA.mat')
dado['TF20'] = sp.loadmat('C:/Users/gabri/OneDrive/Documentos/GitHub/PDPD-Gabriela/passando/TF20/Matlab Workspace/TF20_DATA.mat')

file_to_write = open("./dados2.pickle", "wb")
pickle.dump(dado, file_to_write)

