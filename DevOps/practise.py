import time

from watchdog.events import *
from watchdog.observers import Observer


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        super().__init__()

    def on_moved(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"Folder is moved from {event.src_path} "
                  f"to {event.dest_path} at {now}.")
        else:
            print(f"File is moved from {event.src_path} "
                  f"to {event.dest_path} at {now}.")

    def on_created(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"Folder is created in {event.src_path} at {now}.")
        else:
            print(f"File is created in {event.src_path} at {now}.")

    def on_deleted(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"Folder is deleted in {event.src_path} at {now}.")
        else:
            print(f"File is deleted in {event.src_path} at {now}.")

    def on_modified(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"Folder is modified in {event.src_path} at {now}.")
        else:
            print(f"File is modefied in {event.src_path} at {now}.")


if __name__ == '__main__':
    observer = Observer()
    path = r'C:\Users\Laurence\Desktop'
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path, True)
    print(f"监控目录 {path}: ")
    observer.start()
    observer.join()