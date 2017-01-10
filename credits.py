import ui
menu_view = ui.load_view("main_menu_scene.pyui")
def back_touch_up_inside(sender):
	menu_view.present("fullscreen")
view = ui.load_view()
view.present('full_screen')
