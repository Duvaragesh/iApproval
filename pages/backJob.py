# This job should be running in the background 
# to check for the status of all the new joiner and
# create the sub request and update the database record
#
# Author Duvaragesh Kannan
import requests
from pages.models import Emp_details
import time

while True:
    for Emp in Emp_details.objects.all():
         if Emp.Request_Status != "closed_complete":
            print(Emp.Request_Number +":"+Emp.Request_Status)
            url = 'https://dev68305.service-now.com/api/now/table/sc_request?sysparm_query=number='+ Emp.Request_Number
			
			# Credentials are hardcoded here
            user = 'admin'
            pwd = 'Supla@2526'

            headers = {"Content-Type":"application/json","Accept":"application/json"}
            response = requests.get(url, auth=(user, pwd), headers=headers  )

            if response.status_code != 200: 
                print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            exit()

            data = response.json()
            new_status = data['result'][0]['request_state']
            print(new_status)
            if new_status == "closed_complete":
                url = 'https://dev68305.service-now.com/api/now/table/sc_request?sysparm_fields=number'

                jsondata = "{\"short_description\":\" New Joiner Sub request for " + Emp.Firstname + " to get Team Based application accesses \",\"requested_for\":\"7ce7d5b5db5a23002110bd51399619b3\",\"request_state\":\"requested\",\"u_category\":\"New Joiner\",\"parent\":\""+ Emp.Request_Number +"\",\"approval\":\"Approved\"}"
                # Do the HTTP request
                response = requests.post(url, auth=(user, pwd), headers=headers ,data=jsondata)

                # Check for HTTP codes other than 200
                if response.status_code != 201: 
                    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
                    exit()
                # Decode the JSON response into a dictionary and use the data
                data = response.json()

                Emp.Sub_Request_Number = data['result']['number']
                Emp.Sub_Request_Status = "requested"
                Emp.Request_Status = new_status
                print(Emp.Request_Number +":"+Emp.Request_Status+":"+Emp.Sub_Request_Number+":"+Emp.Sub_Request_Status)
                Emp.save()

    print("Bob Job Slept for  {}...".format(3))
    time.sleep(3)
    print("Bob Job Waked ...")

