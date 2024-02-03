# Projeto Marketing Digital

## Escopo  

O responsável pela empresa Digital World, nossa cliente, precisa suprir os funcionários da área de Marketing com informações 
relevantes sobre as tendências de pesquisa em ferramentas de busca, especialmente o Google.

## Projeto  

O projeto consiste em fornecer essas informações em arquivos de excel para que os mesmos sejam facilmente utilizados pelos funcionários no momento que precisarem, por exemplo, quando estiverem em visita ao cliente.

## Orçamento  

O orçamento disponível para o projeto é muito baixo. Inicialmente, o objetivo objetivo principal avaliar como essas informações poderão ajudar no processo de tomada de decisão das empresas, suas clientes.

## Requisitos

No processo de levantamento de requisitos, a nossa área responsável entrevistou os envolvidos no projeto, especialmente os usuários do sistema e os todos os outros stakeholders. Dessa forma, sugeriram que os dados disponibilizados gratuitamente pelo Google podem servir a esse propósito. Assim, nossa área técnica foi acionada para pensar na implementação. Ficou determinado que a forma mais efetiva e menos custosa de desenvolver esse projeto é através do Big Query, ferramenta de consulta de Big Data do Google que permite a consulta de dados relevantes de tendências (trends) gratuitamente ou com um custo mínimo, dependendo da forma como for implementada e do grau de utilização.  

Como mínimo produto viável (MVP), foi desenvolvido um script em Python que busca os dados de tendências de pesquisa no Big Query e os grava em um arquivo de Excel. Posteriormente, isso poderá ser tratado de diversas formas, ou seja, pelo próprio usuário. Ainda, dado a existência de suplementos fornecidos pela própria Microsoft, será possível expandir o projeto para que o Python forneça dados de análise diretamente nos arquivos excel. O Google Spreadsheet também fornece alguns recursos que tornam a expansão desse projeto interessante. 

Alguns detalhes de implementação já foram pensados, como:  

* Limitar a quantidade de pesquisas para minimizar o impacto de custo de processamento no Google;
* Determinar uma forma de padronizar os nomes dos arquivos para que os mesmos facilitem a identificação histórica de sua criação e a qual período ele se refere (utilizando o campo "week");  
  
Para efeitos de apresentação de um MVP, foi criada uma lista de 10 linhas contendo as tendências a partir da menor data disponível no Big Query, que remonta ao ano de 2018.

