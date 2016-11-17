import pandas as pd


df = pd.read_pickle('jupyterexample.pickle')
print('Read in jupyterexample.pickle as df.')

df['atime'] = df['atime'].astype(int)
df['ctime'] = df['ctime'].astype(int)


df['atime'] = pd.to_datetime(df['atime'], unit='s')
df['ctime'] = pd.to_datetime(df['ctime'], unit='s')

nonlibs = df[df['package-name'].str.contains('lib')]
nonlibs.sort('ctime', ascending=False)
print(nonlibs)



