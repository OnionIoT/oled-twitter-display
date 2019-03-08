# Twitter Onion IoT Wearble Name Badge
Twitter IoT Name badge Displays your twitter feed on a badge using Twitter REST API

![Webpage for this project](https://amiedd.github.io/oled-twitter-display/)

![Wearable Twitter Feed Badge](http://amiedd.com/blogimageuploads/amiedd-github.jpg)

## Twitter IoT Name badge Hardware Ingredients
1. Onion Omega2+
2. Onion OLED display
3. Onion OLED expansion dock

## Thingiverse STL Files
[Twitter 3D Print Badge Files](https://www.thingiverse.com/thing:2438237).

Displays your twitter feed on a badge

## Installation

```
opkg update
opkg install python-light python-urllib3 pyOledExp
```


## Known issues
1. No space left on device
  * This may happen if you have installed the `editor` or `terminal` on the Omega2. If you have previously installed these components, you can remove them with the `opkg remove` commands. You can do a `opkg list` to check if you have the modules installed on your Omega2, and if it's there ( look for `onion-console-xxx`), you can remove them with `opkg remove onion-console-terminal` etc. Once you have removed the `onion-console-terminal`, `onion-console-editor` and `onion-console-base`, you should be able to download and install the remaining `python-urllib3` and `pyOledExp` modules with  `opkg install python-light python-urllib3 pyOledExp`. Since we won't have the editor on the omega2 anymore, you will have to `scp` your updates files to the omega2 or change the file with native linux text editor `vim` and edit your `username`, `consumer API key`, and `consumer API key (secret)` in the `config.json` file.

2. Something went wrong when running the mainProgram() in the [`olderTwitterDisplay.py`](https://github.com/AmieDD/oled-twitter-display/blob/master/oledTwitterDisplay.py)
  * In this case, it's something to do with the ssl module on your OS system where it might not be able to make `HTTPS` requests. So you will have to change L8 of `oledTwitterDisplay.py` file to [`baseUrl = "http://api.twitter.com"`](https://github.com/AmieDD/oled-twitter-display/blob/master/oledTwitterDisplay.py#L8)
  
3. Text on the OLED display is upside down. 
  * Working on a solution

## Questions?
amie@amiedd.com
https://www.amiedd.com
