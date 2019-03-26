# -*- encoding: utf-8 -*-

# # imports
import interface
import pandas as pd
# # imports

# # variables

# # variables

# # classes


class SalvarDados(interface.SalvarDados):
    def __init__(self,colunas,index):
        self.colunas = colunas
        self.index = index
        if index not in colunas:
            raise Exception("{} não está em {}".format(index,colunas))
        self._dataframe = pd.DataFrame(columns=colunas)

    def limpar(self):
        self.__init__(self.colunas)

    def definirColunas(self,colunas):
        self._dataframe.columns = colunas

    def update(self,linha,colunas,valores,inplace=False):
        if inplace:
            self._dataframe[linha][colunas] = valores
        else:
            new = self._dataframe.copy()
            new[linha][colunas] = valores
            return new

    def append(self,series,inplace=False):
        if type(series) != pd.Series:
            raise Exception("Parâmetro incorreto, {} é do tipo {}, {} esperado.".format(series,type(series),pd.Series))
        if inplace:
            self._dataframe = self._dataframe.append(series)
        else:
            return self._dataframe.copy().append(series)

    def find(self, value):
        if value in self._dataframe.index:
            return self._dataframe[value]
        else:
            return None

    def getDataObject(self):
        return self._dataframe
# # classes

# # functions

# # functions

# # main


def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()