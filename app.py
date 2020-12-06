import logging
import os.path
import sys

import aiohttp
import aiohttp_jinja2
import jinja2

from handlers.graphql import GraphqlHandler
from handlers.graphiql import GraphiqlHandler

class Application(aiohttp.web.Application):

    def __init__(self):
        super().__init__()
        self.register_handlers()

    # A função desse método é inicializar todo os serviços da aplicação,
    # é chamado no event loop em server.py logo quando o servidor inicializa
    async def initialize(self):
        await self.initialize_jinja2()
        # await self.servico1()
        # await self.servico1()
        # await self.servico1()

    def register_handlers(self):
        routes = [(r'/graphql', GraphqlHandler)] # Rotas do sistema

        #if self.dev:
        routes += [(r'/graphiql', GraphiqlHandler)] # Rotas do sistema para desenvolvedores

        self.router.add_routes([aiohttp.web.view(route[0], route[1]) for route in routes])

    async def initialize_jinja2(self): # Serviço jinja2
        aiohttp_jinja2.setup(self,
            loader=jinja2.FileSystemLoader('./templates'))
