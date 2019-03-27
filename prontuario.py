# -*- encoding: utf-8 -*-

# # imports
from coleta import Coleta
# # imports

# # variables

# # variables

# # classes


class ColetaProntuario(Coleta):

    def getFileList(self):
        arquivos = [arquivo for arquivo in self.IDiretorio.listarArquivos() if "pront" in arquivo]
        return arquivos

    def initSalvar(self, colunas=None, index=None):
        if colunas is None:
            colunas = ["Nome", "Registro", "Data", "Idade", "Olho", "Dioptria", "Lente", "Modelo"]
        if index is None:
            index = colunas[0]
        self.ISalvar = self.ISalvarcls(colunas, index)

    def initGrafico(self, width=None, height=None, widgets=None):
        if widgets is None:
            raise Exception("Não tem nada para mostrar!")
        if width is None:
            width = "500"
        if height is None:
            height = "300"
        self.IGrafico = self.IGraficacls(width,height,widgets)

    def initDiretorio(self,path):
        self.IDiretorio = self.IDiretoriocls(path)
        self._atual = self.getFileList()[0]

# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()