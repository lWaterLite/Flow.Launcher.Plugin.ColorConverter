import os
import sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

from flowlauncher import FlowLauncher
import pyperclip


class ColorConverter(FlowLauncher):
    def query(self, param: str = '') -> list | None:
        if not param:
            return []
        if param[0] == "#":
            color = param.lstrip('#')
            if len(color) == 3:
                t_color = ''.join([c * 2 for c in color])
                rgb = map(str, tuple(int(t_color[i:i + 2], 16) for i in (0, 2, 4)))
                rgb_str = ", ".join(rgb)
                return [
                    {
                        "Title": f"{rgb_str}",
                        "SubTitle": f"{rgb_str}",
                        "IcoPath": "Image/app.png",
                        "JsonRPCAction": {
                            "method": "copy",
                            "parameters": [rgb_str]
                        }
                    }
                ]
            elif len(color) == 6:
                rgb = tuple(str(int(color[i:i + 2], 16) for i in (0, 2, 4)))
                rgb_str = ", ".join(rgb)
                return [
                    {
                        "Title": f"{rgb_str}",
                        "SubTitle": f"{rgb_str}",
                        "IcoPath": "Image/app.png",
                        "JsonRPCAction": {
                            "method": "copy",
                            "parameters": [rgb_str]
                        }
                    }
                ]
            else:
                return []
        else:
            rgb = [x for x in param.split(',')]
            if len(rgb) != 3:
                return []
            if rgb[2] == "":
                return []
            rgb = list(map(int, rgb))
            hex_str = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
            return [
                {
                    "Title": f"{hex_str}",
                    "SubTitle": f"{hex_str}",
                    "IcoPath": "Image/app.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [hex_str]
                    }
                }
            ]

    def copy(self, text: str):
        pyperclip.copy(text)


if __name__ == '__main__':
    ColorConverter()
