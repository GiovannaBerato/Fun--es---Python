import pandas as pd

filmes = pd.read_csv('movies/tmdb_5000_credits.csv')

# Visualizando as primeiras linhas
print(filmes.head())

# Selecionando as colunas de interesse
filmes_subset = filmes[['title', 'cast']]

# Visualizando os dados das colunas selecionadas
print(filmes_subset.head())

# DESAFIO 

def encontrarator(filmes, nome_ator):
    # Crie uma lista para armazenar os filmes onde o ator foi encontrado
    filmes_encontrados = []

# Itere sobre as linhas do DataFrame
    for row in filmes.iterrows():elenco = row["cast"]
    
# Pegue o conteúdo da coluna 'Elenco'

# Verifique se o nome do ator está na string do elenco
    if nome_ator in elenco:filmes_encontrados.append(row["title"])  
    
    # Adicione o título do filme à lista

    return filmes_encontrados

print(f"Filmes com o ator {nome_ator}:")
for filme in filmes:
    print(filme, " | ", nome_ator)

