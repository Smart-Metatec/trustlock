import sys
import os

from PyQt5.QtCore import QObject, pyqtSignal

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from integrations.onedrive import OneDrive

from database.model import Model

class OneDriveUpload(QObject):
    finished: pyqtSignal = pyqtSignal(bool)
    META_DATA_NAME: str = "onedrive_remote_file_id"
    
    def upload(self):
        onedrive = OneDrive()
        file_id: str = onedrive.upload()
        meta_data = Model().read("metadata")
        if len(meta_data) < 1:
            print("there is no metadata so just add the file_id")
            Model().save("metadata", {"name": self.META_DATA_NAME, "data": file_id})
        else:
            onedrive_file_id = list(filter(lambda entry: entry[1] == self.META_DATA_NAME, meta_data))
            if len(onedrive_file_id) < 1:
                print("there is metadata but the file id metadata doesn't exist")
                Model().save("metadata", {"name": self.META_DATA_NAME, "data": file_id})
            else:
                print("the file id meta data exists so just update the file id")
                Model().update("metadata", {"data": file_id}, onedrive_file_id[0][0])         
            

        self.finished.emit(True)
        
    
class OneDriveDownload(QObject):
    finished: pyqtSignal = pyqtSignal(str or None)
    META_DATA_NAME: str = "onedrive_remote_file_id"
    def download(self):
        meta_data = Model().read("metadata")
        file_id = list(filter(lambda db_entry: db_entry[1] == self.META_DATA_NAME, meta_data))[0]

        onedrive = OneDrive()
        name: str = onedrive.download(file_id[2])
        if name != None:
            self.finished.emit(name)
        else:
            self.finished.emit(None)