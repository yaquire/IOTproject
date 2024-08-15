import multiprocessing
import subprocess
import threading


def run_website():
    # runs the website first
    subprocess.Popen('python3 appSite.py', shell=True)
    print('DONE website?')


def run_LCD():
    subprocess.Popen('python3 LCDoutput.py', shell=True)
    print('Done LCD & keypad')


def run_Ultrasound():
    subprocess.Popen('python3 ultrasound.py', shell=True)
    print('Done Ultrasound')


def run_Insight_Tracker():
    subprocess.Popen('python3 insightTracker.py', shell=True)
    print('Done Insight Tracker')


if __name__ == "__main__":
    while True:
        try:
            multiPro = []
            # starts the website
            website_process = multiprocessing.Process(target=run_website)
            multiPro.append(website_process)
            # Website doesnt turn off
            # for the LCD & Keypad
            LCD_process = multiprocessing.Process(target=run_LCD)
            # LCD also doesnt turn off automatically
            multiPro.append(LCD_process)
            for i in multiPro:
                i.start()

            ##########################################################################################
            threads = []
            Ultrasound_thread = threading.Thread(target=run_Ultrasound)
            threads.append(Ultrasound_thread)
            Insight_thread = threading.Thread(target=run_Insight_Tracker)
            threads.append(Insight_thread)
            for thr in threads:
                thr.start()
        except KeyboardInterrupt:
            print('NOt doing it!!!')
            for i in multiPro:
                i.join()
            for i in threads:
                i.join()
            # stops the processes
        finally:
            break
