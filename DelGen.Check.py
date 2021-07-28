import os, json, re
from packaging.version import Version

home_dir = os.getcwd()
filesHere = os.listdir()

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
            print("Verified.")
    except:
        print("Failed to find \"guid\" field, make sure it is present in your manifest.")

    print("\nVerifying \"version\"...")
    try:
        testString = json_data["version"]
        try:
            Version(json_data["version"])
            print("Verified.")
        except:
            print("Version number invalid, make sure it follows the \"x.x.x\" semantic versioning.")
    except:
        input("Failed to find \"version\" field, make sure it is present in your manifest.")

    print("\nVerifying \"require\"...")
    try:
        testString = json_data["require"]
        try:
            Version(json_data["require"])
            print("Verified.")
        except:
            print("Version number invalid, make sure it follows the \"x.x.x\" semantic versioning.")
    except:
        input("Failed to find \"require\" field, make sure it is present in your manifest.")

    print("\nVerifying \"dependencies\"...")
    try:
        testDict = json_data["dependencies"]
        
        try:
            if not isinstance(json_data["dependencies"], dict):
                raise Exception("TypeError")
            else:
                print("Verified.")
        except:
            print("\"dependencies\" field is not a dictionary. Make ure it follows the following format:")
            print("{ \"dependency guid\" : \"x.x.x\" } with commas seperating each dependency")
    except:
        print("\"dependencies\" field not found.")

    print("\nVerifying \"name\"...")
    try:
        testString = json_data["name"]
        print("Verified.")
    except:
        print("Failed to find \"name\" field, make sure it is present in your manifest.")

    print("\nVerifying \"description\"...")
    try:
        testString = json_data["description"]
        print("Verified.")
    except:
        print("Failed to find \"description\" field, make sure it is present in your manifest.")

    print("\nVerifying \"authors\"...")
    try:
        if not isinstance(json_data["authors"], list):
            raise Exception("TypeError")
        else:
            print("Verified.")
    except:
        print("Failed to find or confirm validity \"authors\" field, make sure it is present in your manifest and follows correct format:")
        print("Is a list (\'[\' and \']\' encapsulate your object), and dependency strings are seperated by commas.")

    print("\nVerifying \"assets\"...")
    try:
        testDict = json_data["assets"]
        print("\"assets\" field present.")
        print("\tVerifying sub-fields in \"assets\"...")
        try:
            if not isinstance(json_data["assets"], dict):
                raise Exception("TypeError")
            else:
                def checkAssets(fieldname):
                    try:
                        json_data["assets"][fieldname]
                        try:
                            if not isinstance(json_data["assets"][fieldname], dict):
                                raise Exception("TypeError")
                            print("\t" + fieldname +" asset field verified, checking associated files...")

                            for asset in json_data["assets"][fieldname]:
                                print("\t\tChecking " + str(asset) + "...")
                                found = False
                                for file in filesHere:
                                    if file == asset:
                                        print("\t\tVerified asset")
                                        found = True
                                        break
                                if not found:
                                    print("Failed to find asset, make sure it is named correctly.")
                        except:
                            print(fieldname + " assets are not in dictionary format.")
                    except:
                        print("\tMissing " + fieldname + " assets field. (This is not an error)")

                checkAssets("runtime")
                checkAssets("setup")
                checkAssets("patcher")
        except:
            print("\"assets\" field is not a dictionary. Make ure it follows the following format:")
            print("Has a loading stage with { and }.")
    except:
        print("Failed to find \"assets\" dictionary.")
except:
    print("Failed to find file called \"manifest.json\". Please make sure I have read permissions.")

input("\nFinished check, please check errors if present.")