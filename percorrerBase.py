# -*- encoding: utf-8 -*-

# # imports
import interface
import os
import webbrowser


# # imports

# # variables

# # variables

# # classes


class OSDiretorio(interface.Diretorio):
    def __init__(self, caminho):
        super().__init__(caminho)
        self.classeArquivo = OSArquivo

    def makeFileHandler(self, caminho):
        return self.classeArquivo(os.path.join(self.caminho, caminho))

    def makeFolderHandler(self, caminho):
        return OSDiretorio(os.path.join(self.caminho, caminho))

    def isFile(self, caminho):
        return os.path.isfile(os.path.join(self.caminho, caminho))

    def isFolder(self, caminho):
        return os.path.isdir(os.path.join(self.caminho, caminho))

    def abrirArquivo(self, caminho):
        self.classeArquivo(caminho).abrir()

    def listarArquivos(self):
        return [self.makeFileHandler(file) for file in os.listdir(self.caminho) if
                self.isFile(file)]

    def listarDiretorios(self):
        return [self.makeFolderHandler(folder) for folder in os.listdir(self.caminho) if self.isFolder(folder)]

    def irParaDiretorio(self, caminho):
        os.chdir(caminho)
        self.caminho = caminho

    def getFolderName(self):
        basename = self.caminho
        basename = os.path.basename(basename)
        return basename

    def __repr__(self):
        return "OSDiretorio Instance: {}".format(self.caminho)

    def __lt__(self, other):
        if isinstance(other, type(self)) and hasattr(other, "caminho"):
            return self.caminho < other.caminho


class OSArquivo(interface.Arquivo):
    def __init__(self, caminho):
        super().__init__(caminho)
        self.instance = None

        browsers = ["safari", "chrome", "firefox"]
        for browser in browsers:
            try:
                self.instance = webbrowser.get(browser)
                break
            except Exception as e:
                pass #TODO make logger --print e--

        if self.instance is None:
            raise Exception("Nenhum browser encontrado. Browsers tentados:\n{}".format(browsers))

    def abrir(self):
        self.instance.open(self.caminho, new=2)

    def ler(self):
        return Exception("Função não definida")

    def getFileName(self):
        basename = self.caminho
        basename = os.path.basename(basename)
        if "." in basename:
            basename = basename.split(".")[0]
        return basename

    def __eq__(self, other):
        if hasattr(other, "caminho"):
            return self.caminho == other.caminho and isinstance(self, type(other))
        else:
            return False

    def __contains__(self, item):
        if isinstance(item, str):
            return item.lower() in self.caminho.lower()

    def __repr__(self):
        return "OSArquivo Instance: {}".format(self.caminho)

    def __lt__(self, other):
        if isinstance(other, type(self)) and hasattr(other, "caminho"):
            return self.caminho < other.caminho


# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()
