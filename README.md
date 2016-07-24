# InfraReminder

Reminder web app:
A web app for create reminder for users.They just have to provide their details necessary for create reminder. 

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

