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

async def extrair_google_maps():
    keywords = carregar_config("keywords.txt")
    locations = carregar_config("location.txt")
    
    print(f"=== LINKBOLT LEADS — SCRAPER ATIVO ===")
    print(f"Termos: {keywords}")
    print(f"Locais: {locations}")
    
    resultados = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for loc in locations:
            for kw in keywords:
                query = f"{kw} em {loc}"
                print(f"--> Buscando: {query}")
                
                url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
                await page.goto(url)
                await page.wait_for_timeout(3000)
                
                # Extrai os elementos visíveis na busca
                cards = await page.query_selector_all('div[role="article"]')
                
                for card in cards[:5]:  # Pega os 5 primeiros resultados por busca
                    try:
                        nome = await card.get_attribute("aria-label")
                        texto_card = await card.inner_text()
                        
                        resultados.append({
                            "Termo": kw,
                            "Local": loc,
                            "Nome Empresa": nome if nome else "N/A",
                            "Detalhes": texto_card.replace("\n", " | ")
                        })
                    except Exception:
                        continue

        await browser.close()
        
    os.makedirs("results", exist_ok=True)
    df = pd.DataFrame(resultados)
    caminho_csv = "results/leads_linkbolt.csv"
    df.to_csv(caminho_csv, index=False, encoding="utf-8-sig")
    print(f"\n✅ Busca finalizada com sucesso!")
    print(f"📊 Total de leads extraídos: {len(resultados)}")
    print(f"📁 Arquivo atualizado em: {caminho_csv}")

if __name__ == "__main__":
    asyncio.run(extrair_google_maps())
