# events/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm



@login_required
def evento_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def evento_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def evento_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})

def evento_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('evento_list')
    return render(request, 'delete_event.html', {'event': event})