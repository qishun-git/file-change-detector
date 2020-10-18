import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from send_email import EmailSender, construct_email


class Detector(object):
    SLEEP_TIME = 3600

    def __init__(self, config):
        self.config = config
        self.counter = 1
        self.last_added_file = ""
        self.detect_path = os.path.abspath(self.config["detect_path"])
        self.__class__.SLEEP_TIME = self.config["sleep_time"]

    def start_detect(self):
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = True
        my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        my_event_handler.on_created = self.on_created
        self.detect_changes(my_event_handler)

    def detect_changes(self, my_event_handler):
        my_observer = Observer()
        print(f"Creating an observer for path: {self.detect_path}")
        my_observer.schedule(my_event_handler, self.detect_path, recursive=True)
        my_observer.start()
        previous_counter = 0
        email_sender = EmailSender(self.config)
        sleep_time = self.SLEEP_TIME
        try:
            while True:
                print("Detecting File Changes:")
                if self.counter == previous_counter:
                    print(f"The last file added is {self.last_added_file}")
                    message = construct_email(self.detect_path, self.last_added_file)
                    email_sender.send_emails(message)
                else:
                    file_added = self.counter - previous_counter
                    print(f"{file_added} files were added during the past hour!")
                previous_counter = self.counter
                time.sleep(sleep_time)
        except KeyboardInterrupt:
            my_observer.stop()
            my_observer.join()

    def on_created(self, event):
        print(f"{event.src_path} created.")
        self.last_added_file = event.src_path
        self.counter += 1
