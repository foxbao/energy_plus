from eppy import modeleditor
from eppy.modeleditor import IDF


class Agent:
    def __init__(self, idf_path:str):
        self.idf = IDF('C:/Users/USER/Desktop/1.idf')
        self.idd_path=""
        
    def action(self):
        pass

    def env(self):
        pass
    


if __name__ == '__main__':
    agent=Agent('C:/Users/USER/Desktop/1.idf')
    pass