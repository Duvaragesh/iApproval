# This script will be called when the form is submitted.
# It does Image processing, signature prediction using Tensorflow, validates,
# creates Service now request using REST API and write details into database. 
#
# Author Duvaragesh Kannan
#

import sys
sys.path.append("..")
from .scripts import label_image 
from PIL import Image
import os
import requests
from django.utils.datastructures import MultiValueDictKeyError
from pages.models import Emp_details

# Create a Service Now Request using REST API(sysparm_fields)
def createSN(request):
    # Set the request parameters
    url = 'https://dev68305.service-now.com/api/now/table/sc_request?sysparm_fields=number'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'Supla@2526'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    jsondata = "{\"short_description\":\" New Joiner request for " + request.POST['firstname'] + " \",\"requested_for\":\"7ce7d5b5db5a23002110bd51399619b3\",\"request_state\":\"requested\",\"u_category\":\"New Joiner\",\"parent\":\"\",\"approval\":\"Pending\"}"
    print(jsondata)
    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=jsondata)

    # Check for HTTP codes other than 200
    if response.status_code != 201: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    print(data['result']['number'])
    return data['result']['number'] , 'requested'

# Write the details into Database
def writedb(request):
    Empid = request.POST['empid']
    Firstname  = request.POST['firstname']
    Lastname  = request.POST['lastname']
    Emailid  = request.POST['emailid']
    Team_Name = request.POST['team_name']
    Request_Number, Request_Status =  createSN(request)
    p = Emp_details(Empid = Empid,   Firstname = Firstname,  Lastname = Lastname,  Email =Emailid,  Team_Name=Team_Name, Request_Number=Request_Number, Request_Status=Request_Status)
    p.save()

    return Request_Number

# Main Method to validate the input data
def validator(request, file_path):
    img = Image.open(file_path)
    width, height = img.size
    #corp only signature part
    img =img.crop((0,height/2,width,height))
    file_path_new="media/tempImage.jpg"
    img.save(file_path_new)
    team_name1 = request.POST['team_name']
    pred_Sign = ''
    pred_Sign, Pred_Score = label_image.label_image(model_file ='pages/tf_files/retrained_graph.pb' , file_name=file_path_new)
    #print accuracy % in log
    print(round(Pred_Score, 5))

    # Manager Names are currently Hardcoded here
    manager_team =	{
    "Front office Team": "Duvaragesh_Kannan",
    "Mid Office Team": "Mid_Manager",
    "Back Office Team": "Back_Manager",
    "Maintenance Team": "Maint_Manager",
    "Testing Team": "Test_Manager",
    }
    manager_name = manager_team.get(team_name1) 


    # check for the 99% of accuracy on the Signature prediction
    if round(Pred_Score, 5) > 0.99000:
        if manager_name == pred_Sign:
            Req_no = writedb(request)
            return "The uploaded approval form has the signature of " + pred_Sign + " and " + Req_no +" created to get necessary access for you!" 
        else:   
            return "The approval form has the signature of " + pred_Sign + ". You should get it signed by "+ team_name1 +  " manager (" + manager_name + ")"
    else:
        return "Invalid Signature!"
        #+ team_name1 +