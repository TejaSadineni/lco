from django.shortcuts import render,redirect
from .models import Hiretubers
from django.contrib import messages

# Create your views here.

    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #tuber_id = models.IntegerField()
    #tuber_name = models.CharField(max_length=100)
    #city = models.CharField(max_length=100)
    #state = models.CharField(max_length=100)
    #phone = models.CharField(max_length=100)
    #message = models.TextField(blank=True)
    #interest = models.CharField(max_length=255)
    #user_id = models.IntegerField(blank=True)
def hiretubers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuberid']
        tuber_name = request.POST['tubername']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        interest = request.POST['interest']
        user_id = request.POST.get('user_id','Unknown')
        email = request.POST['email']

        hiretuber=Hiretubers(
            first_name=first_name,
            last_name=last_name,
            tuber_id=tuber_id,
            tuber_name=tuber_name,
            city=city,
            state=state,
            phone=phone,
            message=message,
            interest=interest,
            user_id=user_id,
            email=email
        )
        hiretuber.save()

        messages.success(request,'Thanks For Reaching Us')

        return redirect('youtubers')
    
        
