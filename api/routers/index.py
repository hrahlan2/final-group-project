from . import orders, order_details, reviews, resources, guest_orders


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(reviews.router)
    app.include_router(resources.router)
    app.include_router(guest_orders.router)
