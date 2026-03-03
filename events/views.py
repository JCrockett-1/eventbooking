from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Event
from .models import Registration

@login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'home', {'events': events})

def register_for_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        registration = Registration.objects.create(user = request.user, event=event)
        return redirect('confirmation', registration_id=registration.id)
    else:
        return render(request, 'registration_page.html', {'event': event})
    
def confirm_details(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'confirmation_page.html', {'registration': registration})

