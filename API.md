#Reminder Web API

Returns json data about a single reminder.

    GET /api/v1/id/ 
    PUT /api/v1/id/
    DELETE /api/v1/id/

    URL: /api/v1/id/

    Method: GET, PUT, DELETE

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

    Error Response:
        code:404
        Content:{error :Not Found}

    Sample call:
        GET /api/v1/3/

        Success Response :
        Code : 200
        Content: {
            "url": "http://localhost:8000/api/v1/3/",
            "date" : "2016-07-24",
            "time" : "12:40:00",
            "email_id" :"amanbabugautam@gmail.com",
            "phone_no": "7289987746",
            "message" : "Meeting"
        }

Returns json data of all the reminders.

    GET /api/v1/

    URL : /api/v1/

    Method :GET

    URL Params :NONE
    Data Params : NONE

    Success Response:
        code :200
        Content : [
            {
                "url": "http://localhost:8000/api/v1/2/",
                "date": "2016-07-24",
                "time": "00:18:00",
                "email_id": "amanbabugautam@gmail.com",
                "phone_no": "7289987746",
                "message": "Food"
            },
            {
                "url": "http://localhost:8000/api/v1/3/",
                "date" : "2016-07-24",
                "time" : "12:40:00",
                "email_id" :"amanbabugautam@gmail.com",
                "phone_no": "7289987746",
                "message" : "Meeting"
            }
        ]

    Error Response:
        code:404
        Content : []

Handle POST request on the API to set a reminder.
    
    POST /api/v1/
    URL : /api/v1/

    Method : POST

    URL Params : None

    Data params : {
        
                "date": "2016-07-27",
                "time": "20:18:00",
                "email_id": "amanbabugautam@gmail.com",
                "phone_no": "7289987746",
                "message": "Post Api Handle"
            }
    Success Response:
        code : 201
        Content : {

                "url": "http://localhost:8000/api/v1/4/",
                "date": "2016-07-27",
                "time": "20:18:00",
                "email_id": "amanbabugautam@gmail.com",
                "phone_no": "7289987746",
                "message": "Post Api Handle"
        }
    Error Response :
        code : 403
        Content : {
            error: forbidden
        }
