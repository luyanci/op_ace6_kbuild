import asyncio
import os
import sys
from telethon import TelegramClient

API_ID = 611335
API_HASH = "d524b414d21f4d37f08684c1df41ac9c"


BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHATID")
MESSAGE_THREAD_ID = os.environ.get("MESSAGE_THREAD_ID")
KSUVAR = os.environ.get("KSUVAR")
SUSFS = os.environ.get("SUSFS")
mountify = os.environ.get("mountify")
BBG = os.environ.get("BBG")
MSG_TEMPLATE = """
**New Build Published!**
#ACE6
```Kernel Info
kernelver: {kernelversion}
KsuVar: {ksuvar}
KsuVersion: {Ksuver}
SUSFS: {SUSFS}
BBG: {BBG}
Mountify support: {mountify}
```
Please follow @gki_kernels_xiaoxiaow !
""".strip()


def get_caption():
    msg = MSG_TEMPLATE.format(
        kernelversion=kernelversion,
        ksuvar=KSUVAR,
        Ksuver=ksuver,
        BBG=BBG,
        SUSFS=SUSFS,
        mountify=mountify,
    )
    if len(msg) > 1024:
        return f"{KSUVAR} {ksuver} {kernelversion}"
    return msg


def check_environ():
    global CHAT_ID, MESSAGE_THREAD_ID
    if BOT_TOKEN is None:
        print("[-] Invalid BOT_TOKEN")
        exit(1)
    if CHAT_ID is None:
        print("[-] Invalid CHAT_ID")
        exit(1)
    else:
        try:
            CHAT_ID = int(CHAT_ID)
        except:
            pass
    if MESSAGE_THREAD_ID is not None and MESSAGE_THREAD_ID != "":
        try:
            MESSAGE_THREAD_ID = int(MESSAGE_THREAD_ID)
        except:
            print("[-] Invaild MESSAGE_THREAD_ID")
            exit(1)
    else:
        MESSAGE_THREAD_ID = None
    get_versions()

def get_kernel_versions():
    version=""
    patchlevel=""
    sublevel=""

    try:
        with open("Makefile",'r') as file:
            for line in file:
                if line.startswith("VERSION"):
                    version = line.split('=')[1].strip()
                elif line.startswith("PATCHLEVEL"):
                    patchlevel = line.split('=')[1].strip()
                elif line.startswith("SUBLEVEL"):
                    sublevel = line.split('=')[1].strip()
                elif line.startswith("#"): # skip comments
                    continue
                else:
                    break
    except FileNotFoundError:
        raise
    return f"{version}.{patchlevel}.{sublevel}"

def get_versions():
    global kernelversion,ksuver
    current_work=os.getcwd()
    if KSU_VAR == "NEXT":
        ksu_folder="KernelSU-Next"
    elif KSU_VAR == "WILD":
        ksu_folder="Wild_KSU"
    else:
        ksu_folder="KernelSU"
    os.chdir(current_work+"/kernel_workspace/kernel_platform/common") #除非next
    kernelversion=get_kernel_versions()
    os.chdir(os.getcwd()+f"/../{ksu_folder}")
    ksuver=os.popen("echo $(git describe --tags $(git rev-list --tags --max-count=1))-$(git rev-parse --short HEAD)@$(git branch --show-current)").read().strip()
    ksuver+=f' ({os.environ.get("KSUVER")})'
    os.chdir(current_work)

async def main():
    print("[+] Uploading to telegram")
    check_environ()
    files = sys.argv[1:]
    print("[+] Files:", files)
    if len(files) <= 0:
        print("[-] No files to upload")
        exit(1)
    print("[+] Logging in Telegram with bot")
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    session_dir = os.path.join(script_dir, "ksubot")
    async with await TelegramClient(session=session_dir, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN) as bot:
        caption = [""] * len(files)
        caption[-1] = get_caption()
        print("[+] Caption: ")
        print("---")
        print(caption)
        print("---")
        print("[+] Sending")
        await bot.send_file(entity=CHAT_ID, file=files, caption=caption, reply_to=MESSAGE_THREAD_ID, parse_mode="markdown")
        print("[+] Done!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"[-] An error occurred: {e}")
