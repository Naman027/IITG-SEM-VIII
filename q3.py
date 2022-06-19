import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv("Merck.txt", sep="\s+", header=None)
df.rename(columns={0:'date',
                   1:'simple'}, inplace=True)
df['log'] = np.log(1+df['simple'])

temp = df['log'].shift(periods=1)
df['two-step-log'] = df['log']+temp.fillna(0)
temp = df['simple'].shift(periods=1)
df['two-step-simple'] = (df['simple']+1)*(temp.fillna(0)+1)-1
df.iloc[0, 4] = 0
df.iloc[0, 3] = 0

alpha = 0.05
z_value=stats.norm.ppf(abs(alpha))
mean_log_2_step=df['two-step-log'].mean()
std_log_2_step=df['two-step-log'].std()
num_shares=10000
var_log=-num_shares*stats.norm.ppf(alpha,loc=mean_log_2_step,scale=std_log_2_step)
print('Two step VaR at 95% conf-interval for log returns:', var_log)

mean_simp_2_step=df['two-step-simple'].mean()
std_simp_2_step=df['two-step-simple'].std()
var_simp=-num_shares*stats.norm.ppf(alpha,loc=mean_simp_2_step,scale=std_simp_2_step)
print('Two step VaR at 95% conf-interval for simple returns:', var_simp)