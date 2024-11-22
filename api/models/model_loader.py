from . import orders, menu, payment
from ..dependencies.database import engine

def index():
    orders.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)

