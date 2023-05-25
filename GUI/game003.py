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
from kivy.uix.widget import Widget

import paho.mqtt.client as mqtt

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from msg_interface.srv import CommandGUI
from rclpy.parameter import Parameter
from std_msgs.msg import String
from std_msgs.msg import Int64

import subprocess

def start_ros_node():
    serviceServer = ['python3', '/home/pinhulk/mobilerobot/project/src/mbrproject001/scripts/serviceNode001.py']
    process = subprocess.Popen(serviceServer)

value = 100


class sendCommand(Node):
    def __init__(self):
        super().__init__('sendCommand')
        self.command_client = self.create_client(CommandGUI,"/command_state")
        self.send_command = CommandGUI.Request()
        self.com = String()

    def send_request(self,com):
        print("send_request")
        self.send_command.command.data = com
        self.future = self.command_client.call_async(self.send_command)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

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
        gameMQ.mq.publish("project01/connect","connect")
        gameMQ.sendCom.send_request("connect")
        self.clear_widgets()
        self.popup.dismiss()
        print("connect button's clicked")
        self.manager.current = 'connectS'

class connectingScreen(Screen):
    def on_enter(self):
        Text = "[size=60]Connecting...[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)

class connectFailed(Screen):
    def on_enter(self):
        print("connection failed")
        popLayout = FloatLayout
        Text = "[size=40]Connection Failed[/size]\n[size=20]Please check your robot and the filed.[/size]"
        l1 = Label(text = Text, markup=True)
        okBut = Button(text = 'OK')
        okBut.bind(on_release = self.butCB)

        pop = Popup()

        self.pop = Popup(title='',content= popLayout, size_hint=(None, None), size=(400, 200))
    
    def butCB(self, instance):
        print("reconnect")
        self.manager.current = 'pop1'

class mainScreen(Screen):
    def on_enter(self):
        with open('/home/pinhulk/mobilerobot/project/src/mbrproject001/files/goalFlag.txt','w') as file:
                file.write(str(0))
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

        self.app = App.get_running_app()

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

    def on_message():
        pass

    def static_callback(self, instance):
        self.clear_widgets()
        self.popup.dismiss()
        gameMQ.mq.publish("project01/playmode","static")
        self.manager.current = 'l1sB'

    def dynamic_callback(self, instance):
        self.clear_widgets()
        self.popup.dismiss()
        gameMQ.mq.publish("project01/playmode","dynamic")
        self.manager.current = 'l1dB'

    def closePop(self, instance):
        print('pop-up closed')
        self.popup.dismiss()
        self.manager.current = 'mainS'

class l1Sbut(Screen):
    def on_enter(self):
        print('u r playing in STATIC MODE')
        Text = "[size=60]LEVEL 1[/size]\n[size=11](static)[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)

class l1Dbut(Screen):
    def on_enter(self):
        print('u r plaing in DYNAMIC MODE')
        Text = "[size=60]LEVEL 1[/size]\n[size=11](dynamic)[/size]"
        self.connect = Label(text=Text, markup=True)
        self.add_widget(self.connect)
        
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

        l1_layout.add_widget(self.moriaStamina)
        l1_layout.add_widget(l1Label)
        l1_layout.add_widget(moriaLabel)
        l1_layout.add_widget(pauseBut)

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)

        self.add_widget(l1_layout)

    def on_leave(self):
        if self.clock_event:  # if clock event is scheduled
            Clock.unschedule(self.clock_event)  # cancel it
        self.clock_event = None 
        
    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 10
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
        gameMQ.sendCom.send_request("pause")
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
        gameMQ.sendCom.send_request("resume")
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
        gameMQ.sendCom.send_request("end")
        gameMQ.mq.publish("project01/home","home")
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
        gameMQ.sendCom.send_request("end")
        gameMQ.mq.publish("project01/home","home")
        self.vicpopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()


class l1_canvasL(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        a2 = Button(text = 'aim Left',size_hint=(None,None),size=(100,50),pos = (150,50))
        a2.bind(on_press=self.cb2,on_release=self.stop)
        self.add_widget(a2)

        self.recL = Rectangle(size = (192,8),pos = (202,264))
        self.cirL = Ellipse(size=(32,32),pos=(186,252))
    
        with self.canvas:
            Rectangle(size = (488,420),pos = (150,120)) # size /10 *4
            Color(0.6,0,0,0.8)
            self.cirL = Ellipse(size=(32,32),pos=(186,252))
            Color(0,0.6,0.3,1)
            self.recL = Rectangle(size = (192,8),pos = (202,264))
        self.cirL_center = (self.cirL.pos[0]+self.cirL.size[0]/2,self.cirL.pos[1]+self.cirL.size[1]/2)
        print(self.cirL_center)
        self.angle = 0
        self.a = 5
        self.b = 0

    def cb2(self,instance):
        self.clock_event = Clock.schedule_interval(self.animate_rotation, 0.05)

    def animate_rotation(self,dt):
        global value
        value = value-0.5
        with self.canvas:
            PushMatrix()
            if self.angle == 70:
                self.a = -5
            elif self.angle == 340:
                self.a = 5
            self.angle = (self.angle+self.a)%360
            print(self.angle)

            self.canvas.remove(self.recL)
            Color(0,0.6,0.3,1)
            Rotate(origin=self.cirL_center,angle=self.angle)
            self.recL = Rectangle(size = (192,8),pos = (202,264))
            PopMatrix()

    def stop(self,instance):
        Clock.unschedule(self.clock_event)
        gameMQ.mq.publish("project01/leftBut",self.angle)

class l1_canvasR(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a2 = Button(text = 'aim Right',size_hint=(None,None),size=(100,50),pos = (540,50))
        a2.bind(on_press=self.cb2,on_release=self.stop)
        self.add_widget(a2)

        self.recR = Rectangle(size = (192,8),pos = (406,404))
        self.cirR = Ellipse(size=(32,32),pos=(582,392))
    
        with self.canvas:
            Color(0.6,0,0,0.8)
            self.cirR = Ellipse(size=(32,32),pos=(582,392))
            Color(0,0.6,0.3,1)
            self.recR = Rectangle(size = (192,8),pos = (406,404))
        self.cirR_center = (self.cirR.pos[0]+self.cirR.size[0]/2,self.cirR.pos[1]+self.cirR.size[1]/2)
        print(self.cirR_center)
        self.angle = 0
        self.a = 5

    def cb2(self,instance):
        self.clock_event = Clock.schedule_interval(self.animate_rotation, 0.05)

    def animate_rotation(self,dt):
        global value
        value = value-0.5
        with self.canvas:
            PushMatrix()
            if self.angle == 70:
                self.a = -5
            elif self.angle == 340:
                self.a = 5
            self.angle = (self.angle+self.a)%360
            print(self.angle)

            self.canvas.remove(self.recR)
            Color(0,0.6,0.3,1)
            Rotate(origin=self.cirR_center,angle=self.angle)
            self.recR = Rectangle(size = (192,8),pos = (406,404))
            PopMatrix()

    def stop(self,instance):
        Clock.unschedule(self.clock_event)
        gameMQ.mq.publish("project01/rightBut",self.angle)


class L1_dynamic(Screen):
    def on_enter(self):
        print('Level 1 Dynamic mode game start')
        l1_layout = FloatLayout()

        l1Label = Label(text = 'LEVEL1', font_size = 30, pos_hint = {'x':0,'y':0.48})

        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.playerStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.43})
        playerLabel = Label(text = 'You',pos_hint={'x':-0.45,'y':0.44})
        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina.value = 100
        self.playerStamina.value = 100

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        l1_layout.add_widget(self.moriaStamina)
        l1_layout.add_widget(self.playerStamina)
        l1_layout.add_widget(playerLabel)
        l1_layout.add_widget(moriaLabel)
        l1_layout.add_widget(pauseBut)
        l1_layout.add_widget(l1Label)
        l1_layout.add_widget(l1_canvasL())
        l1_layout.add_widget(l1_canvasR())

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)
        self.clock_event2 = Clock.schedule_interval(self.playerV, 0.1)

        self.add_widget(l1_layout)

    def on_leave(self):
        if self.clock_event:  # if clock event is scheduled
            Clock.unschedule(self.clock_event)  # cancel it
        self.clock_event = None

        if self.clock_event2:  # if clock event is scheduled
            Clock.unschedule(self.clock_event2)  # cancel it
        self.clock_event2 = None 

    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 10
        print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'

    def playerV(self,dt):
        global value
        self.playerStamina.value = value
        if self.playerStamina.value <= 0:
            self.playerStamina.value = 0
            gameMQ.mq.publish("project01/stamina","out")

    def dynamic_game(self,dt):
        print("L1 ending")
        self.manager.current = 'L2D'


    def pause_callback(self, *args):
        print('pause')
        gameMQ.sendCom.send_request("pause")
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
        gameMQ.sendCom.send_request("resume")
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
        gameMQ.sendCom.send_request("end")
        gameMQ.mq.publish("project01/home","home")
        self.pausepopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()

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

        l2Label = Label(text = 'LEVEL2', font_size = 30, pos_hint = {'x':0,'y':0.48})

        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.moriaStamina.value = 100

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        l2_layout.add_widget(self.moriaStamina)
        l2_layout.add_widget(moriaLabel)
        l2_layout.add_widget(pauseBut)
        l2_layout.add_widget(l2Label)

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)
        self.clock_event2 = Clock.schedule_interval(self.checkgoal, 0.01)


        self.add_widget(l2_layout)
    
    def checkgoal(self,dt):
        with open('/home/pinhulk/mobilerobot/project/src/mbrproject001/files/goalFlag.txt','r') as file:
            self.goalflag = file.read()
            print("goalflag",type(self.goalflag))
        if self.goalflag == "1":
            self.clear_widgets()
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            if self.clock_event2:
                Clock.unschedule(self.clock_event2)
                self.clock_event = None
            print("L2 ending --> player lose")
            self.manager.current = 'loserpop'
        else:
            print("00000")

    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 10
        print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'


    def pause_callback(self, *args):
        print('pause')
        gameMQ.sendCom.send_request("pause")
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
        gameMQ.sendCom.send_request("resume")
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
        gameMQ.sendCom.send_request("end")
        gameMQ.mq.publish("project01/home","home")
        self.pausepopup.dismiss()
        self.homepopup.dismiss()
        self.manager.current = 'mainS'

    def cancleCB(self,instance):
        print('cancle')
        self.homepopup.dismiss()

class l2_canvas1(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        rotateBut = Button(text = 'Trick',size_hint=(None,None),size=(100,50),pos = (350,50))
        rotateBut.bind(on_release = self.rotateCB)
        self.add_widget(rotateBut)

        with self.canvas:
            Rectangle(size = (488,420),pos = (150,120)) # size /10 *4
            Color(0,1,0,0.8)
            self.rec1 = Rectangle(size = (92,8),pos = (204,300))
            self.rec2 = Rectangle(size = (92,8),pos = (348,300))
            self.rec3 = Rectangle(size = (92,8),pos = (492,300))
            self.rec4 = Rectangle(size = (92,8),pos = (276,412))
            self.rec5 = Rectangle(size = (92,8),pos = (420,412))

            self.cir1 = Ellipse(size=(32,32),pos=(234,288))
            self.cir2 = Ellipse(size=(32,32),pos=(378,288))
            self.cir3 = Ellipse(size=(32,32),pos=(522,288))
            self.cir4 = Ellipse(size=(32,32),pos=(306,400))
            self.cir5 = Ellipse(size=(32,32),pos=(450,400))

        self.angle = 0

    def rotateCB(self,instance):
        gameMQ.mq.publish("project01/l2_trick","trick")
        global value
        value = value - 10
        print("value",value)
        with self.canvas:
            self.angle = (self.angle+90)%180
            self.canvas.remove(self.rec1)
            self.canvas.remove(self.rec2)
            self.canvas.remove(self.rec3)
            self.canvas.remove(self.rec4)
            self.canvas.remove(self.rec5)

            PushMatrix()
            Rotate(origin=(250,304),angle=self.angle)
            self.rec1 = Rectangle(size = (92,8),pos = (204,300))
            PopMatrix()

            PushMatrix()
            Rotate(origin=(394,304),angle=self.angle)
            self.rec2 = Rectangle(size = (92,8),pos = (348,300))
            PopMatrix()

            PushMatrix()
            Rotate(origin=(538,304),angle=self.angle)
            self.rec3 = Rectangle(size = (92,8),pos = (492,300))
            PopMatrix()

            
            PushMatrix()
            Rotate(origin=(322,416),angle=self.angle)
            self.rec4 = Rectangle(size = (92,8),pos = (276,412))
            PopMatrix()

            PushMatrix()
            Rotate(origin=(466,416),angle=self.angle)
            self.rec5 = Rectangle(size = (92,8),pos = (420,412))
            PopMatrix()



class L2_dynamic(Screen):
    def on_enter(self):
        print('L2 dynamic game start')
        global value
        l2_layout = FloatLayout()

        l2Label = Label(text = 'LEVEL2', font_size = 30, pos_hint = {'x':0,'y':0.48})

        moriaLabel = Label(text = 'Moria',pos_hint={'x':-0.45,'y':0.48})
        self.moriaStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.47})
        self.moriaStamina.value = 100
        self.playerStamina = ProgressBar(max=100,size_hint_x=0.2,pos_hint={'x':0.1,'y':0.43})
        playerLabel = Label(text = 'You',pos_hint={'x':-0.45,'y':0.44})
        self.playerStamina.value = 100

        pauseBut = Button(text ='| |',font_size = 40,size_hint=(None, None), size=(50, 50),pos_hint={'x':0.82,'y':0.85})
        pauseBut.bind(on_release = self.pause_callback)

        self.goal_var = 0
        print(self.goal_var)

        l2_layout.add_widget(self.moriaStamina)
        l2_layout.add_widget(moriaLabel)
        l2_layout.add_widget(self.playerStamina)
        l2_layout.add_widget(playerLabel)
        l2_layout.add_widget(pauseBut)
        l2_layout.add_widget(l2Label)

        l2_layout.add_widget(l2_canvas1())

        self.clock_event = Clock.schedule_interval(self.lowerStamina, 1.5)
        self.clock_event2 = Clock.schedule_interval(self.playerV, 0.1)

        self.add_widget(l2_layout)
        self.clock_event3 = Clock.schedule_interval(self.checkgoal, 0.01)



    def checkgoal(self,dt):
        with open('/home/pinhulk/mobilerobot/project/src/mbrproject001/files/goalFlag.txt','r') as file:
            self.goalflag = file.read()
            print("goalflag",type(self.goalflag))
        if self.goalflag == "1":
            self.clear_widgets()
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            if self.clock_event2:
                Clock.unschedule(self.clock_event2)
                self.clock_event = None
            if self.clock_event3:
                Clock.unschedule(self.clock_event3)
                self.clock_event = None
            print("L2 ending --> player lose")
            self.manager.current = 'loserpop'
        else:
            print("00000")

    def lowerStamina(self,dt):
        self.moriaStamina.value = self.moriaStamina.value - 10
        print('moria stamina = ', self.moriaStamina.value)
        if self.moriaStamina.value <= 0:
            print('YOU WIN!!')
            if self.clock_event:
                Clock.unschedule(self.clock_event)
                self.clock_event = None
            self.manager.current = 'vicpop'

    def playerV(self,dt):
        self.playerStamina.value = value
        if(value <= 0):
            self.playerStamina.value = 0
            gameMQ.mq.publish("project01/stamina","out")


    def pause_callback(self, *args):
        print('pause')
        gameMQ.sendCom.send_request("pause")
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
        gameMQ.sendCom.send_request("resume")
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
        gameMQ.sendCom.send_request("end")
        gameMQ.mq.publish("project01/home","home")
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
        gameMQ.sendCom.send_request("end")
        gameMQ.mq.publish("project01/home","home")
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
    def __init__(self, **kwargs):
        super(HMmission_stoptheRescueRobot, self).__init__(**kwargs)
        self.mq = mqtt.Client(client_id="", clean_session=True, userdata=None)
        self.topic = ""
        self.playload = ""
        with open('/home/pinhulk/mobilerobot/project/src/mbrproject001/files/goalFlag.txt','w') as file:
                file.write(str(0))
    def build(self):
        rclpy.init()
        self.sendCom = sendCommand()

        self.sm = ScreenManager()

        self.sm.add_widget(openingScreen(name='openS'))
        self.sm.add_widget(popup1_Screen(name='pop1'))
        self.sm.add_widget(connectingScreen(name='connectS'))
        self.sm.add_widget(mainScreen(name='mainS'))
        self.sm.add_widget(popup_playmode(name='popPlaymode'))
        self.sm.add_widget(l1Sbut(name='l1sB'))
        self.sm.add_widget(l1Dbut(name='l1dB'))
        self.sm.add_widget(howtoplay(name='htp'))
        self.sm.add_widget(L1_static(name='L1S'))
        self.sm.add_widget(L1_dynamic(name='L1D'))
        self.sm.add_widget(L2_static(name='L2S'))
        self.sm.add_widget(L2_dynamic(name='L2D'))
        
        self.sm.add_widget(loserPopup(name='loserpop'))
        self.sm.add_widget(vicpop(name='vicpop'))

        self.sm.add_widget(tryScreen(name='ts'))

        #-----------------MQTT config-------------------
        self.mq.on_message=self.on_message 
        self.mq.username_pw_set("iotproject","fra503xfra532")
        self.mq.on_connect = self.on_connect
        self.mq.on_message = self.on_message
        self.mq.on_publish = self.on_publish
        self.mq.connect('10.61.7.208',1883)
        self.mq.loop_start()
        
        self.mq.publish("iotPro/start","MQTT Start")
        self.mq.subscribe([("project01/field_status",0),("project01/prox1",0),("project01/prox2",0)],)
        return self.sm
    
    def start_ros_node(self,*args):
        start_ros_node()
    
    def on_stop(self):
        self.sendCom.destroy_node()
        rclpy.shutdown()
    
    def on_connect(self,client,userdata,flags,rc):
        print("Connected "+str(rc))

    def on_message(self,client,userdata,message):
        self.topic = str(message.topic)
        self.playload = str(message.payload.decode("utf-8"))
        print("Topic: ", self.topic ,", message received: " ,self.playload)
        Clock.schedule_once(self.change_screen, 0.1)

    def on_publish(self, client,userdata,mid):
        print("mid: "+str(mid))
        
    def change_screen(self,dt):
        if self.sm.current == 'connectS':
            if self.topic == "project01/field_status" and self.playload == "ready":
                print('go to mainS')
                self.sm.current = 'mainS'
        else:
            print('not in the right Screen')
        # -------------------- prox1-------------------------
        if self.sm.current == 'l1sB':
            if self.topic == "project01/prox1" and self.playload == "s1":
                print('go to l1s')
                self.sendCom.send_request("start_l1")
                self.sm.current = 'L1S'
        elif self.sm.current == 'l1dB':
            if self.topic == "project01/prox1" and self.playload == "s1":
                print('go to l1d')
                self.sendCom.send_request("start_l1")
                self.sm.current = 'L1D'
        else:
            print('not in the right Screen')
        # -------------------- prox2-------------------------
        if self.sm.current == 'L1S':
            if self.topic == "project01/prox2" and self.playload == "s2":
                print('go to l1s')
                self.sendCom.send_request("start_l2")
                self.sm.current = 'L2S'
        elif self.sm.current == 'L1D':
            if self.topic == "project01/prox2" and self.playload == "s2":
                print('go to l1d')
                self.sendCom.send_request("start_l2")
                self.sm.current = 'L2D'
        else:
            print('not in the right Screen')


if __name__ == '__main__':
    gameMQ = HMmission_stoptheRescueRobot()
    gameMQ.run()