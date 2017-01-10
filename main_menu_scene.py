# coding: utf-8

import ui
menu_view = ui.load_view("main_menu_scene.pyui")
test_view = ui.load_view("test_average.pyui")
credits_view = ui.load_view("credits.pyui")

def test_touch_up(sender):
	test_view.present("fullscreen")

def credits_touch_up(sender):
	credits_view.present("fullscreen")

view = ui.load_view()
view.present('fullscreen')
