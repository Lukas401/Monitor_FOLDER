import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.folder_to_watch, recursive=False)
        self.observer.start()
        print(f"Monitorando a pasta: {self.folder_to_watch}")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return  # Ignorar diretórios novos

        if event.src_path.endswith((".xls", ".xlsx")):
            print(f"Novo arquivo detectado: {event.src_path}")
            subprocess.run(["python", r"C:\Users\Tiadmin\Documents\CONVERTER\converter.py"], check=True)

if __name__ == "__main__":
    folder_to_watch = r"C:\Users\Tiadmin\Documents\CONVERTER\XLS FILES"  
    w = Watcher(folder_to_watch)
    w.run()
