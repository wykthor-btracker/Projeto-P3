# -*- encoding: utf-8 -*-

# # imports
from janelaPadrao import JanelaTkPadrao
import ficha,prontuario
from percorrerBase import OSDiretorio
import os
# # imports

# # variables

# # variables

# # classes

# # classes

# # functions

# # functions

# # main


def main(*args, **kwargs):
    iterador = OSDiretorio("Pacientes").listarDiretorios()
    print(iterador)
    for paciente in iterador:
        pronts = sorted([arquivo for arquivo in paciente.listarArquivos() if "pront" in arquivo])
        for pront in pronts:
            g = JanelaTkPadrao(pront.caminho, prontuario.ColetaProntuario)
            g.coletar()
        break
    path = "Pacientes/ABADIA RIBEIRO LUIZ/"
    f = JanelaTkPadrao(path, ficha.ColetaFicha)
    return


# # main 

if __name__ == "__main__":
    main()