# Flow.Launcher.plugin.ColorConverter

A [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher) Python plugin for color convert.

## Install

Since I haven't setup CI/CD for this repo, the plugin must be installed manually.

- Make sure Python has been installed correctly.

- Clone or Download this repo

- move the plugin folder into your Flow.Launcher plugin directory, e.g. `C:\Program Files\FlowLauncher\app-1.18.0\UserData\Plugins`

- Open the console in plugin directory, and type with the following code.

  ```shell
  pip install -r requirement.txt -t ./lib
  ```

- Restart the launcher.

- Now it should be installed successfully, try the keyword `cc:`.

## Usage

### Hex to RGB

```
cc: <hex>
```

Start with `#`, the hex will be converted into RGB format. Press Enter to copy to clipboard.

e.g.

- `#222` will be converted to `34, 34, 34`
- `#343434` will be converted to `52, 52, 52`

### RGB to Hex

```
cc: <RGB>
```

Type RGB value separated by `,`. Press Enter to copy to clipboard.

e.g.

- `12, 169, 233` will be converted to `#0ca9e9`