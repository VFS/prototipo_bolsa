Protótipo Bolsa
===============

Um sistema que puxa informações da bolsa de valores referente a uma ação, e dado um intervalo de tempo, gera um gráfico desta ação em relação ao índice DI no mesmo período (usando variação em percentual ou base 100).

O input são (Ação, Data inicial, Data final) - então pode ser qualquer ação da BOVESPA, em qualquer período.
Também é exibida uma tabela só da CBLC. Ela será sempre do último dia disponível.

Os campos da tabela da CBLC estão explicados em um [manual fornecido pela própria CBLC](http://bvmf.bmfbovespa.com.br/BancoTitulosBTC/download/DBTCER9999_v3.pdf).

## Fontes de dados:
* Ação: [Yahoo Finance](https://yahoo.com)
* [CBLC](http://www.cblc.com.br/cblc/consultas/Arquivos/DBTCER9999.txt)
* [CDI](ftp://ftp.cetip.com.br/IndiceDI/)
