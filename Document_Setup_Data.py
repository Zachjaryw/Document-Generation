import json
from pathlib import Path
import pandas as pd

class FilePath:

    filepath = 'aaa'
    
    document_filepath = "a.docx"

class Setup_Data:

    def setup_data_JSON(filepath):
        '''
        This method takes in a filepath and returns the json file as a dictionary
        @param filepath (str) - the filepath for the desired file
        @return data (dict) - a dicitonary with the data from the file
        '''
        with open(filepath) as file:
            data = json.load(file)
            return data
        
    def setup_data_xlsx(filepath):
        '''
        This method takes in a filepath and returns the json file as a dictionary
        @param filepath (str) - the filepath for the desired file
        @return data (dict) - a dicitonary with the data from the file
        '''
        data = pd.read_excel(filepath)
        return data