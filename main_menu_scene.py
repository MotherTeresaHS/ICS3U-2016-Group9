# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui

from main_menu_scene import *


class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
# Created by: Margaret Venes
# Created on: December 2016
# Created for: ICS3U
# This scene shows the main menu scene.

from scene import *
import ui
from credits import *
from test import *
from main_menu_scene import *
from tests import *
from copy import deepcopy

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add MT blue background color
        self.size_of_screen = deepcopy(self.size)
        self.center_of_screen = deepcopy(self.size/2)
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        
        credits_button_position = deepcopy(self.center_of_screen)
        credits_button_position.x = 800
        credits_button_position.y = 100
        self.credits_button = SpriteNode('./sprites/assets/next.png',
                                       parent = self,
                                       position = credits_button_position)
                                       
        test_button_position = deepcopy(self.center_of_screen)
        test_button_position.x = 200
        test_button_position.y = 650
        self.test_button = SpriteNode('./sprites/assets/next.png',
                                      parent = self,
                                      position = test_button_position)
                                      
        tests_button_position = deepcopy(self.center_of_screen)
        tests_button_position.x = 800
        tests_button_position.y = 650
        self.tests_button = SpriteNode('./sprites/assets/next.png',
                                      parent = self,
                                      position = tests_button_position)
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditsScene())
            
        if self.test_button.frame.contains_point(touch.location):
            self.present_modal_scene(TestScene())
            
        if self.tests_button.frame.contains_point(touch.location):
            self.present_modal_scene(TestsScene())
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
