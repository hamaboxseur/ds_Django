from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.card import MDCard


# Custom TextField class to handle text input with extra styling
class CustomTextField(MDTextField):
    pass


# Main App class
class ToDoApp(MDApp):
    def build(self):
        return Builder.load_file('todo.kv')

    def add_task(self):
        # Placeholder for task creation logic (e.g., API call or adding to local storage)
        print("Task added successfully!")
        self.show_snackbar("✅ Task added successfully!")

    def show_snackbar(self, message, success=True):
        # Updated snackbar handling with MDSnackbar
        snackbar = MDSnackbar(self.root)
        snackbar.text = message
        snackbar.snackbar_animation = "fade_in"
        snackbar.radius = [12, 12, 12, 12]  # Adjusting corner radius
        snackbar.elevation = 4
        snackbar.md_bg_color = (0.2, 0.6, 0.4, 1) if success else (0.8, 0.2, 0.2, 1)
        snackbar.open()


# Run the application
if __name__ == "__main__":
    ToDoApp().run()
