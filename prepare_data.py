import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import os

def load_data_files_into_raw_df(conference_directory_path,data_split_type):

    directory_in_string = conference_directory_path + '/' + data_split_type
    
    #parsed pdfs
    directory_content = os.fsencode(directory_in_string+'/parsed_pdfs')
    raw_df_content = pd.DataFrame()
    for file in os.listdir(directory_content):
        with open(directory_in_string) as file:
            data = json.load(file)
            df = json_normalize(data['rooms'])
            if raw_df_content.empty:
                raw_df_content = df
            else:
                raw_df_content = raw_df_content.join(df)
    return raw_df_content
                
raw_df_content = load_data_files_into_raw_df('data/iclr_2017','train')