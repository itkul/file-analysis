import re
import glob
import os
class AnalizePy():
    def __init__(self):
        self.data = {}
        self.__files = self.__all_files()        
    def all_name(self,file):       
        with open(f'{file}','r',encoding = 'utf-8',errors = 'ignore') as f:
            file = f.read()    
        func = re.findall(r'def\s(\w+)',file)
        variable = re.findall(r'([\w ]+)=',file)       
        classes = re.findall(r'class\s(\w+)',file)
        variable = set(variable)       
        all_data = {'functions':func,
                    'variables':variable,                   
                    'classes':classes}
        return all_data
    def __all_files(self):  
        search_pattern = os.path.join('C:\\','**','*.py')
        files = glob.glob(search_pattern,recursive = True)        
        return files
    def insert_data(self):
        for file in self.__files:           
            self.data[f'{file}'] = self.all_name(file)
analize = AnalizePy()
analize.insert_data()
print(analize.data)