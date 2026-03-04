from django.shortcuts import render
from django.shortcuts import redirect
from .models import Event
from .models import Registration

# This renders the event_list page. It gets all of the events already published and sends that info the the html
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

# This allows a user to register for an event, if the register button is pressed, as long as a name and email are provided for a specific event, a registration object is created. It will also redirect to the confirmation page
def register_for_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        registration = Registration.objects.create(name=name, email=email, event=event)
        return redirect('confirmation', registration_id=registration.id)
    else:
        return render(request, 'registration_page.html', {'event': event})
    
# This renders the confirmatino page, it is simply given the registration id which has all of the details for the event registered for and the user going, it also includes a redirect back to the event list
def confirm_details(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    if request.method == "POST":
        return redirect('home')
    else:
        return render(request, 'confirmation_page.html', {'registration': registration})

