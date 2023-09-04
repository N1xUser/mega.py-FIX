import os

step = [
    "Starting...",
    "Import mega.py",
    "Extract path",
    "Starting patch mega.py",
    "mega.py READY!",
    "Import tenacity",
    "Starting patch _asyncio.py",
    "_asyncio.py READY!",
]

###
## Why the steps on a list? idk
#


def _print(toPrint, skipSpace=False):

    if skipSpace:
        print(f"\n [+] {toPrint}")
    else:
        print(f" [+] {toPrint}")



def _ModifyTXT(
    mode: int, path, text: str, line: int, customText=None
):              ####
                ### This allow to replace a line of text on a .txt or just add it using a list internally
                ##
    # Mode 0 - add at
    # Mode 1 - replace

    line -= 1
    fText = []

    try:
        with open(path, "r") as file:
            fText = file.readlines()

        if mode == 0:
            fText.insert(line, f"{text}\n")
        else:
            fText[line] = f"{text}\n"

        with open(path, "w") as file:
            for lines in fText:
                file.write(lines)

        if customText != None:
            _print(f"Text '{customText}' inserted at {line + 1}")
        else:
            _print(f"Text '{text}' inserted at {line + 1}")

    except Exception as e:
        _print("Error trying to insert line")
        _print(e)


def _getMxga():
    try:
        _print(step[1], True)
        import random

        path = (
            random.__file__.split("random.py")[0] + "site-packages\\mega\\__init__.py"
        )
    except Exception as e:
        _print(e)
        _print("Error trying to import mega, ending...")
        exit()

    return path


def _getMega():                ####
    try:                       ### Get the path of the mega.py directory, if fails just use a narive import as entry
        _print(step[1], True)  ##
        import mega

        path = mega.__file__
    except Exception as e:
        _print(e)
        _print("Error trying to import mega, nothing to worry about, using brute force")
        path = _getMxga()

    _print(step[2])
    return path


def _getTxnacity():
    try:
        _print(step[5], True)
        import random

        path = (
            random.__file__.split("random.py")[0]
            + "site-packages\\tenacity\\__init__.py"
        )
    except Exception as e:
        _print(e)
        _print("Error trying to import tenacity, ending...")
        exit()

    return path


def _getTenacity():             ####
    try:                        ### Get the path of the tenacity.py directory, if fails just use a narive import as entry
        _print(step[5], True)   ##
        import tenacity

        path = tenacity.__file__
    except Exception as e:
        _print(e)
        _print(
            "Error trying to import tenacity, nothing to worry about, using brute force"
        )
        path = _getTxnacity()

    _print(step[2])
    return path

                                    ####
def _valid(c_dir, c_file):          ### Validates if the directory of the import is valid
    if "__init" in c_dir:           ##
        megaPath = c_dir.split("__init")[0] + f"{c_file}"
        return [True, megaPath]

    else:
        _print("Error with the Lib path, ending...")
        return [False, "..."]


def _backup(f_path, f_type):    ####
                                ### If a backup is not detected it makes one on the same directory
    bk = True                   ##
    data = []

    if f_type in f_path:

        f_path = f_path.split(f_type)[0]

        try:

            with open(f"{f_path}{f_type}", "r") as x:
                data = x.readlines()

        except Exception as e:

            _print(e)
            _print("Error during backup")
            bk = False

        if bk:
            try:
                with open(f"{f_path}_backup{f_type}", "r") as x:
                    if len(x.readlines()) >= 5:
                        bk = False
            except Exception as e:
                if "No such file or directory" in str(e):
                    with open(f"{f_path}_backup{f_type}", "w") as x:
                        for lines in data:
                            x.write(lines)
                    _print(f"Backup -> {f_path}_backup{f_type}")
                else:
                    _print(e)
                    _print("Error during len")
        else:
            _print("Error, skipping backup")
    else:
        _print("Error, skipping backup")


def _patchMega(path):                   ####
                                        ### It patch the mega.py file, inserting a line at 745 only if shutil.move(temp_output_file.name, output_path) is there
    c_mega = _valid(path, "mega.py")    ##

    if c_mega[0]:
        megaPath = c_mega[1]
        _backup(c_mega[1], ".py")
        try:
            with open(megaPath, "r") as lib:

                line = lib.readlines()[744]
                _print(step[3])

                if (
                    "shutil.move(temp_output_file.name, output_path)" in line
                    or "temp_output_file.close()" in line
                ):

                    if "shutil.move(temp_output_file.name, output_path)" in line:

                        _ModifyTXT(
                            0,
                            megaPath,
                            "            temp_output_file.close()",
                            745,
                            "temp_output_file.close()",
                        )
                        _print(step[4])

                    else:
                        _print("mega.py already patched, skipping")
                        _print(step[4])

                else:

                    _print("Malformed mega.py detected, try re-install the Lib")

        except Exception as e:

            _print("Error trying to read mega.py")
            _print(e)
    else:
        _print("Unknown error...")


def _patchTenacity(
    path,                   #####
):                          ### It patch the _asyncio.py file, replacing lines 41, 42, 51 and 58.
                            ##

    c_tenacity = _valid(path, "_asyncio.py")

    if c_tenacity[0]:

        tenacityPath = c_tenacity[1]
        _backup(c_tenacity[1], ".py")
        _print(step[6])

        try:

            with open(tenacityPath, "r") as lib:
                lines = lib.readlines()
                _ModifyTXT(
                    1,
                    tenacityPath,
                    "        #@asyncio.coroutine",
                    41,
                    "#@asyncio.coroutine",
                )
                _ModifyTXT(
                    1,
                    tenacityPath,
                    "        async def call(self, fn, *args, **kwargs):",
                    42,
                    "async def call(self, fn, *args, **kwargs):",
                )
                _ModifyTXT(
                    1,
                    tenacityPath,
                    "                        result = await fn(*args, **kwargs)",
                    51,
                    "result = await fn(*args, **kwargs)",
                )
                _ModifyTXT(
                    1,
                    tenacityPath,
                    "                    await self.sleep(do)",
                    58,
                    "await self.sleep(do)",
                )
                _print(step[7])

        except Exception as e:
            _print("Error trying to read _asyncio.py")
            _print(e)
    else:
        _print("Unknown error...")


if __name__ == "__main__":

    if (
        "yes"
        in input(
            "\n [+] Before continue, please make manually a backup of your mega.py Lib\n [+] You want to continue write [Yes]: "
        ).lower()
    ):

        _print(step[0], True)
        pathMega = _getMega()
        _patchMega(pathMega)

        pathTenacity = _getTenacity()
        _patchTenacity(pathTenacity)

        _print("[END]", True)

    else:
        _print("Exit...", True)
