from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
import requests

# Classe personnalisée pour forcer la couleur du texte
class CustomTextField(MDTextField):
    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        self.text_color = (0, 0, 0.5, 1)  # bleu foncé

KV = '''
<CustomTextField@MDTextField>

BoxLayout:
    orientation: 'vertical'
    padding: "74dp"
    spacing: "30dp"

    MDCard:
        orientation: 'vertical'
        padding: "24dp"
        size_hint_x: 0.9
        height: "300dp"
        pos_hint: {"center_x": 0.5}
        elevation: 8
        md_bg_color: 0.9, 1, 1, 1
        radius: [20,]

        MDLabel:
            text: "Add a New Task"
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H6"

        CustomTextField:
            id: task_title
            hint_text: "Task Title"
            mode: "rectangle"
            helper_text_mode: "on_error"
            on_focus: if self.focus: self.line_color_focus = 0, 0, 0.5, 1

        CustomTextField:
            id: task_description
            hint_text: "Task Description"
            mode: "rectangle"
            helper_text_mode: "on_error"
            on_focus: if self.focus: self.line_color_focus = 0, 0, 0.5, 1

        MDRaisedButton:
            text: "Submit"
            md_bg_color: 0, 0.5, 0.5, 1
            pos_hint: {"center_x": 0.5}
            on_release: app.add_task()

    MDLabel:
        id: feedback_label
        text: ""
        halign: "center"
        theme_text_color: "Secondary"
'''

class ToDoApp(MDApp):
    def build(self):
        self.url = "http://127.0.0.1:8000/api/tasks/"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"
        return Builder.load_string(KV)

    def show_snackbar(self, message, success=True):
        Snackbar(
            text=message,
            bg_color=(0.2, 0.6, 0.4, 1) if success else (0.2, 0.4, 0.6, 1),
            snackbar_animation="fade_in",
            radius=[12],
            elevation=4,
        ).open()

    def add_task(self):
        title = self.root.ids.task_title.text.strip()
        description = self.root.ids.task_description.text.strip()

        if not title or not description:
            self.show_snackbar("Please fill all fields.", success=False)
            return

        try:
            response = requests.post(self.url, data={'title': title, 'description': description})
            print("Response:", response.status_code, response.text)
            if response.status_code == 201:
                self.show_snackbar("✅ Task added successfully!")
                self.root.ids.task_title.text = ""
                self.root.ids.task_description.text = ""
            else:
                self.show_snackbar(f"Error {response.status_code}: {response.text}", success=False)
        except Exception as e:
            self.show_snackbar(f"Connection error: {e}", success=False)

if __name__ == "__main__":
    ToDoApp().run()
