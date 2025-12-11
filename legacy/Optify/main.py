import sys
import os
import time
from plyer import notification
from PIL import Image
from pystray import Menu, MenuItem, Icon
from threading import Thread


def get_icon_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "icon.ico")
    else:
        return "icon.ico"


def notify_202020_rule():
    while True:
        time.sleep(20 * 60)
        notification.notify(
            title="Regra 20-20-20!",
            message="Faça uma pausa! Olhe para algo a 20 pés (~6 metros) por 20 segundos.",
            app_name="Optify",
            app_icon=get_icon_path(),
            timeout=10,
        )

def notify_hourly_pause():
    while True:
        time.sleep(60 * 60)
        notification.notify(
            title="Hora de uma pausa!",
            message="Levante-se e mova-se por 5 minutos.",
            app_name="Optify",
            app_icon=get_icon_path(),
            timeout=10,
        )

def notify_water_reminder():
    while True:
        time.sleep(60 * 60) 
        notification.notify(
            title="Hidrate-se!",
            message="Beba um copo d'água.",
            app_name="Optify",
            app_icon=get_icon_path(),
            timeout=10,
        )

def quit_app(icon, item):
    icon.stop()

def setup_tray():
    image = Image.open(get_icon_path())
    menu = Menu(MenuItem("Sair", quit_app))
    icon = Icon("Optify", image, "Optify", menu)
    icon.run()

def main():
   
    Thread(target=notify_202020_rule, daemon=True).start()
    Thread(target=notify_hourly_pause, daemon=True).start()
    Thread(target=notify_water_reminder, daemon=True).start()

    setup_tray()

if __name__ == "__main__":
    main()