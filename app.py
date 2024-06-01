from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import aioredis

app = FastAPI()

# Conjunto para armazenar os clientes conectados
app.state.clients = set()

# Conectar ao Redis
redis: aioredis.Redis = None

@app.on_event("startup")
async def startup_event():
    global redis
    redis = await aioredis.from_url("redis://localhost")

@app.on_event("shutdown")
async def shutdown_event():
    redis.close()
    await redis.wait_closed()

# Montar a pasta 'static' para servir os arquivos estáticos (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rota principal para servir o arquivo HTML
@app.get("/", response_class=HTMLResponse)
async def index():
    html_path = Path(__file__).resolve().parent / "templates" / "index.html"
    return html_path.read_text()

# Rota WebSocket para lidar com a conexão do cliente
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    app.state.clients.add(websocket)  # Adiciona o cliente à lista de clientes conectados
    try:
        while True:
            data = await websocket.receive_text()
            await send_message(data)  # Envia a mensagem para todos os clientes conectados
    finally:
        app.state.clients.remove(websocket)  # Remove o cliente da lista ao desconectar

# Função para enviar mensagem para todos os clientes conectados e salvar no Redis
async def send_message(message: str):
    for client in app.state.clients:
        await client.send_text(message)
    await save_message(message)

# Função para salvar mensagem no Redis
async def save_message(message: str):
    await redis.rpush("chat", message)
