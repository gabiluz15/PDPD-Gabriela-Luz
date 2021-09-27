import scipy.io as sp
import pickle

dado = dict()

dado[1] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF01/Matlab Workspace/TF01_DATA.mat') 
dado[2] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF02/Matlab Workspace/TF02_DATA.mat')
dado[3] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF05/Matlab Workspace/TF05_DATA.mat')
dado[4] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF06/Matlab Workspace/TF06_DATA.mat')
dado[5] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF07/Matlab Workspace/TF07_DATA.mat')
dado[6] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF08/Matlab Workspace/TF08_DATA.mat')
dado[7] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF09/Matlab Workspace/TF09_DATA.mat')
dado[8] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF10/Matlab Workspace/TF10_DATA.mat')
dado[9] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF11/Matlab Workspace/TF11_DATA.mat')
dado[10] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF12/Matlab Workspace/TF12_DATA.mat')
dado[11] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF13/Matlab Workspace/TF13_DATA.mat')
dado[12] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF14/Matlab Workspace/TF14_DATA.mat')
dado[13] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF15/Matlab Workspace/TF15_DATA.mat')
dado[14] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF16/Matlab Workspace/TF16_DATA.mat')
dado[15] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF17/Matlab Workspace/TF17_DATA.mat')
dado[16] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF18/Matlab Workspace/TF18_DATA.mat')
dado[17] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF19/Matlab Workspace/TF19_DATA.mat')
dado[18] = sp.loadmat('C:/Users/name/Desktop/UFABC/Programação/dadosPDPD/dadosPDPD/TF20/Matlab Workspace/TF20_DATA.mat')

file_to_write = open("dados.pickle", "wb")
pickle.dump(dado, file_to_write)

