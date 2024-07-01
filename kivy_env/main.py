from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

class HelloWorldScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        # Cargar el archivo KV
        return Builder.load_file('hello_world.kv')

if __name__ == '__main__':
    MainApp().run()
