from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MonAppli(App):
    def build(self):
        self.title = "Ma Super App"
        disp = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.txt = Label(text="Salut ! 🎉", font_size=30, color=(1,1,1,1))
        btn = Button(text="Appuie-moi !", size_hint=(1,0.4),
                     background_color=(0.1,0.6,0.8,1), font_size=25)
        btn.bind(on_press=self.changer)
        
        disp.add_widget(self.txt)
        disp.add_widget(btn)
        return disp

    def changer(self, instance):
        self.txt.text = "Ça marche ! 👏" if self.txt.text == "Salut ! 🎉" else "Salut ! 🎉"

if __name__ == "__main__":
    MonAppli().run()
  
