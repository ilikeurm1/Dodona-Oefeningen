from typing import Any
import json
import os

settings_path = os.path.dirname(__file__)
settings_file = os.path.join(settings_path, "settings.json")

defaults: dict[str, Any] = {
    # Path stuff
    "IMG_FOLDER": os.path.join(os.path.dirname(__file__), "..", "imgs"),
    
    # Pygame stuff
    "START_FPS": 60,
    "SCREEN_DIMS": (1280, 720),

    # Player settings
    "MAX_PLAYERS": 3
}

# Change any of the values by using the same key and adjusting the value
overrides: dict[str, Any] = {}

settings = defaults | overrides

def write_settings(s: dict):
    with open(settings_file, "w") as wf:
        json.dump(s, wf, indent=4, sort_keys=True)


def load_settings() -> dict:
    with open(settings_file, "r") as rf:
        return json.load(rf)


def main():
    print("Running settings.py\n\n")
    print("Defaults:")
    print(defaults)



if __name__ == '__main__':
    main()
    print("Program done!")
else:
    write_settings(settings)
