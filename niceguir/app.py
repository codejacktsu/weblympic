# import utils.theme as theme
# import utils.home_page as home_page
# import utils.class_example as class_example
# import utils.function_example as function_example

# from nicegui import app, ui


# # @ui.page('/')
# # def index_page() -> None:
# #     with theme.frame('Homepage'):
# #         home_page.content()


# # function_example.create()

# class_example.ClassExample()

# ui.run(title='Modularization Example')

from nicegui import ui

ui.label("Hello")
ui.run()