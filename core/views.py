from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from twilio.rest import Client




def sendmessage(request):
    if request.method == "POST":
        account_sid = 'ACdef44b8d49fb2a9d322b662fc85d7073' 
        auth_token = 'e83bac0c988edbc29a6ac340d8bf7cb0' 
        
        try:
            client = Client(account_sid, auth_token)
            
            c = request.POST['catagory_name']
            message_data = request.POST['message']
            
            catagory = Categories.objects.filter(catagory_name=c).first()
            query2 = Persons.objects.filter(catagory=catagory)
                
            for person in query2:
                message = client.messages.create(
                                        from_= 'whatsapp:+14155238886',
                                        body=message_data,
                                        to= f'whatsapp:{person.person_whatsapp_no}'
                                    )
            messages.info(request, "All messages sent successfully...")
        except Exception as E:
            print(str(E))
            messages.info(request, "Something Went Wrong! Please Try again!!!")

    query = Categories.objects.all()
    context = {
        'categories': query
    }
    
    return render(request, 'base.html', context)
    