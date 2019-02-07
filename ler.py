#!/usr/bin/env python
# coding: utf-8

import os
import datetime
import subprocess
import pandas
import tkinter as tk


#Inicialização de variáveis
patients = [];
errors = [];
chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
stop = False
save = False
forward = 0
data = pandas.read_excel("Output.xlsx")
erros = pandas.read_excel("Erros.xlsx")

os.chdir("./Pacientes")
#patients = [os.listdir(".")[0]]


def ordenarArquivos(files):
    return sorted(files,key=lambda x:int(x.split("-")[0].rstrip()))

#Retorna os nomes de todos os arquivos no diretório atual
def storeFiles():
    files = []
    for root, directory, file in os.walk('.'):
        pass
        #files.append(file)
    return file

#Inicializa um dataframe para o paciente
def createPatientDF(name):
    patientDF = pandas.DataFrame(columns = ['Nome', 'Registro', "Data da cirurgia", "Olho", "Dioptria", "Marca da Lente", 
                                            "Modelo da Lente","Data Pré-op", "Esférico Pré-op", "Cilindro Pré-op", 
                                            "Eixo Pré-op", "Data Pós-op", "Esférico Pós-op", "Cilindro Pós-op", "Eixo Pós-op"])
    patientDF.loc[0] = [name, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    return patientDF


#Função que abre cada prontuário cirúrgico na pasta atual
def getSurgeries(patientDF, files):
    global stop
    global forward
    #files = ordenarArquivos(files)
    print(files)
    prontuarios = [file for file in files if "PRONTU" in file]
    utilizaveis = []
    ind = 0
    patientDF = patientDF
    
    while(ind<len(prontuarios) and not stop):
        subprocess.Popen([chrome_path, prontuarios[ind]])
        patientDF, pront = prontuario(patientDF)
        if(forward == 1):
            ind+=1
            forward = 0
        elif(forward == -1):
            ind-=1
            forward = 0
        else:
            raise Exception("{} inválido, 1 ou -1 esperado.".format(forward))
        if pront > 0:
            utilizaveis.append(prontuarios[ind-1])
    if patientDF.loc[0]['Olho'] == None:
        patientDF = patientDF.drop(index=0).reset_index().drop(columns=['index'])#ok
    if len(utilizaveis)>2:
        errors.append(patientDF.loc[0]['Nome'])
    #os.system('taskkill /f /im chrome.exe')
    
    return patientDF, utilizaveis

#Gambiarra, salva os dados no prontuário e avança para a próxima tela
def storeSave(instance):
    global save 
    save = True;
    avancar(instance)

#Função que cria a interface e lida com os dados das fichas de atendimento
def prontuario(patientDF):

    pront = 0
    
    global save
    
    root = tk.Tk()
    root.attributes("-topmost", True)
    tk.Label(root, text="Registro").grid(row=0)
    tk.Label(root, text="Data da Cirurgia ('DDMMAAAA')").grid(row=1)
    tk.Label(root, text="Olho (OE ou OD)").grid(row=2)
    tk.Label(root, text="Dioptria").grid(row=3)
    tk.Label(root, text="Marca da Lente").grid(row=4)
    tk.Label(root, text="Modelo da Lente").grid(row=5)
    
    reg = tk.StringVar()
    data = tk.StringVar()
    olho = tk.StringVar()
    dioptria = tk.StringVar()
    marca = tk.StringVar()
    modelo = tk.StringVar()
    
    regEntry = tk.Entry(root, textvariable=reg)
    dataEntry = tk.Entry(root, textvariable=data)
    olhoEntry = tk.Entry(root, textvariable=olho)
    dioptriaEntry = tk.Entry(root, textvariable=dioptria)
    marcaEntry = tk.Entry(root, textvariable=marca)
    modeloEntry = tk.Entry(root, textvariable=modelo)

    regEntry.grid(row=0, column=1)
    dataEntry.grid(row=1, column=1)
    olhoEntry.grid(row=2, column=1)
    dioptriaEntry.grid(row=3, column=1)
    marcaEntry.grid(row=4, column=1)
    modeloEntry.grid(row=5, column=1)

    tk.Button(root, text="Anterior", command=lambda: voltar(root)).grid(row=6, column=0, pady=4)
    tk.Button(root, text="Ok", command=lambda: storeSave(root)).grid(row=6, column=1, pady=4)
    tk.Button(root, text="Próximo", command=lambda: avancar(root)).grid(row=6, column=2, pady=4)
    tk.Button(root, text="Erro", command= lambda: salvarErro(patientDF,root)).grid(row=7, column=0, pady=4)
    tk.Button(root, text="Sair", command=lambda: sair(root)).grid(row=7, column=1)
    
    root.mainloop()
    
    if save:
        patientDF = salvarDadosCir(reg.get(), data.get(), olho.get(), dioptria.get(), marca.get(),
                                                      modelo.get(), patientDF)
        print(patientDF)
        save = False

    #Caso não esteja vazio, consideramos que o prontuário é válido
    if olho.get() == 'OE' or olho.get() == 'OD':
        pront = 1

    return patientDF, pront

#Salva os dados coletados na interface para o dataframe do paciente, criando uma entrada para cada cirurgia.
def salvarDadosCir(reg, data, olho, dioptria, lente, modelo, patientDF):
    name = patientDF.loc[0]['Nome']
    patientDF.loc[patientDF.shape[0]] = [name, reg, data, olho, dioptria, lente, modelo, None, None, None, None, None, None, None, None]
    return patientDF

#Salva os dados coletados na interface para o dataframe do paciente
def salvarDadosFicha(data, esfE, esfD, cilE, cilD, eixoE, eixoD, patientDF, pre):
    name = patientDF.loc[0]['Nome']
    patientDF = patientDF.drop([0]).reset_index().drop(columns=['index'])
    for ind in range(patientDF.shape[0]):
        oldRow = list(patientDF.loc[ind])
        newRow = oldRow.copy()
        if patientDF.loc[ind]['Olho'] == 'OE':
            if pre:
                newRow[7] = data
                newRow[8] = esfE
                newRow[9] = cilE
                newRow[10] = eixoE
            else:
                newRow[11] = data
                newRow[12] = esfE
                newRow[13] = cilE
                newRow[14] = eixoE
        else:
            if pre:
                newRow[7] = data
                newRow[8] = esfD
                newRow[9] = cilD
                newRow[10] = eixoD
            else:
                newRow[11] = data
                newRow[12] = esfD
                newRow[13] = cilD
                newRow[14] = eixoD
        print(len(newRow))
        patientDF.loc[ind] = newRow
    return patientDF

#Volta para a última ficha ou prontuário
def voltar(instance):
    global forward
    instance.destroy()
    forward = -1

#Vai para a próxima ficha ou prontuário
def avancar(instance):
    global forward
    instance.destroy()
    forward = 1

#Registra que há um erro neste paciente e avança para o próximo.
def salvarErro(patientDF,instance):
    errors.append(patientDF.loc[0]['Nome'])
    instance.destroy()

#Para o programa
def sair(instance):
    instance.destroy()
    stop = True;


#Transforma uma string do tipo "DDMMYYYY" em um datetime
def processarData(data):
    day = int(data[0:2])
    month = int(data[2:4])
    year = int(data[4:])
    return datetime.date(year, month, day)

#Transforma uma string com a dioptria em um float. Lida tanto com vírgula quanto com ponto.
def processarDioptria(dioptria):
    if ',' in dioptria:
        part1 = dioptria[0:dioptria.find(',')]
        part2 = dioptria[dioptria.find(',')+1:]
        dioptriaAtualizada = float(part1 + '.' + part2)
    else:
        dioptriaAtualizada = float(dioptria)
    
    return dioptriaAtualizada

def ficha(patientDF, pre):
    
    global save
    
    root = tk.Tk()

    tk.Label(root, text="Data").grid(row=0)
    tk.Label(root, text="Esférico OE").grid(row=1)
    tk.Label(root, text="Esférico OD").grid(row=2)
    tk.Label(root, text="Cilindro OE").grid(row=3)
    tk.Label(root, text="Cilindro OD").grid(row=4)
    tk.Label(root, text="Eixo OE").grid(row=5)
    tk.Label(root, text="Eixo OD").grid(row=6)
    
    data = tk.StringVar()
    esfE = tk.StringVar()
    esfD = tk.StringVar()
    cilE = tk.StringVar()
    cilD = tk.StringVar()
    eixoE = tk.StringVar()
    eixoD = tk.StringVar()
    
    dataEntry = tk.Entry(root, textvariable=data)
    esfEEntry = tk.Entry(root, textvariable=esfE)
    esfDEntry = tk.Entry(root, textvariable=esfD)
    cilEEntry = tk.Entry(root, textvariable=cilE)
    cilDEntry = tk.Entry(root, textvariable=cilD)
    eixoEEntry = tk.Entry(root, textvariable=eixoE)
    eixoDEntry = tk.Entry(root, textvariable=eixoD)

    dataEntry.grid(row=0, column=1)
    esfEEntry.grid(row=1, column=1)
    esfDEntry.grid(row=2, column=1)
    cilEEntry.grid(row=3, column=1)
    cilDEntry.grid(row=4, column=1)
    eixoEEntry.grid(row=5, column=1)
    eixoDEntry.grid(row=6, column=1)

    tk.Button(root, text="Anterior", command= lambda: voltar()).grid(row=7, column=0, pady=4)
    tk.Button(root, text="Ok", command=lambda: storeSave()).grid(row=7, column=1, pady=4)
    tk.Button(root, text="Próximo", command= lambda: avancar()).grid(row=7, column=2, pady=4)
    tk.Button(root, text="Erro", command= lambda: salvarErro(patientDF)).grid(row=8, column=0, pady=4)
    tk.Button(root, text="Sair", command= lambda: sair()).grid(row=8, column=1)

    root.mainloop()
    
    if save:
        patientDF = salvarDadosFicha(data.get(), esfE.get(), esfD.get(), cilE.get(), cilD.get(),
                                                      eixoE.get(), eixoD.get(), patientDF, pre)
        save = False
        
    return patientDF

def quebrarLista(pronts, files):
    return files[0:files.index(pronts[0])], files[files.index(pronts[1])+1:]


#Iterando pelos pacientes
for patient in patients:
    if not stop:
        os.chdir("./" + patient)
        files = storeFiles()
        print(files)
        patientDF = createPatientDF(patient)
        patientDF, pronts = getSurgeries(patientDF, files)
        listaPre, listaPos = quebrarLista(pronts, files)
        print(listaPre)
        print(listaPos)

def main():
    pass

if __name__ == "__main__":
    main()
