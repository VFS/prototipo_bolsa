Protótipo Bolsa
===============

Um sistema que puxa informações da bolsa de valores referente a uma ação, e dado um intervalo de tempo, gera um gráfico desta ação em relação ao índice DI no mesmo período (usando variação em percentual ou base 100).

Ou seja, o input se dá por meio das caixas  `Ação`, `Data inicial` e `Data final`, aceitando qualquer ação da BOVESPA, em qualquer período.

Também é exibida uma tabela só da CBLC, com as informações do último dia disponível.

## Fontes de dados:
* Ação: Yahoo Finance por meio da biblioteca [yahoo-finance](https://pypi.python.org/pypi/yahoo-finance)
* [CBLC](http://www.cblc.com.br/cblc/consultas/Arquivos/DBTCER9999.txt) - [Manual](http://bvmf.bmfbovespa.com.br/BancoTitulosBTC/download/DBTCER9999_v3.pdf)
* [CDI](ftp://ftp.cetip.com.br/IndiceDI/) - [Explicação CETIP](http://www.cetip.com.br/astec/series_v05/paginas/indicedi_i2.htm)

## Bibliotecas
* [PureCSS](https://purecss.io/)
* [C3](https://c3js.org) / [D3](https://d3js.org).js

## Uso
Dentro de um virtualenv com python3.6:

```
git clone git@github.com:VFS/prototipo_bolsa.git
pip install -r requirements.txt
chmod a+x run.py
./run.py
```
E então abra o seu navegador em [http://127.0.0.1:5000](http://127.0.0.1:5000)


## JSON
```
  http://127.0.0.1:5000/api/<stock>/<start_date>/<end_date>.json
```
