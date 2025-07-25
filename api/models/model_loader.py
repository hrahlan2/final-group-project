from . import (
    orders,
    order_details,
    customers,
    menu_items,
    order_items,
    resources,
    promotions,
    reviews,
    payments
)

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    #promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    #payments.Base.metadata.create_all(engine)