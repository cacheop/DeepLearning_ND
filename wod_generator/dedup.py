import pandas as pd

source = "/Users/albertoescarlate/Dropbox/Udacity/wods/data/wod1.tsv"
target = "/Users/albertoescarlate/Dropbox/Udacity/wods/data/wod1out.csv"

df = pd.read_csv(source, sep ='\t')
sep = ';'

for index, row in df.iterrows():
    sent = row[0]
    rest = sent.split(sep, 1)[0]
    #print(rest)
    df.set_value(index, rest)
    
    
#print(df)

df.to_csv(target)





