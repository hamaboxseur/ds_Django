from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.card import MDCard
import requests  # Import the requests library


# Custom TextField class to handle text input with extra styling
class CustomTextField(MDTextField):
    pass


# Main App class
class ToDoApp(MDApp):
    def build(self):
        # URL for the API endpoint (placeholder)
        self.url = "http://127.0.0.1:8000/api/tasks/"

        return Builder.load_file('todo.kv')

    def add_task(self, task_title, task_description):
        data = {"title": task_title, "description": task_description}

        try:
            response = requests.post(self.url, json=data)
            print(f"Response: {response.status_code}, {response.text}")  # Debug print
            if response.status_code == 201:
                self.show_snackbar("✅ Task added successfully!")
                # Clear the input fields
                self.root.ids.task_title.text = ""
                self.root.ids.task_description.text = ""
            else:
                self.show_snackbar(f"❌ Failed to add task: {response.status_code}", success=False)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.show_snackbar("❌ Error connecting to the server!", success=False)

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
