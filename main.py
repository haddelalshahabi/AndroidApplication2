from kivy.app import App
from main_layout import MainLayout
from gallery_access import Gallery

class AudioVisionApp(App):
    def build(self):
        # Initialize gallery to the system's pictures directory
        self.gallery = Gallery()

        # Set up the main layout
        self.main_layout = MainLayout(self.gallery)
        return self.main_layout

if __name__ == '__main__':
    AudioVisionApp().run()
