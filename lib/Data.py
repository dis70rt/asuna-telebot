import pandas as pd
import os

os.system('cls' if os.name=='nt' else 'clear')

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data.csv')
fields = ['id','username','first_name','last_name']

def import_data(data: list):

    data_dict = {
        'id': data[0],
        'username': data[1],
        'first_name': data[2],
        'last_name': data[3]
    }

    df = pd.read_csv(filename)
    df.drop_duplicates(keep='first', ignore_index=True, inplace=True)
    
    if data[0] not in df['id'].values:
        df = df.append(data_dict, ignore_index=True)
        df.to_csv(filename, mode='w', index=False)
        print({df})

    else:
        df.to_csv(filename, mode='w', index=False)
        print(df)