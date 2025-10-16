import pandas as pd
import re

# caminho do arquivo original
caminho = "data/pib_municipal_2021.csv"

# ler a base
df = pd.read_csv(caminho)

# renomear colunas para facilitar
df = df.rename(columns={
    "V": "pib_mil_reais",
    "D1N": "municipio_nome"
})

# extrair a sigla do estado do nome do município (depois do " - ")
df["UF"] = df["municipio_nome"].apply(lambda x: re.search(r"-\s*([A-Z]{2})$", x).group(1) if re.search(r"-\s*([A-Z]{2})$", x) else None)

# converter PIB para número
df["pib_mil_reais"] = pd.to_numeric(df["pib_mil_reais"], errors="coerce")

# agrupar por UF e somar
pib_estadual = df.groupby("UF", as_index=False)["pib_mil_reais"].sum()

# criar coluna em bilhões para facilitar a leitura
pib_estadual["pib_bilhoes"] = (pib_estadual["pib_mil_reais"] / 1_000_000).round(2)

# salvar resultado
pib_estadual.to_csv("data/pib_estadual_2021.csv", index=False, encoding="utf-8-sig")

print("✅ PIB estadual 2021 calculado com sucesso!")
print(pib_estadual)
