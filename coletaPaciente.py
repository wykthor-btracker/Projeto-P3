# -*- encoding: utf-8 -*-

# # imports
from janelaPadrao import JanelaTkPadrao
import ficha, prontuario
from percorrerBase import OSDiretorio
import interfaceGrafTk as iGT
from pandasSave import SalvarDados
# # imports

# # variables

# # variables

# # classes

# # classes

# # functions


def coletar(self):
    self.inst.abrirArquivoAtual()
    self.inst.desenharInterface()
    return self.inst.ISalvar.getDataObject()
# # functions

# # main


def main(*args, **kwargs):
    iterador = OSDiretorio("Pacientes").listarDiretorios()
    for paciente in iterador:

        prontuarios = prontuario.ColetaProntuario(iGT.JanelaTkinter, OSDiretorio, SalvarDados)

        prontuarios.initDiretorio(paciente.caminho)

        prontuarios.initSalvar()

        JanelaTkPadrao(prontuarios)

        coletarDados(prontuarios)
        arquivos = prontuarios.getFileList()

        fichaPre = pegarFicha(paciente, arquivos[0], ficha.ColetaFichaPre)
        coletarDados(fichaPre)

        fichaPos = pegarFicha(paciente, arquivos[-1], ficha.ColetaFichaPos)
        coletarDados(fichaPos)

    return


def coletarDados(inst):
    inst.abrirArquivoAtual()
    inst.desenharInterface()


def pegarFicha(paciente, pront, inst):
    fichas = inst(iGT.JanelaTkinter, OSDiretorio, SalvarDados, pront)
    fichas.initDiretorio(paciente.caminho)
    fichas.initSalvar()
    JanelaTkPadrao(fichas)
    return fichas


# # main 

if __name__ == "__main__":
    main()