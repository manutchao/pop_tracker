import kivy
import kivymd
import time
import errno, os
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivymd.app import MDApp



if platform == "android":
  from android.permissions import request_permissions, Permission
  request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE])


if platform not in ('android', 'ios'):
  Config.set('graphics', 'resizable', '0')
  Window.size = (310, 520)


class TrackerApp(MDApp):

    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"





if __name__ == "__main__":
    TrackerApp().run()
