#!/bin/bash

#Function to run the script & keep it running (FROM chatGPT)
start_script() {
  local script_name=$1
  while true; do
    python3 $script_name
    echo "$script_name crashed with exit code $?.  Respawning.." >&2
    sleep 1
  done
}

#Start when no API key
start_script insightTracker.py
echo "Started Insight Tracker"

#Starts insight add on
start_script InsightAddon.py
echo "Started insight add on"

#Starts the ultrasound
start_script ultrasound.py
echo "started ultrasound"

#this starts the wensite on the local network
start_script /Web Server/app.py
echo "started Website"
#Turns on LCD & keypad
start_script LCDoutout.py
echo "Start LCD"


