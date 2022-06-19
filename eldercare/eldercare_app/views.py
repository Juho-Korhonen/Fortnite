from django.shortcuts import render
from .models import Patient,Staff_member
# Create your views here.
def display_patientpage(request,patient):
    patient = Patient.objects.filter(name=patient)
    return render(request,'websites/patient_page.html',{'patient':patient})
def display_mainpage(request):
    patients = Patient.objects.all()
    return render(request, 'websites/mainpage.html', {'patients': patients})

def display_staffpage(request):
    Staff = Staff_member.objects.all()
    return render(request, 'websites/staff_page.html', {'staff': Staff})
