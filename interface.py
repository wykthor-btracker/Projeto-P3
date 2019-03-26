# -*- encoding: utf-8 -*-

# # imports
from abc import ABC, abstractmethod
# # imports

# # variables

# # variables

# # classes


class Diretorio(ABC):
    def __init__(self,caminhoDiretorio):
        self.caminhoDiretorio = caminhoDiretorio
        self.ClasseArquivo = None

    @abstractmethod
    def isFile(self):
        pass

    @abstractmethod
    def isFolder(self):
        pass

    @abstractmethod
    def abrirArquivo(self):
        pass

    @abstractmethod
    def abrirDiretorio(self):
        pass

    @abstractmethod
    def listarArquivos(self):
        pass

    @abstractmethod
    def listarDiretorios(self):
        pass

    @abstractmethod
    def irParaDiretorio(self):
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


class SalvarDados(ABC):
    def __init__(self,colunas):
        self.colunas = colunas

    @abstractmethod
    def limpar(self):
        pass

    @abstractmethod
    def definirColunas(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def append(self):
        pass

    @abstractmethod
    def find(self):
        pass

class Coleta(ABC):
    def __init__(self,IGrafica,IDiretorio,ISalvar):
        self.IGrafica = IGrafica
        self.IDiretorio = IDiretorio
        self.ISalvar = ISalvar

    @abstractmethod
    def abrirDiretorio(self):
        pass

    @abstractmethod
    def proximoArquivo(self):
        pass

    @abstractmethod
    def coletarDados(self):
        pass

    @abstractmethod
    def salvarDados(self):
        pass

    @abstractmethod
    def desenharInterface(self):
        pass

    @abstractmethod
    def initSalvar(self):
        pass

    @abstractmethod
    def initGrafico(self):
        pass

    @abstractmethod
    def initDiretorio(self):
        pass


class DrawableWidget(ABC):
    def __init__(self,campos):
        self.campos = campos

    @abstractmethod
    def draw(self,root):
        pass

    @abstractmethod
    def getCampos(self):
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

# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()