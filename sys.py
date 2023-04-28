import os

def login(self, email, password):
    download_dir = os.path.expanduser("~/Documents/DocumentBackups")
        print("sdfsdfsd")
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        filename = "test.txt"