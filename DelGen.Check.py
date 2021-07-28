import os, json, re
from packaging.version import Version

home_dir = os.getcwd()

print("Working in " + home_dir)
print("\nLoading manifest...")

try:
    with open("manifest.json") as f:
        json_list = f.readlines()
        json_list[0] = "{\n"
        json_data = json.loads("".join(json_list))
    
    print("Found manifest.")

    print("\nVerifying \"guid\"...")
    try:
        testString = "".join(re.findall("[a-z_0-9.]", json_data["guid"]))
        if not testString == json_data["guid"]:
            print("Your \"guid\" is incorrectly formatted, please change it to follow the regex of:")
            print("\"a-z\", \"0-9\", \"_\", \".\"")
        else:
            print("Verified")
    except:
        print("Failed to find \"guid\" field, make sure it is present in your manifest.")

    print("\nVerifying \"version\"...")
    try:
        testString = json_data["version"]
        try:
            Version(json_data["version"])
            print("Verified")
        except:
            print("Version number invalid, make sure it follows the \"x.x.x\" semantic versioning.")
    except:
        input("Failed to find \"version\" field, make sure it is present in your manifest.")

    print("\nVerifying \"require\"...")
    try:
        testString = json_data["require"]
        try:
            Version(json_data["require"])
            print("Verified")
        except:
            print("Version number invalid, make sure it follows the \"x.x.x\" semantic versioning.")
    except:
        input("Failed to find \"require\" field, make sure it is present in your manifest.")

except:
    input("Failed to find file called \"manifest.json\". Please make sure I have read permissions.")
