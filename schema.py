import graphene

from schemas.schema_hello import Query

# Aqui é onde fica todas as querys/schema do sistema
class AllQuery(
    Query,
    # Schema1,
    # Schema2,
    # Schema3
):
    '''AllQuery'''