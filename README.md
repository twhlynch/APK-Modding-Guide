# Basic-APK-Modding-Guide

## Requirements (provided may not always work)
* [sidequest](https://sidequestvr.com/setup-howto)
* [python 3](https://www.python.org/downloads/)
* [apktool (bin/apktool)](https://ibotpeaches.github.io/Apktool/)
* [zipalign (bin/android_sdk)](https://developer.android.com/studio/command-line/zipalign)
* [jarsigner (bin/jre)](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jarsigner.html)
* [keytool (bin/jre)](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)

## Steps

### Download the APK
Download the APK and place it in the same folder as this README.

### Add requirements to PATH
If you are using the provided requirements, add the following to your PATH environment variable:
* `bin/android_sdk`
* `bin/apktool`
* `bin/jre`
* `bin/astcenc`

If you have downloaded the requirements yourself, add their default binaries to the PATH environment variable.

### Decompile the APK
Use the following command to decompile the APK into a folder called \[APK_NAME\]:
```bash
apktool d -f [APK_NAME].apk
```

### Modify the APK
Change whatever

### Recompile the APK
Before you recompile the APK, you can change the package name in order to install the APK separately to the unmodded version. To do this, open `apktool.yml` in a text editor and change the `renameManifestPackage` value to something else. (I use `com.index.[APK_NAME]_modded`)
- Only use letters and underscores

Once you are done, use the following command to recompile the APK from the folder into `[APK_NAME]/dist/[APK_NAME].apk`:
```bash
apktool b -f -d [APK_NAME]
```

### Sign the APK
in order for the APK to work, it needs to be signed. To do this, you need to create a keystore and sign the APK. To do this, run the following commands:
```bash
cd [APK_NAME]/dist
```
```bash
keytool -genkey -v -keystore [KEY_NAME].keystore -alias [KEY_ALIAS] -keyalg RSA -keysize 2048 -validity 10000
```
This will require a few details to create the keystore. I leave the details blank with the following:
```
123456
123456
[Enter]
[Enter]
[Enter]          (6x)
[Enter]
[Enter]
[Enter]
y
```
Now that the keystore is created, we must use it to sign the APK.
```bash
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore [KEY_NAME].keystore [APK_NAME].apk [KEY_ALIAS]
```
It will ask for the keystore's password, previously set to 123456.
```bash
123456
```
Now that the APK is signed, we must zipalign it.
```bash
zipalign -f -v 4 [APK_NAME].apk [APK_NAME]-modded.apk
```
Now that the APK is signed and zipaligned, we can verify it.
```bash
jarsigner -verify -verbose -certs [APK_NAME]-modded.apk
```
Ready to sideload! You will find the APK in `[APK_NAME]/dist/[APK_NAME]-modded.apk`.
