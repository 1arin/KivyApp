# Packages and sependancies
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker

from kivymd.uix.list import TwoLineAvatarIconListItem , ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox

# Importing the database class from database file
from database import Database
# Instantiating the database class by creating a database file
db = Database()

from datetime import datetime


class DialogContent(MDBoxLayout):
    #this is for class constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text=datetime.now().strftime("%A %d %B %Y")

    #this func wil show the date picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()

    #this func will get date and save in friendly form
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)

#Class for marking and Deleting list
class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk

    #Marking item as complete or incomplete
    def mark(self, check, the_list_item):
        if check.active == True:
            the_list_item.text = '[s]' + the_list_item.text + '[/s]'
            db.mark_task_as_completed(the_list_item.pk)
        else:
            the_list_item.text = str(db.mark_task_as_incompleted(the_list_item.pk))

    #deleting list item
    def delete_item(self, the_list_item):
        self.parent.remove_widget(the_list_item)
        db.delete_task(the_list_item.pk)


class LeftCheckbox(ILeftBody, MDCheckbox):
    pass



class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        self.theme_cls.primary_palette=("Teal")

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title = "Create Task",
                type="custom",
                content_cls = DialogContent()
            )
            self.task_list_dialog.open()

    def add_task(self, task, task_date):
        # print(task.text, task_date)
        created_task = db.create_task(task.text, task_date)
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk = created_task[0], text = '[b]' + created_task[1] + '[/b]',
        secondary_text = created_task[2]))
        task.text = ''

    
    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def on_start(self):
        '''This is to load the saved tasks and add them to the MDList widgey'''
        completed_tasks, incompleted_tasks = db.get_tasks()

        if incompleted_tasks != []:
            for task in incompleted_tasks:
                add_task = ListItemWithCheckbox(pk=task[0], text=task[1], secondary_task = task[2])
                self.root.ids.container.add_widget(add_task)

        if completed_tasks != []:
            for task in completed_tasks:
                add_task = ListItemWithCheckbox(pk= task[0], text = "[s]" + task[1] + "[/s]" , secondary_text = task[2])
                add_task.ids.check.active = True
                self.root.ids.container.add_widget(add_task)


if __name__ == "__main__":
    MainApp().run()
    