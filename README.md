# Projeto P3 - Refatoramento
### Problemática:
> Faz-se necessário uma aplicação que auxilie o usuário na transcrição de documentos médicos ilegíveis para processos automáticos como OCR em conjuntos de dados utilizáveis por métodos de aprendizagem de máquina, no exemplo, tabelas csv/excel.


## Projeto Original
### Como rodar
No diretório onde foi clonado o repositório:
```bash
git checkout master
python3 script.py
```

## Projeto Refatorado
### Como rodar
```bash
git checkout if-to-series
python3 coletaPaciente.py
```
## Padrão 1,2 e 3
# Composite
Para a implementação do padrão de design composite, foi desenhada uma interface(interface.InterfaceGrafica) que quando extendida, fosse capaz de conter objetos compostos e simples(interface.DrawableWidget), todos tendo a mesma propriedade, no caso específico da aplicação, foi feito de forma que a interface gráfica fosse construída modularmente.
[UML]

# Strategy
Para a implementação do padrão de design Strategy, fiz com que o objeto que implementa a interface interface.Coleta fosse capaz de receber instâncias de classes que implementam interfaces relativas às funcionalidades necessárias para fazer a coleta de dados: Gerar uma interface gráfica(interface.InterfaceGrafica), percorrer diretórios(interface.Diretorio) com os arquivos(interface.Arquivo) desejados, lógica necessária para salvar os dados(interface.SalvarDados) coletados em estruturas de dados. Dessa forma, é possível substituir os objetos concretos que implementam as interfaces designadas, e utilizar o objeto de coleta sem muitas complicações.
[UML]

# Template
Para a implementação do padrão de design Template, foi feita uma implementação para facilitar a geração de interfaces gráficas por meio da biblioteca implementada para exemplificar o funcionamento do programa: Tkinter. Um objeto JanelaPadraoTk foi criado que continha os passos necessários para desenhar a interface gráfica correspondente ao tipo de informação que se desejava coletar. Esta foi herdada para classes que continham o funcionamento diferenciado necessário para contemplar os diferentes tipos de dados encontrados em diferentes documentos de consulta/relatórios de cirurgia necessários.
[UML]

## Funcionalidades/Métodos afetados
Todos, o código legado foi completamente reescrito para realizar o refatoramento das funcionalidades.
