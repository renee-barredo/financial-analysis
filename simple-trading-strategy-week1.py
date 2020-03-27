import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ms = pd.DataFrame.from_csv('data/microsoft.csv')
ms['MA10']=ms['Close'].rolling(10).mean()
ms['MA50']=ms['Close'].rolling(50).mean()
ms = ms.dropna()
ms.head()

ms['Shares'] = [1 if ms.loc[ei,'MA10']> ms.loc[ei,'MA50'] else 0 for ei in
                ms.index]
ms['Close1'] = ms['Close'].shift(-1)
ms['Profit'] = [ms.loc[ei,'Close1'] - ms.loc[ei,'Close'] if 
                ms.loc[ei,'Shares'] == 1 else 0 for ei in ms.index]
ms['Profit'].plot()

ms['wealth'] = ms['Profit'].cumsum()
ms.tail

ms['wealth'].plot()
