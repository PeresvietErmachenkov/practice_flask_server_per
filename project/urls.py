from .settings import python_app
from home_page import home_app, show_home
from shop_page import shop_app, show_shop_page

home_app.add_url_rule(
    rule = "/",
    view_func = show_home,
    methods = ["GET", "POST"]
)

shop_app.add_url_rule(
    rule = "/shop/",
    view_func = show_shop_page,
    methods = ["GET", "POST"]
)

python_app.register_blueprint(blueprint = home_app)
python_app.register_blueprint(blueprint = shop_app)