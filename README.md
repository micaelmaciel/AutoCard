
# releases
não vai ter nenhum por enquanto porque esse foi o meu primeiro projeto "real" em python feito num final de semana, então sabe-se o que esperar do código :(

# uso
ao clicar em adicionar palavra, será criado um arquivo txt contendo a sintaxe correta entendida pelo anki, então basta importar para o anki para o deck de sua escolha

## linux
```console
git clone https://github.com/micaelmaciel/AutoCard.git autocard
cd autocard
python -m venv venv
source venv/bin/active
pip install -r requirements
python main.py
```

## windows powershell
```console
git clone https://github.com/micaelmaciel/AutoCard.git autocard
dir autocard
python -m venv venv
.\venv\bin\activate.ps1
pip install -r requirements
python main.py
```
se tiver algum erro com o tkinter, provavelmente tem que baixá-lo antes, e isso depende do package manager

# features
* palavras no infinitivo e exemplos de frases (uau)
* dá pra importar em decks já existentes
* um botão que não faz nada

# motivação
eu queria algo MUITO específico e por mais que tenham alguns projetos muito melhores envolvendo o anki que provavelmente resolveriam o meu problema, o formato das cartas não é o meu formato e nem funciona do jeito que queria


