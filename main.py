from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

class DialogContent(MDBoxLayout):
    #this is for class constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text=datetime.now().strtime("%A %d %B %Y")

    #this func wil show the date picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save)

    #this func will get date and save in friendly form
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)


class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        self.theme_cls.primary_palette=("Teal")

    def show_task_function(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title = "Create Task",
                type="custom",
                content_cls = DialogContent()
            )
            self.task_list_dialog.open()

    def add_task(self, task, task_date):
        print(task.text, task_date)

    
    
    def close_dialog(self, **kwargs):
        self.task_list_dialog.dismiss()


if __name__ == "__main__":
    MainApp().run()
    