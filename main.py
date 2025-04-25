from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
import requests

class ToDoApp(MDApp):
    def build(self):
        self.url = "http://127.0.0.1:8000/api/tasks/"
        return Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    MDTextField:
        id: task_title
        hint_text: "Title"
    MDTextField:
        id: task_description
        hint_text: "Description"
    MDRaisedButton:
        text: "Add Task"
        on_release: app.add_task()
    """)

    def add_task(self):
        title = self.root.ids.task_title.text
        description = self.root.ids.task_description.text
        if title and description:
            response = requests.post(self.url, data={'title': title, 'description': description})
            if response.status_code == 201:
                print("Task Added Successfully")
            else:
                print("Failed to Add Task")

if __name__ == "__main__":
    ToDoApp().run()

