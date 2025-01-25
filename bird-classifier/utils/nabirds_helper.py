import sys

from pathlib import Path

class NABirdsHelper:
    def __init__(self, nabirds_dir: str):
        self._nabirds_dir = Path(nabirds_dir)

        # set up local bird image data-set paths
        self._nabirds_images = self._nabirds_dir / "images"
        self._nabirds_python_file = self._nabirds_dir / "nabirds.py"

        # important to add the root directory to sys-path to import nabirds.py
        sys.path.append(str(self._nabirds_dir.parent))

        # check and load all data
        self._check_nabirds_directory()
        self._import_nabirds_module()

    def _check_nabirds_directory(self):
        """
        Check if all important parts of the 'NABirds' dataset are present in the provided directory.
        """
        # check if required content directories / files exist
        if self._nabirds_dir.is_dir():
            print(f"[*] Found '{self._nabirds_dir}' directory!")
        else:
            print(f"[!] '{self._nabirds_dir}' data-set directory does not exist at specified location!")

        if self._nabirds_images.is_dir():
            print(f"[*] Found '{self._nabirds_images}' image directory!")

            nb_images = len(list(self._nabirds_images.glob('*/*.jpg')))
            print(f"[*] The 'NABirds' data-set consists of {nb_images} images.")
        else:
            print(f"[!] '{self._nabirds_images}' data-set image directory does not exist at specified location!")

        if  self._nabirds_python_file.is_file():
            print(f"[*] Found '{ self._nabirds_python_file}' Python-script!")
        else:
            print(f"[!] '{ self._nabirds_python_file}' Python-script does not exist at specified location!")

    def _import_nabirds_module(self):
        """
        Try to import the 'nabirds.py' module of NABirds directory.
        If successfully imported, use the NABirds data to set some properties useful for further processing.
        """
        if not Path(self._nabirds_dir / "nabirds.py").exists():
            print("[!] Cannot import nabirds module because the file does not exist!")
        else:
            try:
                from nabirds import nabirds
                print("[*] Successfully imported 'nabirds' module!")

                # load all data if import was successful (nabirds module only available in here!)
                self._image_paths = nabirds.load_image_paths(self._nabirds_dir) # image-id: path
                self._bounding_boxes = nabirds.load_bounding_box_annotations(self._nabirds_dir) # image-id: bounding-box coordinates
                self._bird_class_labels = nabirds.load_image_labels(self._nabirds_dir) # image-id - class-id
                self._bird_class_names = nabirds.load_class_names(self._nabirds_dir) # class-id - class-name

            except Exception as ex:
                print(f"[!] Failed to import 'nabirds' module with following error: {ex}")

    def get_image_paths(self) -> dict:
        return self._image_paths

    def get_bounding_boxes(self) -> dict:
        return self._bounding_boxes

    def get_bird_class_labels(self) -> dict:
        return self._bird_class_labels

    def get_bird_class_names(self) -> dict:
        return self._bird_class_names
