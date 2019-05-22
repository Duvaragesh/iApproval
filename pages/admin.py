#
# Author Duvaragesh Kannan
#
from django.contrib import admin

# Register your models here.

from .models import Emp_details

class EmpAdmin(admin.ModelAdmin):
    list_display = ('Empid', 'Firstname', 'Lastname','Email','Team_Name','Request_Number','Request_Status','Sub_Request_Number','Sub_Request_Status')

admin.site.register(Emp_details, EmpAdmin)