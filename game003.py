import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
# from kivy.lang.builder import Builder
# from kivymd.app import MDApp


class openingScreen(Screen):
    def __init__(self, **kw):
        super(openingScreen, self).__init__(**kw)
        Text = "[size=36]A HENCHMAN's MISSION:[/size]\n[size=60]STOP THE RESCUE ROBOT![/size]"
        self.gamename = Label(text=Text, markup=True, opacity=0)
        self.add_widget(self.gamename)
        self.fadename = Animation(opacity=1, duration=2)
        self.fadename.start(self.gamename)
        Window.bind(on_mouse_down=self.on_click)

    def on_click(self, window, mouse_x, mouse_y, *args):
        # create pop-up box with message
        self.clear_widgets()
        print("window's clicked")
        self.manager.current = 'pop1'


class popup1_Screen(Screen):
    def on_enter(self):
        connectPopLayout = GridLayout(cols = 1, padding = 10)
        popLable = Label(text='Please Connect the ROBOT!',font_size = 28)
        self.connectButton = Button(text='Connect')
        self.connectButton.bind(on_release = self.connect_callback)
        connectPopLayout.add_widget(popLable)
        connectPopLayout.add_widget(self.connectButton)
        self.popup = Popup(title='',content= connectPopLayout, size_hint=(None, None), size=(400, 200))
        self.popup.open()

    def connect_callback(self,instance):
        self.clear_widgets()
        self.popup.dismiss()
        print("connect button's clicked")
        self.manager.current = 'connectS'

class connectingScreen(Screen):
    def on_enter(self):
        self.clear_widgets()
        Text = "[size=60]Connecting...[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)


class HMmission_stoptheRescueRobot(App):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(openingScreen(name='openS'))
        self.sm.add_widget(popup1_Screen(name='pop1'))
        self.sm.add_widget(connectingScreen(name='connectS'))
        return self.sm
    
if __name__ == '__main__':
    HMmission_stoptheRescueRobot().run()