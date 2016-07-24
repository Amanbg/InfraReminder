#Reminder web app

This is the Reminder webapp.Users can open the webapp, provide either their email address or their mobile number or both and setup a reminder with a message.Then the app reminds them over their preferred channel of notification with the message.

Create mocks for the sms and email send for the reminder.
Users can simply input date , time , reminder message,contact for sms and email id for email.
They can change the reminder date and time according to their prefrences.

User Api endpoint:

Returns json data about a single user.

    URL: http://localhost:8000/api/v1/id/

    Method: GET

    URL Params: Required:
				id=[integer]

    Data Params :None

    Success Response:
        Code: 200
        Content: { 
        	"url": "http://localhost:8000/api/v1/2/",
    	    "date": "2016-07-24",
    	    "time": "00:18:00",
   		    "email_id": "amanbabugautam@gmail.com",
    		"phone_no": "7289987746",
    		"message": "Food"
    	}

