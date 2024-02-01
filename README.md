# Projeto Marketing Digital

## Escopo  

O responsável pela empresa Digital World, nossa cliente, precisa suprir os funcionários da área de Marketing com informações 
relevantes sobre as tendências de pesquisa em ferramentas de busca, especialmente o Google.

## Projeto  

Contudo, num primeiro momento, o projeto consiste em fornecer essas informações em arquivos de excel para que os mesmos sejam facilmente utilizados pelos funcionários no momento que precisarem, por exemplo, quando estiverem em visita ao cliente.

## Orçamento  

Para isso, o responsável designou que o orçamento que ele tem disponível para o projeto é muito baixo. O objetivo principal é avaliar como essas informações poderão ajudar no processo de tomada de decisão das empresas, suas clientes.

## Requisitos

No processo de levantamento de requisitos, a nossa área responsável analisou de forma ampla, entrevistando os envolvidos no projeto, especialmente os usuários do sistema e os stakeholders. Dessa forma, sugeriram que os dados disponibilizados gratuitamente pelo Google podem servir a esse propósito. Então, nossa área técnica determinou que a forma mais efetiva e menos custosa de desenvolver esse projeto é através do Big Query, ferramenta de consulta de Big Data do Google que permite a consulta de dados relevantes de tendências (trends) gratuitamente ou com um custo mínimo, dependendo da forma como for implantada e do grau de utilização.  

Para isso, a nossa área técnica desenvolveu um script em Python que, busca os dados de tendências de pesquisa no Big Query e grava os resultados em um arquivo de Excel.

Alguns detalhes de implementação já foram pensados, como:  

* Limitar a quantidade de pesquisas para minimizar o impacto de custo de processamento no Google;
* Determinar uma forma de padronizar os nomes dos arquivos para que os mesmos facilitem a identificação histórica de sua criação e a qual período ele se refere (utilizando o campo "week");  
  
Para efeitos de apresentação de um mínimo produto viável (MVP), foi criada uma lista de 10 linhas contendo as tendências a partir da menor data disponível no Big Query, que remonta ao ano de 2018.

