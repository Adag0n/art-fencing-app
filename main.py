import sys
import requests
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

URL_API = "http://10.0.2" 

class ArtFencingApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        from kivy.core.window import Window
        Window.clear_color = (0.08, 0.08, 0.1, 1)
        
        box.add_widget(Label(
            text="⚔️ АРТ-ФЕХТОВАНИЕ", 
            font_size='32sp', 
            bold=True, 
            color=(0.75, 0.55, 0.15, 1),
            size_hint_y=None,
            height='100dp'
        ))
        
        box.add_widget(Label(
            text="Мобильное приложение судейства\nи управления боевыми номерами", 
            font_size='16sp', 
            halign='center',
            color=(0.8, 0.8, 0.8, 1)
        ))
        
        btn = Button(
            text="ПОДКЛЮЧИТЬСЯ К БАЗЕ ДАННЫХ",
            size_hint_y=None,
            height='60dp',
            background_normal='',
            background_color=(0.75, 0.55, 0.15, 1),
            font_size='18sp'
        )
        box.add_widget(btn)
        return box

if __name__ == '__main__':
    ArtFencingApp().run()
