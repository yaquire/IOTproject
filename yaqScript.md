## Slide 1: Title
- Reason for name: John Doe is the name given to people with unknown identities
## Slide 5: Problems Faced
 So, we have found 3 problems faced by these individuals; losing customers due to slow service, stressed & fatigue from operating the shop, unable to track business statistics. Their stress & fatigue is due to them being the only ones running the store for long periods of time. This is leads to them likely being slow to service customers. This fatigue is also likely to make it difficult to handle the business analytics of the store. This problems are more common in stores which operate with only 1 person, regardless of the type of product sold. 

## Slide 6: Brainstorming 
Thus to relive, these issues, we have come up with 4 ideas that we plan to implement. 
- Order A Head
	- This is mean to be a way for customers to check stock & order online so that they can pick up @ the store
- Insight Tracker
	- A business analytics tracker model, where sales, the number of people who come to the store & other metrics are kept & displayed to the client 
- Live Chat Support 
	- Live chat support that customers can chat to in real time
- Promotion Codes
	- Codes & Cards that the store can offer to customers that they can use for discounts on their purchases
	- They can offer cards exclusively for the store, that the customer can buy 

## Slide 8: Overall Block Diagram 
The main connecting feature is obviously the RPi, with data exchange being for the payment software & website so that the data can be transferred to the Thingspeak channel to be stored remotely. The left side of the diagram consists of input channels; the payment & online order, ultrasound sensor to detect the number of ppl entering the store. While, the right is the output devices; the buzzer to indicate successful payment, the website & insight tracker which get updated after the purchase alongside the item data.


## Slide 9: Flowcharts 
Now moving onto the flowcharts, this consists of the Order A Head system, Insight Tracker & the RFID reader, which is the Proomcodes

## Slides 13: Data Flow
This is how the data flow will work for the system. The input of data comes from the barcode scanner; for sold items, ultra sound; for ppl who come to the store, RFID reader; for payment & discount codes. This is fed to the RPi which arranges the data neatly for the cloud, so that it can be displayed easily on the dashboard & website

## Slides 14: Gannt Chart
This is our timeline (goes on to mew); describes content comprehensively 