import time
import subprocess

def run_script():
    # path to exe
    command = ["python", "chan_scraper.py", "--board_name", "pol", "--num_threads", "1", "--debug", "False"]
    
    # run command
    subprocess.run(command)

# set desired time for running the script (24-hour format: HH:MM)
desired_time = "18:00"

while True:
    current_time = time.strftime("%H:%M")
    if current_time == desired_time:
        run_script()

        # wait 24 hours before running the script again
        time.sleep(24 * 60 * 60)
    else:
        # check every minute if the desired time has arrived
        time.sleep(60)