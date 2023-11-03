from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from ui_components import SettingsButton

class MainLayout(BoxLayout):
    def __init__(self, gallery, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.gallery = gallery

        # Add navigation buttons
        nav_layout = BoxLayout(size_hint_y=None, height=50)
        self.prev_button = Button(text='Previous')
        self.next_button = Button(text='Next')
        nav_layout.add_widget(self.prev_button)
        nav_layout.add_widget(self.next_button)

        # Bind the buttons to the navigation methods
        self.prev_button.bind(on_release=self.on_previous_image)
        self.next_button.bind(on_release=self.on_next_image)

        self.add_widget(nav_layout)

        # Display the first image if available
        self.display_current_image()

    def on_previous_image(self, instance):
        if self.gallery.prev_image():
            self.display_current_image()

    def on_next_image(self, instance):
        if self.gallery.next_image():
            self.display_current_image()

    def display_current_image(self):
        # Logic to display the image in the UI goes here
        current_image = self.gallery.get_current_image()
        if current_image:
            print(f"Displaying image: {current_image}")
            # Update an image widget with the current image
        else:
            print("No image to display")