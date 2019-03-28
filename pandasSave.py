# -*- encoding: utf-8 -*-

# # imports
import interface
import pandas as pd
# # imports

# # variables

# # variables

# # classes


class SalvarDados(interface.SalvarDados):
    def __init__(self,colunas, index):
        super().__init__(colunas, index)
        self._dataframe = pd.DataFrame(columns=colunas)
        if index not in colunas and index is not None:
            raise Exception("{} não está em {}".format(index,colunas))
        self._dataframe.set_index(index)

    def limpar(self):
        self.__init__(self.colunas,self.index)

    def definirColunas(self,colunas):
        self._dataframe.columns = colunas

    def update(self, linha, colunas, valores, inplace=False):
        if inplace:
            self._dataframe[linha][colunas] = valores
        else:
            new = self._dataframe.copy()
            new[linha][colunas] = valores
            return new

    def append(self, dataObject, inplace=False):
        if inplace:
            try:
                self._dataframe = self._dataframe.append(dataObject,ignore_index=True)
            except Exception as e:
                print(e)
        else:
            try:
                return self._dataframe.copy().append(dataObject,ignore_index=True)
            except Exception as e:
                print(e)

    def find(self, value):
        if value in self._dataframe.index:
            return self._dataframe[value]
        else:
            return None

    def getDataObject(self):
        return self._dataframe

    def saveToFile(self, title):
        self._dataframe.to_csv(title, sep=";")
# # classes

# # functions

# # functions

# # main


def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()