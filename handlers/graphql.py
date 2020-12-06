import graphene

from handlers import GQLBaseHandler
from schema import AllQuery

class GraphqlHandler(GQLBaseHandler):

    @property
    def schema(self):
        # Adiciona AllQuery em graphene.Schema
        return graphene.Schema(query=AllQuery)
