import numpy as np
import pandas as pd

HC_data = np.genfromtxt('all_HC.csv', delimiter=',')
HC_data = HC_data.reshape(-1,500)
HC_class = np.full((HC_data.shape[0], 1), 'HC')
HC_data = np.hstack((HC_data,HC_class))
print(HC_data.shape)
print(HC_data)


HO_data = np.genfromtxt('all_HO.csv', delimiter=',')
HO_data = HO_data.reshape(-1,500)
HO_class = np.full((HO_data.shape[0], 1), 'HO')
HO_data = np.hstack((HO_data,HO_class))
print(HO_data.shape)
print(HO_data)

WE_data = np.genfromtxt('all_WE.csv', delimiter=',')
WE_data = WE_data.reshape(-1,500)
WE_class = np.full((WE_data.shape[0], 1), 'WE')
WE_data = np.hstack((WE_data,WE_class))
print(WE_data.shape)
print(WE_data)

WF_data = np.genfromtxt('all_WF.csv', delimiter=',')
WF_data = WF_data.reshape(-1,500)
WF_class = np.full((WF_data.shape[0], 1), 'WF')
WF_data = np.hstack((WF_data,WF_class))
print(WF_data.shape)
print(WF_data)

dataset = np.vstack((HC_data,HO_data))
dataset = np.vstack((dataset,WE_data))
dataset = np.vstack((dataset,WF_data))
print(dataset.shape)
print(dataset)

dataset = pd.DataFrame(dataset)
