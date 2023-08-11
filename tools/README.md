# ModAPK.py

ModAPK.py allows you to decompile and recompile APKS automatically. It uses [Apktool](https://ibotpeaches.github.io/Apktool/) to decompile and recompile the APK and [zipalign](https://developer.android.com/studio/command-line/zipalign) and [Apksigner](https://developer.android.com/studio/command-line/apksigner) to align and sign the APK.

## Usage

`python ModAPK.py [-h] [-d] [-r] [-o OUTPUT] [-p PACKAGE_NAME] apk`

### Arguments
- -h, --help: Show the help message and exit.
- -d, --decompile: Decompile the APK.
- -r, --recompile: Recompile the APK.
- apk: Path to the APK file to decompile or the folder to recompile.
- -o, --output: (Optional) Output folder for the decompiled APK or output file for the recompiled APK. Defaults to 'modded-[apk]'.
- -p, --package_name: (Optional) Package name for the recompiled APK. Defaults to 'com.index.[apk]_modded'. Only letters and underscores are allowed.

### Examples

Decompile an APK:

`python ModAPK.py -d mygame.apk -o decompiled`

Recompile an APK with a custom package name:

`python ModAPK.py -r decompiled -o modified.apk -p com.me.mygame_modified`

## Disclaimer

Please note that modifying APK files of games or any other applications may infringe on the terms of service and may be against the law. Ensure that you have proper authorization and comply with the relevant legal requirements before using this script. The authors of ModAPK.py hold no responsibility for any misuse or illegal activities conducted using this script.
