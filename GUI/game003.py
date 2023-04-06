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
from kivy.clock import Clock
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
        Window.unbind(on_mouse_down=self.on_click)
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
        Text = "[size=60]Connecting...[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)
        Clock.schedule_once(self.change_screen, 3)  # Change screen after 5 seconds
    
    def change_screen(self, dt):
        self.manager.current = 'mainS'

class mainScreen(Screen):
    def on_enter(self):
        print('this is the mainscreen of the game')
        mainLayout = GridLayout(cols=1, rows=3, padding=10)
        Text = "[size=20]A HENCHMAN's MISSION:[/size]\n[size=40]STOP THE RESCUE ROBOT![/size]"
        self.gameNameLabel = Label(text=Text, markup=True)
        mainLayout.add_widget(self.gameNameLabel)

        self.playmodeBut = Button(text='PLAY MODE', size_hint=(None, None), size=(300, 100))
        self.playmodeBut.bind(on_release=self.playmode_callback)
        mainLayout.add_widget(self.playmodeBut)

        self.htpBut = Button(text='HOW TO PLAY', size_hint=(None, None), size=(300, 100))
        self.htpBut.bind(on_release=self.htp_callback)
        mainLayout.add_widget(self.htpBut)

        self.add_widget(mainLayout)

    def playmode_callback(self, instance):
        print("play mode button's clicked")

    def htp_callback(self, instance):
        print("how to play button's clicked")

# class popup_playmode(Screen):
#     def on_enter(self):
#         playmodePopLayout = GridLayout(cols = 1,rows =4 padding = 10)


class HMmission_stoptheRescueRobot(App):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(openingScreen(name='openS'))
        self.sm.add_widget(popup1_Screen(name='pop1'))
        self.sm.add_widget(connectingScreen(name='connectS'))
        self.sm.add_widget(mainScreen(name='mainS'))
        return self.sm
    
if __name__ == '__main__':
    HMmission_stoptheRescueRobot().run()