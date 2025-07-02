import importlib.metadata as metadata
from packaging.version import Version

requirements = {
    "click": ("newer", "8.0"),
    "rich": ("older", "13.0"),
    "packaging": ("newer", "21"),
    "colorama": ("older", "0.4"),
    "pyfiglet": ("newer", "0.8")
}

all_ok = True

for pkg, (req_type, ver) in requirements.items():
    try:
        installed = metadata.version(pkg)
        current = Version(installed)
        required = Version(ver)
        if req_type == "older":
            if current >= required:
                print(f"'{pkg}' version too new: {installed} (want older than {ver})")
                all_ok = False
        else:
            if current < required:
                print(f"'{pkg}' version too old: {installed} (want newer than {ver})")
                all_ok = False
    except metadata.PackageNotFoundError:
        print(f"'{pkg}' is not installed.")
        all_ok = False

if all_ok:
    import pyfiglet
    from colorama import Fore, Style, init
    init(autoreset=True)
    banner = pyfiglet.figlet_format("All Good!")
    print(Fore.GREEN + banner + Style.RESET_ALL)
else:
    print("\nPlease adjust your package versions to meet the requirements.")
