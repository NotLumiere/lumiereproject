# greyvbss
# cilik-userbot


from Lumiere import CMD_HELP
from Lumiere.lumi import ayiin_cmd

from . import cmd


@ayiin_cmd(pattern="skull(?: |$)(.*)")
async def _(event):
    await event.edit("███████████████████████████\n"
                     "███████▀▀▀░░░░░░░▀▀▀███████\n"
                     "████▀░░░░░░░░░░░░░░░░░▀████\n"
                     "███│░░░░░░░░░░░░░░░░░░░│███\n"
                     "██▌│░░░░░░░░░░░░░░░░░░░│▐██\n"
                     "██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n"
                     "██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n"
                     "██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n"
                     "██▌░│██████▌░░░▐██████│░▐██\n"
                     "███░│▐███▀▀░░▄░░▀▀███▌│░███\n"
                     "██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n"
                     "██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n"
                     "████▄─┘██▌░░░░░░░▐██└─▄████\n"
                     "█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n"
                     "████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n"
                     "█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n"
                     "███████▄░░░░░░░░░░░▄███████\n"
                     "██████████▄▄▄▄▄▄▄██████████\n"
                     "███████████████████████████\n")


@ayiin_cmd(pattern="wlc(?: |$)(.*)")
async def _(event):
    await event.edit("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                     "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
                     "█░░║║║╠─║─║─║║║║║╠─░░█\n"
                     "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
                     "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


@ayiin_cmd(pattern="klb(?: |$)(.*)")
async def _(event):
    await event.edit("   ╚⊙ ⊙╝..\n"
                     "   ╚═(███)═╝\n"
                     "    ╚═(███)═╝\n"
                     "       ╚═(███)═╝\n"
                     "        ╚═(███)═╝\n"
                     "        ╚═(███)═╝\n"
                     "        ╚═(███)═╝\n"
                     "      ╚═(███)═╝\n"
                     "     ╚═(███)═╝\n"
                     "    ╚═(███)═╝ \n"
                     "    ╚═(███)═╝\n"
                     "     ╚═(███)═╝\n"
                     "      ╚═(███)═╝\n"
                     "       ╚═(███)═╝\n"
                     "        ╚═(███)═╝\n"
                     "        ╚═(███)═╝\n"
                     "       ╚═(███)═╝\n"
                     "      ╚═(███)═╝\n"
                     "     ╚═(███)═╝\n"
                     "     ╚═(███)═╝\n"
                     "      ╚═(█)═╝\n")


@ayiin_cmd(pattern="fucek(?: |$)(.*)")
async def _(event):
    await event.edit("░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░\n"
                     "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                     "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                     "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                     "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                     "██████▄███▄████░░███▄░░░░░░░\n"
                     "▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░\n"
                     "▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░\n"
                     "▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░\n"
                     "▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░\n"
                     "▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░\n"
                     "▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░\n")


CMD_HELP.update(
    {
        "animasi": f"**Plugin : **`animasi`\
        \n\n  »  **Perintah :** `{cmd}skull`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}wlc`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}klb`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}fucek`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
