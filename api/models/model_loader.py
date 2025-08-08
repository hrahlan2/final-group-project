from . import orders, order_details, customers, menu_items, resources, promotions, reviews, payment, delivery_options, order_items

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    delivery_options.Base.metadata.create_all(engine)
