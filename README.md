# ShowMeTheCode

## Teste da Vizir

<p>O projeto foi feito com o uso do python na versão 3.8.2, o flask no gerenciamento das rotas e sqlite3 como banco de dados.</p>
<p>Para rodar o projeto, foi utilizado o pipenv para gerenciamento das dependências, basta rodar um pipenv install na pasta e todas as dependências serão instaladas. Após a instalação das dependências, no caso do uso do pipenv, basta rodas um 'pipenv shell' na pasta e depois rodas o arquivo app.py que o servidor estará no ar. No caso de não se utilizar o pipenv para instação das dependências, são elas: python 3.8, flask e requests. </p>
<p>O flask roda no endereço padrão que é o http://127.0.0.1:5000/ e possui apenas duas rotas: '/' e '/resultado'.</p>
<p>Como mencionado, foi utilizado o sqlite3 para teste do banco de dados, não é necessário isntalar o sqlite para rodar o servidor, apenas para rodar o sql diretamente no arquivo do banco de dados(pythonsqlite.db).</p>
<p>Os testes foram feitos usando o unittest e estão denstro da pasta test, eles podem ser executados diretamente do terminal, sem passar pelo flask. Na pasta test, além dos testes de todos os arquivos, ainda contém um diretório chamado 'create_database', onde constam os arquivos utilizados para criar e popular o arquivo do sqlite.</p>
