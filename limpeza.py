import pandas as pd
import os

# Caminho da pasta
base_path = "data/limpos/"

# Nomes dos arquivos
arquivos = {
    "populacao": "br_ibge_populacao_estados_limpo.csv",
    "desmatamento": "desmatamento_2021_por_estado.csv",
    "ipeadata": "ipeadata_limpo.csv",
    "pib": "pib_estadual_amazonia_2021.csv"
}

# Função auxiliar pra exibir infos resumidas
def mostrar_info(nome, df):
    print(f"\n=== 📄 {nome.upper()} ===")
    print("Colunas:", list(df.columns))
    print("Tipos:\n", df.dtypes)
    print("Amostra:")
    print(df.head(), "\n")

# Ler e exibir informações de cada base
bases = {}
for nome, arquivo in arquivos.items():
    caminho = os.path.join(base_path, arquivo)
    df = pd.read_csv(caminho)
    bases[nome] = df
    mostrar_info(nome, df)

# 🔎 Verificar colunas de identificação do estado
print("\n=== 🧭 Colunas de identificação (UF / Estado) ===")
for nome, df in bases.items():
    for col in df.columns:
        if "uf" in col.lower() or "estado" in col.lower():
            print(f"{nome}: '{col}'")

# 🔎 Verificar se todas as UFs estão na Amazônia Legal
amazonia_legal = {"AC","AM","AP","MA","MT","PA","RO","RR","TO"}
print("\n=== 🗺️ Estados presentes em cada base ===")
for nome, df in bases.items():
    uf_cols = [c for c in df.columns if "uf" in c.lower()]
    if uf_cols:
        print(f"{nome}: {sorted(set(df[uf_cols[0]].unique()) & amazonia_legal)}")

print("\n✅ Análise concluída!")
