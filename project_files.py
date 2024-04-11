import re
import glob
import os
class AnalizePy(): #создаем класс
    def __init__(self):
        self.data = {}
        self.__files = self.__all_files()        
    def all_name(self, file):  #анализирует файл на наличие функций, классов и переменных 
        with open(f'{file}', 'r', encoding = 'utf-8', errors = 'ignore') as f:
            file = f.read()    
        func = re.findall(r'def\s(\w+)', file)
        variable = re.findall(r'([\w ]+)=', file)       
        classes = re.findall(r'class\s(\w+)', file)
        variable = set(variable)       
        all_data = {'functions':func,   #словарь со всей информацией
                    'variables':variable,                   
                    'classes':classes}
        return all_data 
    def __all_files(self):  #поиск всех файлов на компьютере с расширением py
        search_pattern = os.path.join('C:\\', '**', '*.py')
        files = glob.glob(search_pattern, recursive = True)        
        return files
    def insert_data(self): #объединяет всё в словарь
        for file in self.__files:           
            self.data[f'{file}'] = self.all_name(file)
analize = AnalizePy()
analize.insert_data()
print(analize.data)
