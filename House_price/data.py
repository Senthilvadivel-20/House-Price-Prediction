import pandas as pd
from sklearn.preprocessing import LabelEncoder



def locatio_encoder(value):
    df=pd.read_csv('.\Files\Chennai.csv')
    loc=LabelEncoder()
    df['Location']=loc.fit_transform(df['Location'])
    location=loc.transform([value])[0]

    return location





