import geopandas as gpd
import pandas as pd

# Caminho do shapefile
caminho = "data/PRODES_AMZ_Municipal_2023.shp"

# Ler o shapefile
gdf = gpd.read_file(caminho)

print("Colunas encontradas no shapefile:")
print(gdf.columns)


# Agrupar por estado e ano, somando área total desmatada
# Salvar como CSV

gdf.to_csv('data/desmatamento_por_estado.csv', index=False)

print("✅ Arquivo CSV agregado salvo com sucesso em data/desmatamento_por_estado.csv")
