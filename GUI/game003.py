import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.progressbar import ProgressBar
# from kivy.lang.builder import Builder
# from kivymd.app import MDApp
# Pin

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
        mainLayout = FloatLayout()
        Text = "[size=20]A HENCHMAN's MISSION:[/size]\n[size=40]STOP THE RESCUE ROBOT![/size]"
        self.gameNameLabel = Label(text=Text, markup=True, pos_hint = {'center_x': 0.5,'y':0.2})
        mainLayout.add_widget(self.gameNameLabel)

        self.playmodeBut = Button(text='PLAY MODE', size_hint=(None, None), size=(300, 100), pos_hint = {'center_x':0.5,'y':0.35})
        self.playmodeBut.bind(on_release=self.playmode_callback)
        mainLayout.add_widget(self.playmodeBut)

        self.htpBut = Button(text='HOW TO PLAY', size_hint=(None, None), size=(300, 100), pos_hint = {'center_x':0.5,'y':0.15})
        self.htpBut.bind(on_release=self.htp_callback)
        mainLayout.add_widget(self.htpBut)

        self.add_widget(mainLayout)

    def playmode_callback(self, instance):
        self.manager.current = 'popPlaymode'
        print("play mode button's clicked")


    def htp_callback(self, instance):
        print("how to play button's clicked")
        self.manager.current = 'htp'

class popup_playmode(Screen):
    def on_enter(self):
        print('play mode PAGE')
        playmodePopLayout = FloatLayout()
        self.staticButton = Button(text='STATIC MODE',size_hint=(None, None), size=(300, 100), pos_hint = {'center_x':0.5,'top':0.85})
        self.staticButton.bind(on_release = self.static_callback)
        self.dynamicButton = Button(text='DYNAMIC MODE',size_hint=(None, None), size=(300, 100),pos_hint = {'center_x':0.5,'top':0.55})
        self.dynamicButton.bind(on_release = self.dynamic_callback)
        self.closeButton = Button(text ='X',size_hint=(None, None), size=(50, 50),pos_hint = {'center_x':0.93,'top':1})
        self.closeButton.bind(on_release = self.closePop)
        playmodePopLayout.add_widget(self.closeButton)
        playmodePopLayout.add_widget(self.staticButton)
        playmodePopLayout.add_widget(self.dynamicButton)
        self.popup = Popup(title='Select Play Mode',content= playmodePopLayout, size_hint=(None, None), size=(400, 500))
        self.popup.open()

    def static_callback(self, instance):
        print('u r playing in STATIC MODE')
        self.clear_widgets()
        self.popup.dismiss()
        Text = "[size=60]LEVEL 1[/size]\n[size=11](static)[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)
        Clock.schedule_once(self.static_game, 3)  # Change screen after 5 seconds

    def dynamic_callback(self, instance):
        print('u r plaing in DYNAMIC MODE')
        self.clear_widgets()
        self.popup.dismiss()
        Text = "[size=60]LEVEL 1[/size]\n[size=11](dynamic)[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)
        Clock.schedule_once(self.dynamic_game, 3)  # Change screen after 5 seconds
    
    def static_game(self, dt):
        print('go to game LEVEL 1 static')
        self.manager.current = 'L1S'

    def dynamic_game(self, dt):
        print('go to game LEVEL 1 dynamic')
        self.manager.current = 'L1D'

    def closePop(self, instance):
        print('pop-up closed')
        self.popup.dismiss()
        self.manager.current = 'mainS'

class howtoplay(Screen):
    def on_enter(self):
        print('This is HOW TO PLAY page')
        htpLayout = FloatLayout()
        
        headLable = Label(text = "HOW TO PLAY",font_size = 48,pos_hint = {'center_x':0.5,'center_y':0.7})
        description = Label(text = "DescriptionDescriptionDescriptionDescriptionDescriptionDescription\nDescriptionDescriptionDescriptionDescriptionDescriptionDescription\nDescriptionDescriptionDescriptionDescriptionDescriptionDescription\nDescriptionDescriptionDescriptionDescriptionDescriptionDescription",pos_hint = {'center_x':0.5,'top':1})
        backBut = Button(text ='<--',size_hint=(None, None), size=(100, 50))
        backBut.bind(on_release = self.backtomain)

        htpLayout.add_widget(headLable)
        htpLayout.add_widget(description)
        htpLayout.add_widget(backBut)

        self.add_widget(htpLayout)

    def backtomain(self,instance):
        print('back to main button pressed')
        self.manager.current = 'mainS'

class L1_static(Screen):       
    def on_enter(self):
        print('l1 static game start')
        l1_layout = FloatLayout()
        with self.canvas:
            Rectangle(size = (488,420),pos = (150,120)) # size /10 *4
            Color(0,1,0,0.8)
            Rectangle(size = (192,8),pos = (202,264))
            Rectangle(size = (192,8),pos = (406,404))
            Color(1,0.8,0.45,1)
            Ellipse(size=(32,32),pos=(186,252))
            Ellipse(size=(32,32),pos=(582,392))

        l1Label = Label(text = 'LEVEL1', font_size = 30, pos_hint = {'x':0,'y':0.48})

        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.moriaStamina.value = 100

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        self.goal_var = 0
        print(self.goal_var)
        testBut = Button(text = 'goal', size_hint=(None,None), size=(50,30),pos_hint={'x':0.93,'y':0})
        testBut.bind(on_release = self.reachgoal)
        l1_layout.add_widget(testBut)

        l1_layout.add_widget(self.moriaStamina)
        l1_layout.add_widget(l1Label)
        l1_layout.add_widget(moriaLabel)
        l1_layout.add_widget(pauseBut)

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)


        self.add_widget(l1_layout)

    def reachgoal(self,instance):
        print(self.goal_var)
        self.goal_var = 1
        if self.goal_var == 1:
            self.clear_widgets()
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.canvas.clear()
            Text = "[size=60]LEVEL 2[/size]\n[size=11](static)[/size]"
            self.connect = Label(text=Text, markup=True)
            self.add_widget(self.connect)
            self.goal_var = 0
            Clock.schedule_once(self.static_game, 3)  # Change screen after 5 seconds

    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 30
        print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'


    def static_game(self,dt):
        print("L1 ending")
        self.manager.current = 'L2S'

    def pause_callback(self, *args):
        print('pause')
        if self.clock_event:
            Clock.unschedule(self.clock_event)
            self.clock_event = None

        pausePopLayout = FloatLayout()
        resumeBut = Button(text = 'RESUME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.85})
        resumeBut.bind(on_release = self.resume_callback)
        backHome = Button(text = 'HOME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.45})
        backHome.bind(on_release = self.home_callback)
        pausePopLayout.add_widget(resumeBut)
        pausePopLayout.add_widget(backHome)
        self.pausepopup = Popup(title='PAUSE',content= pausePopLayout, size_hint=(None, None), size=(400, 350))
        self.pausepopup.open()
    
    def resume_callback(self, instance):
        print('resume dai jaaa')
        self.pausepopup.dismiss()
        if not self.clock_event:
            self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)

    def home_callback(self,instance):
        print('go back home')
        homeconfirmPopLayout = FloatLayout()
        homeLabel = Label(text = 'HOME ?',font_size = 60,pos_hint = {'center_x':0.5,'y':0.25})
        okBut = Button(text = 'OK',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.25,'top':0.45})
        cancleBut = Button(text = 'CANCLE',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.75,'top':0.45})
        okBut.bind(on_release = self.gotomain)
        cancleBut.bind(on_release = self.cancleCB)
        homeconfirmPopLayout.add_widget(homeLabel)
        homeconfirmPopLayout.add_widget(okBut)
        homeconfirmPopLayout.add_widget(cancleBut)
        self.homepopup = Popup(title='',content= homeconfirmPopLayout, size_hint=(None, None), size=(400, 300))
        self.homepopup.open()

    def gotomain(self,instance):
        print('go to main')
        self.pausepopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()

class vicpop(Screen):
    def on_enter(self):
        victoryPopLayout = FloatLayout()
        vicLabel = Label(text = 'VICTORY !!',font_size = 60,pos_hint = {'center_x':0.5,'y':0.3})
        vicLabel2 = Label(text = "You've saved my princess.",font_size = 22,pos_hint = {'center_x':0.5,'y':0.1})
        backHome = Button(text = 'HOME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.45})
        backHome.bind(on_release = self.home_callback)
        victoryPopLayout.add_widget(vicLabel)
        victoryPopLayout.add_widget(vicLabel2)
        victoryPopLayout.add_widget(backHome)
        self.vicpopup = Popup(title='',content= victoryPopLayout, size_hint=(None, None), size=(400, 300))
        self.vicpopup.open()

    def home_callback(self,instance):
        print('go back home')
        homeconfirmPopLayout = FloatLayout()
        homeLabel = Label(text = 'HOME ?',font_size = 60,pos_hint = {'center_x':0.5,'y':0.25})
        okBut = Button(text = 'OK',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.25,'top':0.45})
        cancleBut = Button(text = 'CANCLE',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.75,'top':0.45})
        okBut.bind(on_release = self.gotomain)
        cancleBut.bind(on_release = self.cancleCB)
        homeconfirmPopLayout.add_widget(homeLabel)
        homeconfirmPopLayout.add_widget(okBut)
        homeconfirmPopLayout.add_widget(cancleBut)
        self.homepopup = Popup(title='',content= homeconfirmPopLayout, size_hint=(None, None), size=(400, 300))
        self.homepopup.open()

    def gotomain(self,instance):
        print('go to main')
        self.vicpopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()
            
class L1_dynamic(Screen):
    def on_enter(self):
        print('Level 1 Dynamic mode game start')
        l1_layout = FloatLayout()
        with self.canvas:
            Rectangle(size = (488,420),pos = (150,120)) # size /10 *4
            Color(0,1,0,0.8)
            Rectangle(size = (192,8),pos = (202,264))
            Rectangle(size = (192,8),pos = (406,404))
            Color(1,0.8,0.45,1)
            Ellipse(size=(32,32),pos=(186,252))
            Ellipse(size=(32,32),pos=(582,392))

        l1Label = Label(text = 'LEVEL1', font_size = 30, pos_hint = {'x':0,'y':0.48})

        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.playerStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.43})
        playerLabel = Label(text = 'You',pos_hint={'x':-0.45,'y':0.44})
        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina.value = 100
        self.playerStamina.value = 100

        leftaimming = Button(text = 'aim Left',size_hint=(None,None),size=(100,50),pos = (150,50))
        rightaimming = Button(text = 'aim Right',size_hint=(None,None),size=(100,50),pos = (540,50))
        leftaimming.bind(state = self.leftaimCB)
        rightaimming.bind(state = self.rightaimCB)

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        self.goal_var = 0
        print(self.goal_var)
        testBut = Button(text = 'goal', size_hint=(None,None), size=(50,30),pos_hint={'x':0.93,'y':0})
        testBut.bind(on_release = self.reachgoal)
        l1_layout.add_widget(testBut)

        l1_layout.add_widget(self.moriaStamina)
        l1_layout.add_widget(self.playerStamina)
        l1_layout.add_widget(playerLabel)
        l1_layout.add_widget(moriaLabel)
        l1_layout.add_widget(pauseBut)
        l1_layout.add_widget(leftaimming)
        l1_layout.add_widget(rightaimming)
        l1_layout.add_widget(l1Label)

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)

        self.add_widget(l1_layout)

    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 10
        # print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'

    def reachgoal(self,instance):
        print(self.goal_var)
        self.goal_var = 1
        if self.goal_var == 1:
            self.clear_widgets()
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.canvas.clear()
            Text = "[size=60]LEVEL 2[/size]\n[size=11](dynamic)[/size]"
            self.connect = Label(text=Text, markup=True)
            self.add_widget(self.connect)
            self.goal_var = 0
            Clock.schedule_once(self.dynamic_game, 3)  # Change screen after 5 seconds

    def dynamic_game(self,dt):
        print("L1 ending")
        self.manager.current = 'L2D'


    def pause_callback(self, *args):
        print('pause')
        if self.clock_event:
            Clock.unschedule(self.clock_event)
            self.clock_event = None

        pausePopLayout = FloatLayout()
        resumeBut = Button(text = 'RESUME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.85})
        resumeBut.bind(on_release = self.resume_callback)
        backHome = Button(text = 'HOME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.45})
        backHome.bind(on_release = self.home_callback)
        pausePopLayout.add_widget(resumeBut)
        pausePopLayout.add_widget(backHome)
        self.pausepopup = Popup(title='PAUSE',content= pausePopLayout, size_hint=(None, None), size=(400, 350))
        self.pausepopup.open()
    
    def resume_callback(self, instance):
        print('resume dai jaaa')
        self.pausepopup.dismiss()
        if not self.clock_event:
            self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)

    def home_callback(self,instance):
        print('go back home')
        homeconfirmPopLayout = FloatLayout()
        homeLabel = Label(text = 'HOME ?',font_size = 60,pos_hint = {'center_x':0.5,'y':0.25})
        okBut = Button(text = 'OK',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.25,'top':0.45})
        cancleBut = Button(text = 'CANCLE',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.75,'top':0.45})
        okBut.bind(on_release = self.gotomain)
        cancleBut.bind(on_release = self.cancleCB)
        homeconfirmPopLayout.add_widget(homeLabel)
        homeconfirmPopLayout.add_widget(okBut)
        homeconfirmPopLayout.add_widget(cancleBut)
        self.homepopup = Popup(title='',content= homeconfirmPopLayout, size_hint=(None, None), size=(400, 300))
        self.homepopup.open()

    def gotomain(self,instance):
        print('go to main')
        self.pausepopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()

    def leftaimCB(self,button,value):
        print('aimming left')
        print('player stamina = ', self.playerStamina.value)

        if self.playerStamina.value <= 0:
            print("player's stamina is out!!")
        else:
            if value == 'down':
                # Code to be executed when the button is pressed
                print("left DOWN!")
            elif value == 'normal':
                # Code to be executed when the button is released
                self.playerStamina.value = self.playerStamina.value - 10
                print("left UP!")
            elif value == 'disabled':
                # Code to be executed when the button is disabled
                print("left disabled!")


    def rightaimCB(self,button,value):
        print('aimming right') 
        print('player stamina = ', self.playerStamina.value)

        if self.playerStamina.value <= 0:
            print("player's stamina is out!!")
        else:
            if value == 'down':
                # Code to be executed when the button is pressed
                print("right DOWN!")
            elif value == 'normal':
                # Code to be executed when the button is released
                self.playerStamina.value = self.playerStamina.value - 10
                print("right UP!")
            elif value == 'disabled':
                # Code to be executed when the button is disabled
                print("right disabled!")


class L2_static(Screen):
    def on_enter(self):
        l2_layout = FloatLayout()
        with self.canvas:
            Rectangle(size = (488,420),pos = (150,120)) # size /10 *4
            Color(0,1,0,0.8)
            Rectangle(size = (92,8),pos = (204,300))
            Rectangle(size = (92,8),pos = (348,300))
            Rectangle(size = (92,8),pos = (492,300))
            Rectangle(size = (92,8),pos = (276,412))
            Rectangle(size = (92,8),pos = (420,412))
            Color(1,0.8,0.45,1)
            Ellipse(size=(32,32),pos=(234,288))
            Ellipse(size=(32,32),pos=(378,288))
            Ellipse(size=(32,32),pos=(522,288))
            Ellipse(size=(32,32),pos=(306,400))
            Ellipse(size=(32,32),pos=(450,400))
            # Ellipse(size=(32,32),pos=(150,120))

        l2Label = Label(text = 'LEVEL2', font_size = 30, pos_hint = {'x':0,'y':0.48})

        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.moriaStamina.value = 100

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        self.goal_var = 0
        print(self.goal_var)
        testBut = Button(text = 'goal', size_hint=(None,None), size=(50,30),pos_hint={'x':0.93,'y':0})
        testBut.bind(on_release = self.reachgoal)
        l2_layout.add_widget(testBut)

        l2_layout.add_widget(self.moriaStamina)
        l2_layout.add_widget(moriaLabel)
        l2_layout.add_widget(pauseBut)
        l2_layout.add_widget(l2Label)

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)


        self.add_widget(l2_layout)

    def reachgoal(self,instance):
        print(self.goal_var)
        self.goal_var = 1
        if self.goal_var == 1:
            self.clear_widgets()
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.goal_var = 0
        print("L2 ending --> player lose")
        self.manager.current = 'loserpop'


    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 30
        print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'


    def pause_callback(self, *args):
        print('pause')
        if self.clock_event:
            Clock.unschedule(self.clock_event)
            self.clock_event = None

        pausePopLayout = FloatLayout()
        resumeBut = Button(text = 'RESUME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.85})
        resumeBut.bind(on_release = self.resume_callback)
        backHome = Button(text = 'HOME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.45})
        backHome.bind(on_release = self.home_callback)
        pausePopLayout.add_widget(resumeBut)
        pausePopLayout.add_widget(backHome)
        self.pausepopup = Popup(title='PAUSE',content= pausePopLayout, size_hint=(None, None), size=(400, 350))
        self.pausepopup.open()
    
    def resume_callback(self, instance):
        print('resume dai jaaa')
        self.pausepopup.dismiss()
        if not self.clock_event:
            self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)

    def home_callback(self,instance):
        print('go back home')
        homeconfirmPopLayout = FloatLayout()
        homeLabel = Label(text = 'HOME ?',font_size = 60,pos_hint = {'center_x':0.5,'y':0.25})
        okBut = Button(text = 'OK',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.25,'top':0.45})
        cancleBut = Button(text = 'CANCLE',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.75,'top':0.45})
        okBut.bind(on_release = self.gotomain)
        cancleBut.bind(on_release = self.cancleCB)
        homeconfirmPopLayout.add_widget(homeLabel)
        homeconfirmPopLayout.add_widget(okBut)
        homeconfirmPopLayout.add_widget(cancleBut)
        self.homepopup = Popup(title='',content= homeconfirmPopLayout, size_hint=(None, None), size=(400, 300))
        self.homepopup.open()

    def gotomain(self,instance):
        print('go to main')
        self.pausepopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()


class L2_dynamic(Screen):
    def on_enter(self):
        print('L2 dynamic game start')
        l2_layout = FloatLayout()
        with self.canvas:
            Rectangle(size = (488,420),pos = (150,120)) # size /10 *4
            Color(0,1,0,0.8)
            Rectangle(size = (92,8),pos = (204,300))
            Rectangle(size = (92,8),pos = (348,300))
            Rectangle(size = (92,8),pos = (492,300))
            Rectangle(size = (92,8),pos = (276,412))
            Rectangle(size = (92,8),pos = (420,412))
            Color(1,0.8,0.45,1)
            Ellipse(size=(32,32),pos=(234,288))
            Ellipse(size=(32,32),pos=(378,288))
            Ellipse(size=(32,32),pos=(522,288))
            Ellipse(size=(32,32),pos=(306,400))
            Ellipse(size=(32,32),pos=(450,400))
            # Ellipse(size=(32,32),pos=(150,120))

        l2Label = Label(text = 'LEVEL2', font_size = 30, pos_hint = {'x':0,'y':0.48})

        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.moriaStamina.value = 100
        self.playerStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.43})
        playerLabel = Label(text = 'You',pos_hint={'x':-0.45,'y':0.44})
        self.playerStamina.value = 100

        rotateBut = Button(text = 'Trick',size_hint=(None,None),size=(100,50),pos = (350,50))
        rotateBut.bind(on_release = self.rotateCB)

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        self.goal_var = 0
        print(self.goal_var)
        testBut = Button(text = 'goal', size_hint=(None,None), size=(50,30),pos_hint={'x':0.93,'y':0})
        testBut.bind(on_release = self.reachgoal)
        l2_layout.add_widget(testBut)

        l2_layout.add_widget(self.moriaStamina)
        l2_layout.add_widget(moriaLabel)
        l2_layout.add_widget(self.playerStamina)
        l2_layout.add_widget(playerLabel)
        l2_layout.add_widget(pauseBut)
        l2_layout.add_widget(l2Label)
        l2_layout.add_widget(rotateBut)

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)


        self.add_widget(l2_layout)

    def reachgoal(self,instance):
        print(self.goal_var)
        self.goal_var = 1
        if self.goal_var == 1:
            self.clear_widgets()
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.goal_var = 0
        print("L2 ending --> player lose")
        self.manager.current = 'loserpop'


    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 30
        print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'


    def pause_callback(self, *args):
        print('pause')
        if self.clock_event:
            Clock.unschedule(self.clock_event)
            self.clock_event = None

        pausePopLayout = FloatLayout()
        resumeBut = Button(text = 'RESUME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.85})
        resumeBut.bind(on_release = self.resume_callback)
        backHome = Button(text = 'HOME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.45})
        backHome.bind(on_release = self.home_callback)
        pausePopLayout.add_widget(resumeBut)
        pausePopLayout.add_widget(backHome)
        self.pausepopup = Popup(title='PAUSE',content= pausePopLayout, size_hint=(None, None), size=(400, 350))
        self.pausepopup.open()

    def rotateCB(self,instance):
        print('rotate')
        print('player stamina = ', self.playerStamina.value)

        if self.playerStamina.value <= 0:
            print("player's stamina is out!!")
        else:
            self.playerStamina.value = self.playerStamina.value - 10

    def resume_callback(self, instance):
        print('resume dai jaaa')
        self.pausepopup.dismiss()
        if not self.clock_event:
            self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)

    def home_callback(self,instance):
        print('go back home')
        homeconfirmPopLayout = FloatLayout()
        homeLabel = Label(text = 'HOME ?',font_size = 60,pos_hint = {'center_x':0.5,'y':0.25})
        okBut = Button(text = 'OK',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.25,'top':0.45})
        cancleBut = Button(text = 'CANCLE',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.75,'top':0.45})
        okBut.bind(on_release = self.gotomain)
        cancleBut.bind(on_release = self.cancleCB)
        homeconfirmPopLayout.add_widget(homeLabel)
        homeconfirmPopLayout.add_widget(okBut)
        homeconfirmPopLayout.add_widget(cancleBut)
        self.homepopup = Popup(title='',content= homeconfirmPopLayout, size_hint=(None, None), size=(400, 300))
        self.homepopup.open()

    def gotomain(self,instance):
        print('go to main')
        self.pausepopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()

class loserPopup(Screen):
    def on_enter(self):
        print("LOSER")
        loserPopLayout = FloatLayout()
        loserLabel = Label(text = 'LOSER !!',font_size = 60,pos_hint = {'center_x':0.5,'y':0.3})
        loserLabel2 = Label(text = "You are FIRED !!.",font_size = 22,pos_hint = {'center_x':0.5,'y':0.1})
        backHome = Button(text = 'HOME',size_hint=(None, None),size=(300, 100), pos_hint = {'center_x':0.5,'top':0.45})
        backHome.bind(on_release = self.home_callback)
        loserPopLayout.add_widget(loserLabel)
        loserPopLayout.add_widget(loserLabel2)
        loserPopLayout.add_widget(backHome)
        self.vicpopup = Popup(title='',content= loserPopLayout, size_hint=(None, None), size=(400, 300))
        self.vicpopup.open()

    def home_callback(self,instance):
        print('go back home')
        homeconfirmPopLayout = FloatLayout()
        homeLabel = Label(text = 'HOME ?',font_size = 60,pos_hint = {'center_x':0.5,'y':0.25})
        okBut = Button(text = 'OK',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.25,'top':0.45})
        cancleBut = Button(text = 'CANCLE',size_hint=(None, None),size=(150, 100), pos_hint = {'center_x':0.75,'top':0.45})
        okBut.bind(on_release = self.gotomain)
        cancleBut.bind(on_release = self.cancleCB)
        homeconfirmPopLayout.add_widget(homeLabel)
        homeconfirmPopLayout.add_widget(okBut)
        homeconfirmPopLayout.add_widget(cancleBut)
        self.homepopup = Popup(title='',content= homeconfirmPopLayout, size_hint=(None, None), size=(400, 300))
        self.homepopup.open()

    def gotomain(self,instance):
        print('go to main')
        self.vicpopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()

class tryScreen(Screen):
    def on_enter(self):
        pass



        
class HMmission_stoptheRescueRobot(App):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(openingScreen(name='openS'))
        self.sm.add_widget(popup1_Screen(name='pop1'))
        self.sm.add_widget(connectingScreen(name='connectS'))
        self.sm.add_widget(mainScreen(name='mainS'))
        self.sm.add_widget(popup_playmode(name='popPlaymode'))
        self.sm.add_widget(howtoplay(name='htp'))
        self.sm.add_widget(L1_static(name='L1S'))
        self.sm.add_widget(L1_dynamic(name='L1D'))
        self.sm.add_widget(L2_static(name='L2S'))
        self.sm.add_widget(L2_dynamic(name='L2D'))
        self.sm.add_widget(vicpop(name='vicpop'))
        self.sm.add_widget(loserPopup(name='loserpop'))


        self.sm.add_widget(tryScreen(name='ts'))
        return self.sm
    
if __name__ == '__main__':
    HMmission_stoptheRescueRobot().run()