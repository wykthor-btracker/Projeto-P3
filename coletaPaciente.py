# -*- encoding: utf-8 -*-

# # imports
from janelaPadrao import JanelaTkPadraoProntuario, JanelaTkPadraoFicha
import ficha, prontuario
from percorrerBase import OSDiretorio
import interfaceGrafTk as iGT
from pandasSave import SalvarDados
import pandas as pd
import traceback
# # imports

# # variables

# # variables

# # classes

# # classes

# # functions


def pegarFicha(paciente, pront, inst, data):
    fichas = inst(iGT.JanelaTkinter, OSDiretorio, SalvarDados, pront, data)
    try:
        fichas.initDiretorio(paciente.caminho)
    except Exception as e:
        print("Ignorando {} devido a {}".format(paciente.caminho,e))
        #traceback.print_exc()
        return None
    fichas.initSalvar()
    JanelaTkPadraoFicha(fichas)
    return fichas


def coletarDados(inst):
    inst.abrirArquivoAtual()
    inst.desenharInterface()
    return inst.ISalvar.getDataObject()
# # functions

# # main


def main(*args, **kwargs):
    iterador = OSDiretorio("Pacientes").listarDiretorios()
    resultados = None
    for paciente in iterador:

        prontuarios = prontuario.ColetaProntuario(iGT.JanelaTkinter, OSDiretorio, SalvarDados)

        prontuarios.initDiretorio(paciente.caminho)

        prontuarios.initSalvar()

        JanelaTkPadraoProntuario(prontuarios)

        pronts = coletarDados(prontuarios)
        arquivos = prontuarios.getFileList()

        data = pronts.iloc[-1]["Data"]

        fichaPre = pegarFicha(paciente, arquivos[0], ficha.ColetaFichaPre, data)
        fichaPreDados = coletarDados(fichaPre)

        fichaPos = pegarFicha(paciente, arquivos[-1], ficha.ColetaFichaPos, data)
        fichaPosDados = coletarDados(fichaPos)

        if fichaPre and fichaPos:
            for indice, linha in pronts.iterrows():
                fichaPreDados = fichaPreDados.T.squeeze()
                fichaPosDados = fichaPosDados.T.squeeze()
                concat = pd.concat([linha, fichaPreDados, fichaPosDados]).to_frame().T
                if resultados is None:
                    resultados = concat
                else:
                    resultados = resultados.append(concat)
                print(resultados)
    return


# # main 

if __name__ == "__main__":
    main()