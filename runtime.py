import InsightAddon
import insightTracker
import LCDoutput
import ultrasound
import appSite


def run_the_scripts():
    #Runs the website
    appSite.run_appSite()
    #Runs the LCD & keypad
    LCDoutput.run_LCDoutput()
    
    #runs ultrasound then Tracker , Addon
    ultrasound.run_ultrasound()
    insightTracker.run_insightTracker()
    InsightAddon.run_InsightAddon()
    
    print('DONE?')
    
if __name__ == "__main__":
    while True:
        try:
            run_the_scripts()
        except KeyboardInterrupt:
            print('NOt doing it')
        finally: break