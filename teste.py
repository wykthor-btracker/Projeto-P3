# -*- encoding: utf-8 -*-

# # imports
import ficha,prontuario
from pandasSave import SalvarDados
from percorrerBase import OSDiretorio, BrowserArquivo
import interfaceGrafTk as gtk
# # imports

# # variables

# # variables

# # classes

# # classes

# # functions
def coletarDados(inst):
    dados = inst.coletarDados()
    for widget,fields in dados.items():
        if isinstance(widget,gtk.TextWidgets):
            inst.ISalvar.append(fields,True)
            inst.IGrafico.rootInst.destroy()
# # functions

# # main


def coletarFicha(path):
    inst = ficha.ColetaFicha(gtk.JanelaTkinter, OSDiretorio, SalvarDados)
    inst.initSalvar()
    inst.initDiretorio(path)
    campos = gtk.TextWidgets([])
    camposTexto = inst.ISalvar.colunas
    campos.generateWidgets(camposTexto, gtk.CampoTexto)
    salvar = gtk.Botao("Ok",len(camposTexto),0,lambda:coletarDados(inst),[])
    proximo = gtk.Botao("Proximo",salvar.row+1,0,lambda:inst.proximoArquivo())
    inst.initGrafico(widgets=[campos,salvar,proximo])
    inst.abrirArquivo()
    inst.desenharInterface()
    return inst.ISalvar.getDataObject()

def main():
    print(coletarFicha("Pacientes/ABADIA RIBEIRO LUIZ/"))
    return None

# # main 

if __name__ == "__main__":
    main()