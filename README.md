Linkbolt Leads

Ferramenta simples para buscar leads de transportadoras, distribuidoras, operadores logísticos, centros de distribuição, atacadistas, indústrias e outros negócios com alta demanda de roteirização, gestão de frotas e otimização de entregas.

O usuário edita três listas:

    config/keywords.txt: palavras-chave.

    config/location.txt: bairros, cidades, polos industriais, regiões ou recortes geográficos.

    config/categorias_permitidas.txt: categorias do Google Maps que fazem sentido para triagem de operações logísticas e distribuição.

O programa cruza as listas automaticamente, roda o Google Maps Scraper, organiza os dados, tenta complementar contatos em sites e Instagram, e salva a planilha final em results/.

A planilha final já sai com telefones padronizados, horários mais legíveis e apenas as colunas mais úteis para prospecção B2B.
Como baixar do GitHub
Jeito mais simples, sem Git

    Abra o repositório no GitHub: [https://github.com/alexkwok95/linkbolt-leads](https://github.com/alexkwok95/linkbolt-leads) (ajuste o link caso o nome do repositório esteja diferente).

    Clique no botão verde Code.

    Clique em Download ZIP.

    Abra o .zip baixado.

    Mova a pasta para um lugar fácil, por exemplo Documentos/Linkbolt.

Jeito pelo Terminal, com Git
Bash

cd ~/Documents
git clone https://github.com/alexkwok95/linkbolt-leads.git
cd linkbolt-leads

Requisitos

Antes de rodar, instale:

    Docker Desktop: https://www.docker.com/products/docker-desktop/

    Python 3

Para conferir o Python:
Bash

python3 --version

Antes de buscar leads, abra o Docker Desktop e espere ele ficar ativo.
Instalar / verificar

Na pasta do projeto, dê dois cliques em:
Plaintext

instalar_linkbolt.command

(ou instalar.command, conforme o nome salvo na pasta)

Esse arquivo verifica Python, Docker, permissões e já gera o arquivo interno de buscas.
Como rodar

Dê dois cliques em:
Plaintext

rodar_linkbolt.command

O programa pergunta apenas:
Plaintext

Modo de busca:
1 [rápido]
2 [equilibrado]
3 [máxima cobertura]

Tempo de inatividade antes de encerrar [1m]:

Depois ele faz tudo automaticamente:

    Gera as buscas combinando keywords.txt + location.txt.

    Roda o Google Maps Scraper.

    Transforma o resultado bruto em planilha Linkbolt e já classifica a aderência ao ICP.

    Complementa contatos encontrados nos sites dos leads marcados como Sim ou Revisar.

    Complementa contatos encontrados em perfis públicos de Instagram dos leads marcados como Sim ou Revisar.

    Limpa e padroniza a planilha final.

    Salva a planilha final.

    Mostra um resumo.

Modos de busca

Use:

    1 [rápido]: menor profundidade e maior paralelismo controlado. Bom para teste ou primeira varredura rápida.

    2 [equilibrado]: equilíbrio entre cobertura e tempo. Recomendado para uso normal.

    3 [máxima cobertura]: maior profundidade, todos os locais/palavras-chave e concorrência conservadora para preservar estabilidade e cobertura.

Internamente, o programa converte:

    1 [rápido]: Google Maps depth 1, mais workers para site/Instagram.

    2 [equilibrado]: Google Maps depth 5, workers moderados.

    3 [máxima cobertura]: Google Maps depth 10, workers mais conservadores.

A opção 3 ainda pode demorar bastante em grandes polos comerciais e industriais. A otimização reduz retrabalho e paraleliza etapas seguras, mas não inventa dados nem pula regiões/palavras-chave.
Otimizações de velocidade

O programa usa:

    concorrência controlada no Google Maps;

    deduplicação antes do enriquecimento;

    cache local para sites e Instagram já analisados;

    enriquecimento paralelo de sites e perfis públicos de Instagram.

O cache fica em:
Plaintext

data/cache/

Se quiser forçar uma busca totalmente nova nos sites/Instagram, apague essa pasta.
Tempo de inatividade

O padrão é:
Plaintext

1m

Isso significa que o scraper encerra quando fica 1 minuto sem encontrar novos resultados. Você pode alterar antes de rodar, por exemplo:
Plaintext

3m

Como editar palavras-chave

Abra:
Plaintext

config/keywords.txt

Cada linha é uma palavra-chave.

Exemplo:
Plaintext

transportadora
distribuidora
operador logístico
centro de distribuição
logística e transportes
atacadista
distribuidora de alimentos
distribuidora de bebidas
frota própria
entrega rápida

Como editar locais

Abra:
Plaintext

config/location.txt

Cada linha é um local. Pode ser bairro, cidade, polo industrial, distrito ou recorte comercial.

Exemplo:
Plaintext

Distrito Industrial, Maracanaú CE
Messejana, Fortaleza CE
Eusébio CE
Juazeiro do Norte CE
Sobral CE

O programa combina automaticamente:
Plaintext

keyword + location

Exemplo:
Plaintext

transportadora em Distrito Industrial, Maracanaú CE
distribuidora em Messejana, Fortaleza CE
operador logístico em Eusébio CE

Como editar categorias permitidas

Abra:
Plaintext

config/categorias_permitidas.txt

Cada linha é uma categoria do Google Maps que pode fazer sentido na triagem. A lista não força Sim para tudo: categorias logísticas/atacadistas diretas entram como Sim, categorias genéricas permitidas sem sinal claro de operação de entrega/frota entram como Revisar, e categorias fora da lista entram como Não.

Exemplos:

    Transportadora, Serviço de logística, Distribuidora, Atacadista, Armazém: tendem a Sim.

    Indústria, Comércio atacadista, Depósito, Fornecedor de alimentos: entram como Revisar se não houver sinal claro de frota ou distribuição.

    Restaurante, Salão de beleza, Clínica médica, Loja de roupas, Escola: entram como Não, salvo se houver um sinal forte de operação de distribuição/logística.

Onde sai o resultado

O resultado principal fica em:
Plaintext

results/results.csv

O programa também mantém histórico em:
Plaintext

results/results_YYYYMMDD_HHMMSS.csv

Assim, o arquivo results.csv é sempre o mais recente, e os arquivos com data/hora preservam execuções antigas.

O resultado final remove colunas internas de auditoria e mantém os principais campos comerciais:

    ID

    Tipo de lead

    Nome do lead

    Categoria

    Cidade

    Estado

    Bairro

    Endereço completo

    Horário de funcionamento

    Telefones e WhatsApps

    Link Google Maps

    Nota e número de avaliações

    Instagram

    Site

    Potencial para roteirização / logística

    Score comercial

    Prioridade

    Faz sentido?

    Motivo do filtro

As colunas Faz sentido? e Motivo do filtro ajudam a revisar ruídos da busca profunda. Exemplos:

    Sim: há indício claro de transporte de cargas, distribuição, atacado, frota ou operação logística.

    Revisar: a categoria está na lista permitida, mas é genérica, como comércio, indústria ou depósito sem sinal claro de rotas de entrega.

    Não: a categoria está fora da lista permitida ou há indício forte de que não faz parte do ICP (varejo local sem entrega, serviços médicos, estética, alimentação no local etc.).

Essa avaliação olha o nome do lead, categoria, endereço, site e tipo de lead. Nomes com indício logístico/atacadista — como Trans, Log, Express, Cargas, Distribuidora, Atacado, Frotas, Entregas, CD e similares — ajudam a classificar o lead como aderente mesmo quando a categoria do Google vem genérica.

O programa não exclui automaticamente os leads marcados como Não; ele preserva tudo para você auditar e filtrar na planilha.
Arquivos internos

A pasta data/ guarda arquivos intermediários necessários para o fluxo:

    consultas geradas;

    CSV bruto do Google Maps;

    CSV normalizado;

    CSV enriquecido por site;

    CSV enriquecido por Instagram.

O usuário final normalmente só precisa abrir results/results.csv.

Os intermediários em data/processed/ podem ter mais colunas do que o resultado final. Isso é intencional: eles servem para auditoria e depuração.
Se o Mac bloquear o instalador

Se aparecer uma mensagem dizendo que a Apple não pode verificar instalar_linkbolt.command, faça assim:

    Clique em OK.

    Clique com o botão direito em instalar_linkbolt.command.

    Escolha Abrir.

    Confirme em Abrir novamente.

Se não aparecer a opção, abra Ajustes do Sistema > Privacidade e Segurança e clique em Abrir Mesmo Assim.

Pelo Terminal, também funciona:
Bash

xattr -dr com.apple.quarantine .
chmod +x *.command scripts/*.py scripts/*.sh
./instalar_linkbolt.command

Limitações

O fluxo atual automatiza:

    Google Maps.

    Sites das próprias transportadoras, distribuidoras e empresas.

    Extração simples de telefone, WhatsApp e Instagram quando aparecem publicamente no site.

    Extração de telefone/WhatsApp em perfis públicos de Instagram quando a planilha já tem o link do perfil.

    Leitura do link da bio do Instagram quando ele aponta para WhatsApp, agregador de links, catálogo ou site institucional.

O Instagram pode bloquear leitura automática ou esconder dados. A etapa de Instagram funciona melhor quando o perfil é público e o WhatsApp está na bio ou no link da bio.

Portais B2B, diretórios de fretes e bases governamentais (como ANTT/Receita) ainda não estão automatizados neste repositório e podem entrar como módulos separados em uma fase futura.
Qual modo usar?

    Para uso normal por região ou polo industrial, comece com 2 [equilibrado]. Ele costuma trazer boa cobertura com menos ruído e menos tempo.

    Use 3 [máxima cobertura] quando quiser varrer o máximo possível de uma cidade ou estado. Ele pode trazer mais ruído, porque o Google Maps aprofunda resultados relacionados de forma ampla. Para isso, use as colunas Faz sentido? e Motivo do filtro para filtrar o que não pertence ao ICP.

Estrutura do repositório
Plaintext

README.md
instalar_linkbolt.command
rodar_linkbolt.command
config/
  keywords.txt
  location.txt
  categorias_permitidas.txt
scripts/
data/
results/
