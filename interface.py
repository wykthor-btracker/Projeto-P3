# -*- encoding: utf-8 -*-

# # imports
from abc import ABC, abstractmethod
# # imports

# # variables

# # variables

# # classes


class Diretorio(ABC):
    def __init__(self,caminhoDiretorio):
        self.caminho = caminhoDiretorio
        self.ClasseArquivo = None

    @abstractmethod
    def isFile(self,caminho):
        pass

    @abstractmethod
    def isFolder(self,caminho):
        pass

    @abstractmethod
    def makeFileHandler(self,caminho):
        pass

    @abstractmethod
    def makeFolderHandler(self,caminho):
        pass

    @abstractmethod
    def abrirArquivo(self,caminho):
        pass

    @abstractmethod
    def listarArquivos(self):
        pass

    @abstractmethod
    def listarDiretorios(self):
        pass

    @abstractmethod
    def irParaDiretorio(self,caminho):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def getFolderName(self):
        pass


class Arquivo(ABC):
    def __init__(self,caminhoRaiz):
        self.caminho = caminhoRaiz

    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def ler(self):
        pass

    @abstractmethod
    def __eq__(self,other):
        pass

    @abstractmethod
    def __contains__(self, item):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def getFileName(self):
        pass

    @abstractmethod
    def __lt__(self,other):
        pass


class SalvarDados(ABC):
    def __init__(self,colunas,index):
        self.colunas = colunas
        self.index = index

    @abstractmethod
    def limpar(self):
        pass

    @abstractmethod
    def definirColunas(self, colunas):
        pass

    @abstractmethod
    def update(self, linha, colunas, valores, inplace=False):
        pass

    @abstractmethod
    def append(self, dataObject, inplace=False):
        pass

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def getDataObject(self):
        pass

    @abstractmethod
    def saveToFile(self):
        pass


class Coleta(ABC):
    def __init__(self,IGraficacls,IDiretoriocls,ISalvarcls):
        self.IGraficacls = IGraficacls
        self.IDiretoriocls = IDiretoriocls
        self.ISalvarcls = ISalvarcls
        self.ISalvar = None
        self.IGrafico = None
        self.IDiretorio = None

    @abstractmethod
    def abrirDiretorio(self,path):
        pass

    @abstractmethod
    def coletarDados(self):
        pass

    @abstractmethod
    def salvarDados(self, title):
        pass

    @abstractmethod
    def abrirArquivoAtual(self):
        pass

    @abstractmethod
    def adicionarDados(self, listaDeDados):
        pass

    @abstractmethod
    def desenharInterface(self):
        pass

    @abstractmethod
    def fecharInterface(self):
        pass

    @abstractmethod
    def initSalvar(self):
        pass

    @abstractmethod
    def initGrafico(self):
        pass

    @abstractmethod
    def initDiretorio(self,caminho):
        pass

    @abstractmethod
    def getFileList(self):
        pass

    @abstractmethod
    def proximoArquivo(self):
        pass

    @abstractmethod
    def anteriorArquivo(self):
        pass


class DrawableWidget(ABC):
    def __init__(self,campos):
        self.campos = campos

    @abstractmethod
    def draw(self,root):
        pass

    @abstractmethod
    def coletarDados(self):
        pass


class InterfaceGrafica(ABC):
    def __init__(self,width,height,Widgets):
        self.width = width
        self.height = height
        self.Widgets = Widgets

    @abstractmethod
    def desenharWidgets(self):
        pass

    @abstractmethod
    def desenharInterface(self):
        pass

    @abstractmethod
    def coletarDados(self):
        pass

    @abstractmethod
    def fecharInterface(self):
        pass
# # classes

# # functions

# # functions

# # main


def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()