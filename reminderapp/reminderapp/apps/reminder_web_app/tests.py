
from rest_framework import status
from rest_framework.test import APITestCase
from reminder_web_app.models import Reminder

# Create your tests here.

class CreateReminderTest(APITestCase):
    """
    Tests for POST request on API to create reminder.
    """
    def test_create_reminder(self):
        """
        Method to test POST request on the API by posting some data.
        """
        data = {
                'date':'2016-07-26',
                'time':'18:56',
                'email_id':'amanbabugautam@gmail.com',
                'phone_no':'7289987746',
                'message':'Write tests for api',
            }

        url = '/api/v1/'
        response = self.client.post(url, data, format='json')
        print "response : ",response
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class ReadReminderTest(APITestCase):
    """
    Tests for GET request on API to retrieve data.
    """
    def setUp(self):
        """
        Create some reminder objects and save to the database.
        """
        self.reminder_object_1 = Reminder(
                                        date = '2016-07-26',
                                        time = '19:30',
                                        email_id = 'amanbabugautam@gmail.com',
                                        phone_no = '7289987746',
                                        message = 'Written test for api'
                                    )
        self.reminder_object_1.save()

        self.reminder_object_2 = Reminder(
                                        date='2016-07-26',
                                        time='20:30',
                                        email_id='amanbabugautam@gmail.com',
                                        phone_no='7289987746',
                                        message='Another test for api'
        )
        self.reminder_object_2.save()

    def test_read_reminder_list(self):
        """
         GET request test on API to get the list of reminder objects.
        """
        url = '/api/v1/'
        response = self.client.get(url)
        print "response_2 : ",response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_reminder_detail(self):
        """
         GET request test on API to get an instance from the reminder list.
        """
        url = '/api/v1/2/'
        response = self.client.get(url)
        print "response_3 : ", response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

