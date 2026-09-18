import pandas as pd
dados = {
    "Nome": ["João", "Carlos", "Daniel", "Leonardo"],
    "Idade": ["27", "21", "32", "18"],
    "Cidade": ["Maringá", "Curitiba", "Londrina", "Telêmaco Borba"]

}

df = pd.DataFrame(dados)
print(df)
