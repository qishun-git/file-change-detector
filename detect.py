import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

counter = 0

def start_detect(config):
    file_dir = input("File Directory: ")
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    detect_changes(my_event_handler, file_dir)


def detect_changes(my_event_handler, path):
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    previous_counter = counter
    try:
        while True:
            if counter == previous_counter:
                print("status unchanged!")
            else:
                file_added = counter - previous_counter
                print(f"{file_added} files were added!")
            previous_counter = counter
            time.sleep(10)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


def on_created(event):
    print(f"{event.src_path} created.")
    global counter
    counter += 1
