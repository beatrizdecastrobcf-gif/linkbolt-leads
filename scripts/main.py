import os
import asyncio
import pandas as pd
from playwright.async_api import async_playwright

def carregar_config(nome_arquivo):
    caminho = os.path.join("config", nome_arquivo)
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return [linha.strip() for linha in f if linha.strip()]
    return []

async def buscar_leads():
    keywords = carregar_config("keywords.txt")
    locations = carregar_config("location.txt")
    
    print(f"=== LINKBOLT LEADS ===")
    print(f"Termos: {keywords}")
    print(f"Locais: {locations}")
    
    # Aqui entra o fluxo automatizado do navegador
    print("Iniciando raspagem com Python e Playwright...")
    
    # Estrutura inicial de resultados
    resultados = []
    
    # Salvar resultados
    os.makedirs("results", exist_ok=True)
    df = pd.DataFrame(resultados, columns=["Nome", "Telefone", "Endereco", "Website", "Categoria"])
    df.to_csv("results/leads_linkbolt.csv", index=False, encoding="utf-8-sig")
    print("Busca concluida! Arquivo salvo em results/leads_linkbolt.csv")

if __name__ == "__main__":
    asyncio.run(buscar_leads())
