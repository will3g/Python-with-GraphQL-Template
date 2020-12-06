import asyncio
from aiohttp import web
from app import Application

# Essa função tem como objetivo chamar a classe principal do sistema
def get_app():
    return Application()

if __name__ == '__main__':
    app = get_app() # Aqui instânciamos a classe Application
    loop = asyncio.get_event_loop() # Nessa linha é chamado o event-loop do aiohttp
    loop.run_until_complete(app.initialize()) # Nessa linha passamos os nossos serviços do método initialize para o event-loop
    web.run_app(app) # Nessa linha a função web do aiohttp executa a instância da classe Application e sobe o servidor da aplicação