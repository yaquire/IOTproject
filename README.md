https://www.canva.com/design/DAGFNaMvKn4/P_g8dsA2eISCfiNJrH0dXw/edit?utm_content=DAGFNaMvKn4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
![Gannt](https://github.com/yaquire/IOTproject/assets/136306256/c9b63d19-ab84-438e-a757-37a9bf56179b)

## Tasks
#### Set up cloud (JY)
- [ ]   Create the Thingspeak account
- [ ] Create the channels for the data (sales & people that come into the store)
#### Code the Website (Yaq)
- [ ] Create the folders & files for the Website (static, template, python)
- [ ] Create the main landing page of the Website 
- [ ] Create the page for the database of items in the site
- [ ] Allow for the page to be updated using info from the Thingspeak channel
#### Code Inside Tracker 
- [ ] Create the first files 
- [ ] Create the parts that allow for data to be taken in from the Thingspeak channel
- [ ] Create the input for the Ultrasound
- [ ] Create the formulas & code for the insight 
- [ ] Code the output in the form of Charts & Graphs

#### Code Promo Code, Sensor (Yaq)
- [ ] Create the files & needed modules
- [ ] Add promo codes 
- [ ] Allow for reading of RFID 
- [ ] Show output of RFID 

#### Create Audio Play Back (JY)
- [ ] Create the files & needed modules
- [ ] Add the input of payment; works/ not working 
- [ ] Add the code for the buzzer to buzz when it works 
- [ ] Adds differing buzzes for works & not works 

#### Creat LCD Output (JY)
- [ ] Create the files & needed modules
- [ ] Make the input code for the output 
- [ ] Mold the output to fit in the LCD

# New Idea [Yaqube & Jun Yu]

| Idea               | Detail                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------- |
| *RFID*             | used for discount cards for customers                                                        |
| *Thingspeak*       | Used to store the data; QR codes of the items, items purchased, estimated stock in the store |
| *Playback/Speaker* | Used to indicate the status of the purchase                                                  |
| *LCD*              | Show errors & QR code for paynow                                                             |
| *Keypad*           | Add discount code manually or add item number                                                |
| *Ultrasound*       | Used to estimate the number of people who have entered the store                             |
| *Web Server*       | Allow online access to the store, see the stock available                                    |

---
## Code Writing Format
- **Naming**: use CAMEL format; new type -> newType 
- **Error Correction**: Use a function for error correction, there is a error correction for each type; *int, float, bool, str*
- **Comments**: ***REMEMBER TO COMMENT WHAT EACH GROUP OF CODE DOES***
- **Data Files**: Use csv files for the data; a function can be used to read & write the files
