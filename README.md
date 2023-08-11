# APK-Modding-Guide

## Requirements
- [sidequest](https://sidequestvr.com/setup-howto) (for sideloading after modding)
- [Apktool](https://ibotpeaches.github.io/Apktool/) added to PATH
- [JDK](https://www.oracle.com/java/technologies/downloads/) added to PATH
- [zipalign and Apksigner (Command-line tools)](https://developer.android.com/studio#command-line-tools-only) added to PATH (use /bin/android_sdk)

## Steps

### Setup

- Download the APK and place it in the same folder as this README.
- Add the requirements to your PATH environment variable:

### Decompile the APK
```bash
apktool d -f [APK_NAME].apk
```
Use this command to decompile the APK into a folder called \[APK_NAME\]:

### Modify the APK
This is where you can make changes to the apk. The most basic way would be swapping out audio or texture assets.

You can also change the package name in order to install the APK separately to the unmodded version. To do this, open `apktool.yml` in a text editor and change the `renameManifestPackage` value to something else. (eg, `com.index.[APK_NAME]_modded`)
> Only use letters and underscores
### Recompile the APK
```bash
apktool b -f --use-aapt2 -d [APK_NAME]
```
This command will recompile the APK into `[APK_NAME]/dist/[APK_NAME].apk`:

### Create a keystore
> Coming soon, for now use the keys in /tools

### Traverse to the folder containing the APK
```bash
cd [APK_NAME]/dist
```

### Align the APK
```bash
zipalign -p 4 [APK_NAME] aligned-[APK_NAME]
```
This command will align the APK into `aligned-[APK_NAME].apk`:

### Sign the APK
```bash
ApkSigner sign --key index.pk8 --cert index.pem --v4-signing-enabled false --out modded-[APK_NAME].apk aligned-[APK_NAME].apk
```
This command will sign the APK

Ready to sideload! You will find the APK as `[APK_NAME]/dist/modded-[APK_NAME].apk`.

## Disclaimer

Please note that modifying APK files of games or any other applications may infringe on the terms of service and may be against the law. Ensure that you have proper authorization and comply with the relevant legal requirements before using this guide. The author of this guide holds no responsibility for any misuse or illegal activities conducted using it.