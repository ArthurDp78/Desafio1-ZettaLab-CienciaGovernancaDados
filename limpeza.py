import pandas as pd
import re
import os

# Caminho do arquivo original
caminho = "data/pib_municipal_2021.csv"

# Criar pasta de saída
os.makedirs("data/limpos", exist_ok=True)

# 1️⃣ Ler a base de PIB municipal
df = pd.read_csv(caminho, encoding="utf-8")
print("✅ Base carregada com sucesso!")
print("📊 Linhas:", len(df))

# 2️⃣ Renomear colunas relevantes
df = df.rename(columns={
    "V": "pib_mil_reais",
    "D1N": "municipio"
})

# 3️⃣ Extrair a sigla do estado a partir do nome do município
df["UF"] = df["municipio"].apply(
    lambda x: re.search(r"-\s*([A-Z]{2})$", x).group(1)
    if isinstance(x, str) and re.search(r"-\s*([A-Z]{2})$", x)
    else None
)

# 4️⃣ Converter valores para numérico
df["pib_mil_reais"] = pd.to_numeric(df["pib_mil_reais"], errors="coerce")

# 5️⃣ Filtrar apenas estados da Amazônia Legal
amazonia_legal = ["AC", "AM", "AP", "MA", "MT", "PA", "RO", "RR", "TO"]
df = df[df["UF"].isin(amazonia_legal)]

print("🌳 Estados filtrados (Amazônia Legal):", sorted(df["UF"].unique()))

# 6️⃣ Agrupar por estado e somar PIB
pib_estadual = df.groupby("UF", as_index=False)["pib_mil_reais"].sum()

# 7️⃣ Adicionar PIB em bilhões para facilitar leitura
pib_estadual["pib_bilhoes"] = (pib_estadual["pib_mil_reais"] / 1_000_000).round(2)

# 8️⃣ Salvar resultado
output = "data/limpos/pib_estadual_amazonia_2021.csv"
pib_estadual.to_csv(output, index=False, encoding="utf-8-sig")

print("✅ PIB estadual da Amazônia Legal salvo com sucesso!")
print(pib_estadual)
