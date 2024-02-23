from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.testclient import TestClient

app = FastAPI()

produto = {"id": 1, "nome": "Notebook", "preco": 2500.00, "estoque": 50}

carro = {"id": 1, "marca": "Toyota", "modelo": "Corolla", "ano": 2020, "preco": 50000}

cor = {"id": 1, "nome": "Azul", "hex": "#0000FF"}

animal = {"id": 1, "nome": "Cachorro", "especie": "Canis lupus familiaris", "idade": 5}

fruta = {"id": 1, "nome": "Maçã", "tipo": "Fruta", "cor": "Vermelha", "preco": 2.50}

@app.get("/produto", response_class=JSONResponse)
async def obter_produto_json():
    return produto

@app.get("/carro", response_class=JSONResponse)
async def obter_carro_json():
    return carro

@app.get("/cor", response_class=JSONResponse)
async def obter_cor_json():
    return cor

@app.get("/animal", response_class=JSONResponse)
async def obter_animal_json():
    return animal

@app.get("/fruta", response_class=JSONResponse)
async def obter_fruta_json():
    return fruta

@app.get("/", response_class=HTMLResponse)
async def obter_dados_html():
    html_content = f"""
    <html>
        <head>
            <title>Dados HTML</title>
        </head>
        <body>
            <h1>Dados HTML</h1>
            <h2>Produto</h2>
            <p>ID: {produto['id']}</p>
            <p>Nome: {produto['nome']}</p>
            <p>Preço: R${produto['preco']:.2f}</p>
            <p>Estoque: {produto['estoque']}</p>
            <h2>Carro</h2>
            <p>ID: {carro['id']}</p>
            <p>Marca: {carro['marca']}</p>
            <p>Modelo: {carro['modelo']}</p>
            <p>Ano: {carro['ano']}</p>
            <p>Preço: R${carro['preco']:.2f}</p>
            <h2>Cor</h2>
            <p>ID: {cor['id']}</p>
            <p>Nome: {cor['nome']}</p>
            <p>Hex: {cor['hex']}</p>
            <h2>Animal</h2>
            <p>ID: {animal['id']}</p>
            <p>Nome: {animal['nome']}</p>
            <p>Espécie: {animal['especie']}</p>
            <p>Idade: {animal['idade']}</p>
            <h2>Fruta</h2>
            <p>ID: {fruta['id']}</p>
            <p>Nome: {fruta['nome']}</p>
            <p>Tipo: {fruta['tipo']}</p>
            <p>Cor: {fruta['cor']}</p>
            <p>Preço: R${fruta['preco']:.2f}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

client = TestClient(app)

def test_obter_produto_json():
    response = client.get("/produto")
    assert response.status_code == 200
    assert response.json() == produto

def test_obter_carro_json():
    response = client.get("/carro")
    assert response.status_code == 200
    assert response.json() == carro

def test_obter_cor_json():
    response = client.get("/cor")
    assert response.status_code == 200
    assert response.json() == cor

def test_obter_animal_json():
    response = client.get("/animal")
    assert response.status_code == 200
    assert response.json() == animal

def test_obter_fruta_json():
    response = client.get("/fruta")
    assert response.status_code == 200
    assert response.json() == fruta
