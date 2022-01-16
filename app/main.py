import kivy
import time
import sqlite3
import errno, os
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


con=sqlite3.connect('db/kivy_android.db')
cursor=con.cursor()


if platform == "android":
  from android.permissions import request_permissions, Permission
  request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])


# if platform not in ('android', 'ios'):
#   Config.set('graphics', 'resizable', '0')
#   Window.size = (310, 520)



class LblTxt(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        # # Anchor Layout2
        # anchorLayout2    = AnchorLayout()
        # anchorLayout2.anchor_x = 'right'
        # anchorLayout2.anchor_y = 'top'
        #
        # # Add the anchor layouts to a box layout
        # button2 = Button(text='Top-Right', size_hint = (0.3, 0.3))
        # anchorLayout2.add_widget(button2)
        #
        # # Create a box layout
        # boxLayout = BoxLayout()
        #
        # # Add both the anchor layouts to the box layout
        # boxLayout.add_widget(anchorLayout2)
        # self.add_widget(boxLayout)



        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Genre: "))
        self.genre = TextInput(multiline=False)
        self.inside.add_widget(self.genre)

        self.inside.add_widget(Label(text="Série: "))
        self.serie = TextInput(multiline=False)
        self.inside.add_widget(self.serie)

        self.inside.add_widget(Label(text="Numéro: "))
        self.numero = TextInput(multiline=False)
        self.inside.add_widget(self.numero)

        self.inside.add_widget(Label(text="Personnage: "))
        self.personnage = TextInput(multiline=False)
        self.inside.add_widget(self.personnage)

        self.inside.add_widget(Label(text="Exclusivité: "))
        self.exclusivite = TextInput(multiline=False)
        self.inside.add_widget(self.exclusivite)

        self.inside.add_widget(Label(text="Commentaire: "))
        self.commentaire = TextInput(multiline=True)
        self.inside.add_widget(self.commentaire)

        self.inside.add_widget(Label(text="Prix achat: "))
        self.prix_achat = TextInput(multiline=False)
        self.inside.add_widget(self.prix_achat)

        self.inside.add_widget(Label(text="Prix vente: "))
        self.prix_vente = TextInput(multiline=False)
        self.inside.add_widget(self.prix_vente)

        # self.inside.add_widget(Label(text="Photo couverture: "))
        # self.photo_couverture = TextInput(multiline=False)
        # self.inside.add_widget(self.photo_couverture)
        #
        # self.inside.add_widget(Label(text="Photo vente: "))
        # self.photo_vente = Button(text="Prendre photo")
        # self.inside.add_widget(self.photo_vente)

        self.add_widget(self.inside)

        self.btn_validation = Button(text="Valider")
        self.add_widget(self.btn_validation)
        self.btn_validation.bind(on_press=self.validate_form)

        # self.btn_photo = Button(text="Prendre")
        # self.btn_photo.bind(on_press=self.take_picture)
        # self.inside.add_widget(self.btn_photo)
        #
        # self.camera = Camera(play=True,index=1)
        # self.inside.add_widget(self.camera)



    def validate_form(self, *args):
        print(self.serie.text)


    def take_picture(self, *args):
        print("Take_picture function called")
        timestr = time.strftime("%Y%m%d_%H%M%S")
        try:
            os.makedirs('snapshots')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.camera.export_to_png("snapshots/IMG_{}.png".format(timestr))
        print("Captured snapshots/IMG_{}.png".format(timestr))














class AccueilScreen(Screen):
    pass

class CollectionScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")



class MyApp(App):

    def build(self):
        return presentation

        # cursor.execute("select * from Type_Collection")
        # rows = cursor.fetchall()
        #
        # for row in rows:
        #     print(row)

        # return MyGrid()

if __name__ == '__main__':
    MyApp().run()
