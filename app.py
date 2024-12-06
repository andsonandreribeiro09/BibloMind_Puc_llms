import pandas as pd

# Carregar o arquivo Excel
file_path = "Acervo MB.xlsx"

# Ler a planilha
try:
    df = pd.read_excel(file_path, sheet_name='NOVOS LIVROS - AGOSTO e SETEMBR')
    print("Dados carregados com sucesso!")
    print(df.head())  # Exibir as primeiras linhas da planilha
except Exception as e:
    print(f"Erro ao carregar a planilha: {e}")


# Função para gerar termos de indexação
def gerar_termos_indexacao(row):
    termos = set()
    if pd.notna(row['PALAVRAS-CHAVE MB']):
        termos.update(row['PALAVRAS-CHAVE MB'].split(','))
    if pd.notna(row['ÁREA DO CONHECIMENTO MB']):
        termos.add(row['ÁREA DO CONHECIMENTO MB'])
    if pd.notna(row['Título']):
        termos.add(" ".join(row['Título'].split()[:3]))
    if pd.notna(row['AUTORIA']):
        termos.add(row['AUTORIA'].split(';')[0].strip())
    return ', '.join(list(termos)[:5])

# Aplicar a função para preencher a coluna 'Indexação'
df['Indexação'] = df.apply(gerar_termos_indexacao, axis=1)

# Salvar em um novo arquivo Excel
output_path = "planilha_indexada.xlsx"
df.to_excel(output_path, index=False)
print(f"Planilha com indexação salva em {output_path}")
