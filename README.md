# iApproval
Simplifying Onboarding, Approval & Request Creation Processes using Machine Learning(Tensorflow)/Python/Django/REST-API/ServiceNow

Problem statement:
-
 A new Joinee in a project will not have access to any of the client applications and servicenow to create a Joiner request. He/she needs help from an existing team member to create a new Joiner request to get the profile created and then keep chasing them for the status of the request. Once the Joiner request is completed then he/she has to create multiple requests to get access to all the client applications. This process is time consuming and too many manual interventions involved. The new joiner will not be productive untill they get access.  

Solution:
-
 A new Joiner Just fill a request form, get the signature from the corresponding team manager and upload it in iApproval application.

Processes in iApproval:
-
	iApproval does the image processing on the uploaded request form and predicts the manager name from the signature present in the form using Tensorflow.

	It validates the predicted manager's signature against the actual manager name of the team he/she is joining.

	Once the signature is validated and the manager name is matched then it creates a new Joiner Servicenow request using REST API.
	Write the user and servicenow request details in database.

	A background process keep checking the status of new joiner request. once it is completed and it create sub request automatically to get access to all the client applications.

	Update the sub requests detail and their status in the existing record in database.
 

Below are used to create iApproval application:
-
	Python  - Development
	Django - Web Framwork
	TensorFlow - Machine Learning
	REST API - for Tecket creation in ServiceNow
	HTML & CSS(from bootstrapcdn) for Web Pages

Other information:
-
Sample request form and the application screenshots are placed in the media folder.
