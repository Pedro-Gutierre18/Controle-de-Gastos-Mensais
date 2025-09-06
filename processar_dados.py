import pandas as pd
import sys

print("Iniciando o script de processamento de dados..")

try:
    df_transacoes = pd.read_csv("Planilha sem titulo - Transacoes.csv")
    df_categorias = pd.read_csv("Planilha sem titulo - Categorias.csv")
    
except:
    print("Arquivos não encontrados")
    sys.exit()
    
if 'ID_Categorias' in df_categorias.columns:
    df_categorias.rename(columns={'ID_Categorias': 'ID_Categoria'}, inplace=True)
    print("Coluna 'ID_Categorias 'ID_Categorias' renomeada para 'ID_Categoria'.")
    
if df_categorias['ID_Categoria'].duplicated().any():
    print("Aviso: IDs duplicados encontrados no arquivo de categorias. Removendo duplicatas..")
    df_categorias.drop_duplicates(subset=['ID_Categoria'], keep='first', inplace=True)
    
df_transacoes['Data_Transacao'] = pd.to_datetime(df_transacoes['Data_Transacao'])
print("Colina 'Data_Transacao' convertida para o formato de data.")

print("Unindo os dados de transações com as categorias..")
df_completo = pd.merge(df_transacoes, df_categorias, on='ID_Categoria', how='left')

output_filename = 'dados_tratados.csv'
df_completo.to_csv(output_filename, index=False)

print("-" * 50)
print(f"SUCESSO! O arquivo final '{output_filename}' foi criado.")
print("Este arquivo contém todos os dados unidos e limpos.")
print("-" * 50)