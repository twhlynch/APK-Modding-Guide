import os, subprocess, argparse

def decompile(APK_FILE_NAME, OUTPUT_FOLDER=False):
    if not OUTPUT_FOLDER:
        OUTPUT_FOLDER = os.path.splitext(APK_FILE_NAME)[0]

    print(f"Decompiling {APK_FILE_NAME} into {OUTPUT_FOLDER}...")
    
    sp = subprocess.Popen(["apktool", "d", "-f", APK_FILE_NAME, "-o", OUTPUT_FOLDER], shell=True, stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

def recompile(APK_FOLDER_NAME, OUTPUT_FILE=False, PACKAGE_NAME=False):
    if not OUTPUT_FILE:
        OUTPUT_FILE = f"{APK_FOLDER_NAME}.apk"
    if not PACKAGE_NAME:
         ADJUSTED_APK_FOLDER_NAME = APK_FOLDER_NAME.replace("-", "_")
         PACKAGE_NAME = f"com.index.{ADJUSTED_APK_FOLDER_NAME}_modded"

    print(f"Changing package name to {PACKAGE_NAME}...")
    
    with open(f"{APK_FOLDER_NAME}/apktool.yml", 'r') as file:
        filedata = file.read()        
    filedata = filedata.replace("renameManifestPackage: null", f"renameManifestPackage: {PACKAGE_NAME}")        
    with open(f"{APK_FOLDER_NAME}/apktool.yml", 'w') as file:
        file.write(filedata)

    print(f"Building {APK_FOLDER_NAME} into {OUTPUT_FILE}...")

    sp = subprocess.Popen(["apktool", "b", "-f", "-d", APK_FOLDER_NAME, "-o", f"tmp-{OUTPUT_FILE}"], shell=True, stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

    print(f"Signing {OUTPUT_FILE}...")

    # print('\033[32m'+'Password is 123456'+'\033[37m')
    sp = subprocess.Popen(["jarsigner", "-verbose", "-sigalg", "SHA1withRSA", "-digestalg", "SHA1", "-keystore", "index.keystore", f"tmp-{OUTPUT_FILE}", "index"], shell=True, stdin=subprocess.PIPE)
    sp.communicate(input=b'123456\n')

    print(f"Aligning {OUTPUT_FILE}...")

    sp = subprocess.Popen(["zipalign", "-f", "-v", "4", f"tmp-{OUTPUT_FILE}", f"modded-{OUTPUT_FILE}"], shell=True, stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

    print(f"Verifying {OUTPUT_FILE}...")

    sp = subprocess.Popen(["jarsigner", "-verify", "-verbose", "-certs", f"modded-{OUTPUT_FILE}"], shell=True, stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')
    
    os.remove(f"tmp-{OUTPUT_FILE}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APK Decompiler, Recompiler, Signer, Aligner, and Verifier.")
    parser.add_argument("-d", "--decompile", action="store_true", help="Decompile the APK")
    parser.add_argument("-r", "--recompile", action="store_true", help="Recompile the APK")
    parser.add_argument("apk", help="APK file to decompile or folder to recompile")
    parser.add_argument("-o", "--output", help="Output folder for decompiled APK or output file for recompiled APK")
    parser.add_argument("-p", "--package_name", help="Package name for recompiled APK. Defaults to 'com.index.[apk]_modded'. ONLY LETTERS AND UNDERSCORES.")
    args = parser.parse_args()

    if args.decompile:
        decompile(args.apk_file, args.output)
        print("APK decompiled successfully!")

    if args.recompile:
        recompile(args.apk_file, args.output)
        print("APK recompiled successfully!")
