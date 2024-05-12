# Polaris [Yaqube & Jun Yu]
	The system will likely use a video setup instead of static photos. Allows to capture moving vehicles, i.e. Emergency vehicles & Buses
1. **Better Lights Inc.**
     - For incoming vehicles (emergency vehicles, buses) will force it so that the traffic lights passes them, & also determines how close to the traffic light
2. **Old Face Reg.**
     - uses face recognition to allow, & keeps the light on as ppl are approaching.
     - makes the traffic light change if there are no cars
3. **Uses cloud Data**
     - Buzzes a melody when there is a lightning alert, uses humidity to predict rain, and potential difference to see if lightning is gonna strike
     - If lightning is detected, output 'Lightning incoming! Seek Shelter now!'
     - LCD also displays date & time 
4. **Data Collection**
	- Using the images that the camera sees, it will tabulate the amount of vehicles on the road & add them to a data base
	- Allows for tracking of roadways, at certain points of time, also allows for there to be better calibration between traffic lights
	- It then uploads the data into the cloud to be stored, can have like local backup if needed
---
## Code Writing Format
- **Naming**: use CAMEL format; new type -> newType 
- **Error Correction**: Use a function for error correction, there is a error correction for each type; *int, float, bool, str*
- **Comments**: ***REMEMBER TO COMMENT WHAT EACH GROUP OF CODE DOES***
- **Data Files**: Use csv files for the data; a function can be used to read & write the files
