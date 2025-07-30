import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Sunil M S\data.csv")
df
legend=['India','Pakistan']
plt.hist([df['score_india'],df['score_pk']],color=['blue','green'])
plt.legend(legend)
plt.xlabel('runs')
plt.ylabel('Frequency')
plt.title('Champions Trophy 2017' )
plt.show()
