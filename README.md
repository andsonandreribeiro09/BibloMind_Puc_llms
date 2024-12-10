Denominado de BibloMind_Puc

E Uma Arquitetura do Sistema de Indexação Automática

Entrada de Dados

Fontes: O Excel será usado como ponto de entrada inicial para os metadados do acervo, como título, resumo, e outros campos relevantes.

Automação: Utilizar VBA ou Python (com openpyxl ou pandas) para enviar os dados automaticamente para a API do modelo de linguagem.

Modelo de Linguagem Local

Ferramenta: Usar o Ollama como base para rodar modelos como Llama 2, Mistral, ou similares localmente.

Personalização: Treinar ou ajustar o modelo com um vocabulário controlado, contendo termos e classificações já utilizadas na biblioteca.

Saída: 

Configurar o modelo para sugerir:

Um número de classificação (baseado em padrões como CDD ou CDU, se aplicável).
Três a cinco palavras-chave contextuais.

Processamento e Feedback

Integrar o modelo com uma interface que permita ajustes manuais às sugestões feitas (para refinar o aprendizado com o vocabulário da biblioteca).
Salvar os dados processados no Excel ou diretamente em um sistema de gerenciamento de acervo.

Integração de API

Usar uma API REST local gerenciada pelo Ollama para interagir com o modelo.

Ferramentas:

FastAPI ou Flask para criar endpoints locais de envio e recepção.
Scripts Python para ler os dados do Excel, enviar para a API, e atualizar as sugestões no arquivo.


Aprendizado Contínuo

Feedback Loop: Armazenar as classificações e palavras-chave aprovadas em uma base de dados para treinar novamente o modelo, incorporando correções e novas tendências de uso.

Atualização do Vocabulário: Adicionar termos automaticamente a partir de revisões feitas pelos bibliotecários.

Ferramentas Necessárias

Ollama: Para hospedar os modelos de linguagem.

Excel + VBA ou Python: Para lidar com dados estruturados e automação.

FastAPI/Flask: Para comunicação entre o Excel e o modelo de linguagem.

Base de Dados: SQLite ou PostgreSQL para armazenamento do vocabulário controlado e do histórico de sugestões.


Modelos LLM Open Source:

Llama 2: Foco em compreensão geral de textos e personalização.

Mistral: Mais leve, ideal para uso em ambientes locais com menos hardware.

Falcon ou GPT-NeoX: Alternativas se precisarem de maior compreensão de contexto.
Fluxo do Sistema

O sistema lê os dados de Título e Resumo no Excel.

Os dados são enviados para o modelo LLM via API.

O modelo sugere o número de classificação e as palavras-chave.

As sugestões são revisadas manualmente (se necessário).
As informações finais são salvas e o vocabulário controlado é atualizado.

Próximos Passos

Definir o Vocabulário Controlado Inicial:

Levantar os termos e classificações atualmente usados na biblioteca.

Configurar o Ollama e o Modelo LLM:

Escolher um modelo adequado e testar localmente.

Criar a Integração com Excel e API:

Decidir entre VBA ou Python para automação.

Prototipar o Sistema:

Configurar o fluxo end-to-end e ajustar conforme o feedback dos usuários.
