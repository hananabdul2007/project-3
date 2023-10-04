from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import  Window
import os



class MainWindow(Screen):

    pass



class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("test.kv")


class TestApp(MDApp):

    dialog = None
    def build(self):
        return kv



    def show_alert(self):
        if not self.dialog:
            self.dialog = MDDialog(title = "Do you want to exit?",
                buttons =[
                    MDFlatButton(
                        text="yes",on_release = self.root_window.close),
                    MDRectangleFlatButton(
                        text="no",on_release = self.close_dialog) ,


                ] )

            self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = os.path.expanduser('/')

        self.filemanager = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.close_filemanager,
            preview = True
    )

    def open_filemanager(self):
        self.filemanager.show(self.path)
    def select_path(self,path:str):
        print(path)
        self.close_filemanager()

    def close_filemanager(self,*args):
        self.filemanager.close()


if __name__ == "__main__":
    TestApp().run()