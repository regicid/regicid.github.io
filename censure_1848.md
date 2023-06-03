```python
import seaborn as sns
from pyllicagram.pyllicagram import *
import matplotlib.pyplot as plt
from matplotlib import dates
import numpy as np
a = pyllicagram("pas",debut=1846,fin=1854)

a["date"] = a.annee.astype("str") + "-" +a.mois.astype("str")
a["date2"] =dates.datestr2num(a.date)
a["Censure"] = a.annee > 1851

a.Censure[71] = True

sns.lmplot(a,x="date2",y="ratio",hue="Censure",ci=None,scatter_kws={"s": 5},legend=None)
plt.scatter(a.date2[25], max(a.ratio), c='red', marker='D', s=30,label="Février 1848")
plt.xticks(a.date2[::20],a.date[::20])
plt.plot([a.date2[71],a.date2[71]],[min(a.ratio),max(a.ratio)],":",color="black",label="Loi sur la presse")

L=plt.legend()
L.get_texts()[0].set_text('Avant censure')
L.get_texts()[1].set_text('Après censure')
plt.ylabel('Fréquence du mot "pas"')
plt.xlabel('Date')
```

    100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 10.72it/s]
    /var/folders/b2/ltxbgkps3p32wwrffpz_2mmr0000gp/T/ipykernel_13480/2351550475.py:12: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      a.Censure[71] = True





    Text(0.5, 28.999999999999986, 'Date')




    
![png](output_0_2.png)
    

