import time
import webbrowser
import schedule
import os



TARGET_TIME = "11:25" 


NEWS_FEED_URL = "https://bbc.com"

def ask_and_open_news():
    print(f"\n--- TRIGGER TIME HIT ({TARGET_TIME}): Launching Ubuntu Native Question Box ---")
    
    
    exit_status = os.system('zenity --question --title="Daily News Prompt" --text="Your scheduled time has arrived! Do you want to open the live news feed right now?" --width=350')
    
    
    if exit_status == 0:
        print("User clicked YES. Launching your browser news dashboard...")
        webbrowser.open(NEWS_FEED_URL)
    else:
        print("User clicked NO or closed the prompt window. Sleeping until tomorrow...")


schedule.every().day.at(TARGET_TIME).do(ask_and_open_news)

print(f"News notification system is active. Sitting quietly in background...")
print(f"Will prompt you daily at exactly {TARGET_TIME}.")

# Background loop keeping the automation sequence alive
while True:
    schedule.run_pending()
    time.sleep(1)

