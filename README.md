# Projeto P3 - Refatoramento
### Problemática:
> Faz-se necessário uma aplicação que auxilie o usuário na transcrição de documentos médicos ilegíveis para processos automáticos como OCR em conjuntos de dados utilizáveis por métodos de aprendizagem de máquina, no exemplo, tabelas csv/excel.

### Erros esperados:
No programa original, se a coluna Olho ou data não forem preenchidas corretamente, OE/OD(Dois prontuários são exigidos para considerar o exame válido) e ddmmyyyy ou dd/mm/yyyy ou dd-mm-yyyy, respectivamente, o programa irá levantar um erro e parar execução, ou determinar que o paciente é inválido e adicioná-lo à planilha de erros, parando a execução.

![Não encontrado](https://i.imgur.com/cB0OMTf.png)

Se este erro se apresentar, acesse Erros.xlsx, e delete Paciente1 da coluna Nomes, então, rode o programa original novamente.

No início de script.py, na linha 14,
```python
chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
```
Se este caminho estiver incorreto, o programa irá dar erro e parar de funcionar. Se o sistema em que está sendo testado não tiver o google chrome instalado, duas coisas podem ser feitas:
- Instalar o chrome e usar a variável para guardar o caminho do executável
- Apontar o caminho de algum outro executável de um navegador capaz de abrir arquivos de imagem(Firefox, safari)

# Execução comum aos dois programas:

Rode o programa, uma janela se abrirá com a interface, e outro com o documento desejado, busque no documento as informações tais como estarão na interface gráfica, quando tiver coletado tudo que for possível, aperte o botão salvar(para o programa refatorado, após isto, finalizar.)

Outra janela se abrirá, repita o procedimento, desta vez coletando os dados da ficha de atendimento. Se encontrar os dados apenas na linha precedida por AR, marque as linhas correspondentes com 1.

Repita este processo até a interface gráfica fechar, os resultados serão salvos em Outputs.xlsx .

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
# Composite
Para a implementação do padrão de design composite, foi desenhada uma interface(interface.InterfaceGrafica) que quando extendida, fosse capaz de conter objetos compostos e simples(interface.DrawableWidget), todos tendo a mesma propriedade, no caso específico da aplicação, foi feito de forma que a interface gráfica fosse construída modularmente.
![Composite](https://i.imgur.com/6qRnkXH.png)

# Strategy
Para a implementação do padrão de design Strategy, fiz com que o objeto que implementa a interface interface.Coleta fosse capaz de receber instâncias de classes que implementam interfaces relativas às funcionalidades necessárias para fazer a coleta de dados: Gerar uma interface gráfica(interface.InterfaceGrafica), percorrer diretórios(interface.Diretorio) com os arquivos(interface.Arquivo) desejados, lógica necessária para salvar os dados(interface.SalvarDados) coletados em estruturas de dados. Dessa forma, é possível substituir os objetos concretos que implementam as interfaces designadas, e utilizar o objeto de coleta sem muitas complicações.
![Strategy](https://i.imgur.com/4pIOfRg.png)

# Template
Para a implementação do padrão de design Template, foi feita uma implementação para facilitar a geração de interfaces gráficas por meio da biblioteca implementada para exemplificar o funcionamento do programa: Tkinter. Um objeto JanelaPadraoTk foi criado que continha os passos necessários para desenhar a interface gráfica correspondente ao tipo de informação que se desejava coletar. Esta foi herdada para classes que continham o funcionamento diferenciado necessário para contemplar os diferentes tipos de dados encontrados em diferentes documentos de consulta/relatórios de cirurgia necessários.
![Template](https://i.imgur.com/MplHCi3.png)

## Funcionalidades/Métodos afetados
Todos, o código legado foi completamente reescrito para realizar o refatoramento das funcionalidades.
