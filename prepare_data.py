import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import os
import pandas.io.json as pd_json

def load_data_files_into_raw_df(conference_directory_path,data_split_type):

    #parsed pdfs
    directory_in_string = conference_directory_path + '/' + data_split_type +'/parsed_pdfs/'
    directory_content = os.fsencode(directory_in_string)
    raw_df_content = pd.DataFrame()
    for file in os.listdir(directory_content):
        filename = os.fsdecode(file)
        with open(os.path.join(directory_in_string, filename),encoding="utf8") as file:
            df = pd.read_json(file,orient='columns')
            #data = json.load(file)
            #df = json_normalize(data)
            #data = pd_json.loads(result)
            if raw_df_content.empty:
                raw_df_content = df
            else:
                raw_df_content = raw_df_content.append(df)
    return raw_df_content
                
raw_df_content = load_data_files_into_raw_df('data/iclr_2017','train')