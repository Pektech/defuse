from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from engine import run_engine
from rules import rulebook

class WireForm(BoxLayout):
    def defuse(self):
        wire_states = {
            "red": self.ids.red_spinner.text.lower(),
            "blue": self.ids.blue_spinner.text.lower(),
            "yellow": self.ids.yellow_spinner.text.lower(),
            "black": self.ids.black_spinner.text.lower(),
        }
        self.ids.result_label.text = run_engine(wire_states, rulebook)

class BombApp(App):
    def build(self):
        return WireForm()

if __name__ == "__main__":
    BombApp().run()
