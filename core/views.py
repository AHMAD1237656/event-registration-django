from django.shortcuts import render, redirect
from .models import Event, Registration

# Event list show karna
def event_list(request):
    events = Event.objects.all()
    return render(request, "event_list.html", {"events": events})

# Registration form handle karna
def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        # Duplicate check
        if Registration.objects.filter(event=event, email=email).exists():
            return JsonResponse({"error": "You are already registered for this event."})

        Registration.objects.create(event=event, name=name, email=email)
        return redirect("event_list")

    return render(request, "register_event.html", {"event": event})
