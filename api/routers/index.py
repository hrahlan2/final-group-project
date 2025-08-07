from . import orders, order_details, reviews, resources, guest_orders, delivery_options, payments


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(reviews.router)
    app.include_router(resources.router)
    app.include_router(guest_orders.router)
    app.include_router(menu_items.router)
    app.include_router(delivery_options.router)
    app.include_router(payments.router)
