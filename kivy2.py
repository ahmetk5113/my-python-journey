import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class My_gui(App):
	def build(self):
		return LoginScreen()


class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text="Username"))
		self.usernames = TextInput(multiline=True)
		self.add_widget(self.usernames)
		self.add_widget(Label(text="password"))
		self.password = TextInput(password=True, multiline=True)
		self.add_widget(self.password)


if __name__ == '__main__':
	My_gui().run()