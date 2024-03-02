from datetime import datetime
import mss # pip install mss
import sched
import time


def take_screenshots(scheduler):
    scheduler.enter(900, 1, take_screenshots, (scheduler,))
    print("Taking screenshot...")
    formatted_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with mss.mss() as sct:
        if len(sct.monitors) < 2:
            return
        for monitor_number, mon in enumerate(sct.monitors[1:], 1):
            output = f"./screenshot-{formatted_date}-mon{monitor_number}_{mon['top']}x{mon['left']}_{mon['width']}x{mon['height']}.png"
            sct_img = sct.grab(mon)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

screenshot_scheduler = sched.scheduler(time.time, time.sleep)
screenshot_scheduler.enter(10, 1, take_screenshots, (screenshot_scheduler,))
screenshot_scheduler.run()

