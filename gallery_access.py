from plyer import storagepath
import os
import datetime

class Gallery:
    def __init__(self):
        try:
            self.gallery_path = storagepath.get_pictures_dir()
        except NotImplementedError:
            self.gallery_path = '/Users/haddelalshahabi/Desktop/Images'

    def set_gallery_path(self, path):
        if os.path.isdir(path):
            self.gallery_path = path
            self.current_folder = path  # Also set the current folder
            self._load_images_from_current_folder()  # Refresh the image list
            return True
        else:
            print("The provided path is not a valid directory.")
            return False

    def get_folders(self):
        folders = [f for f in os.listdir(self.gallery_path) if os.path.isdir(os.path.join(self.gallery_path, f))]
        return folders

    def set_folder(self, folder_name):
        folder_path = os.path.join(self.gallery_path, folder_name)
        if os.path.isdir(folder_path):
            self.current_folder = folder_path
            self.image_list = [img for img in os.listdir(folder_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
            self.current_image_index = 0 if self.image_list else -1
            return True
        return False

    def get_current_image(self):
        if self.current_folder and 0 <= self.current_image_index < len(self.image_list):
            return os.path.join(self.current_folder, self.image_list[self.current_image_index])
        return None

    def next_image(self):
        if self.image_list and self.current_image_index < len(self.image_list) - 1:
            self.current_image_index += 1
            return self.get_current_image()
        return None

    def prev_image(self):
        if self.image_list and self.current_image_index > 0:
            self.current_image_index -= 1
            return self.get_current_image()
        return None

    def get_images_by_date(self, date_query):
        if not self.current_folder:
            return None

        date_images = []
        for img in self.image_list:
            img_path = os.path.join(self.current_folder, img)
            # Get the modification time of the image
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(img_path))
            # Check if the image's modification date matches the query
            if date_query.lower() in mod_time.strftime("%B %Y").lower():
                date_images.append(img)

        if date_images:
            self.image_list = date_images
            self.current_image_index = 0
            return True
        return False