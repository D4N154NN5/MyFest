from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Shift, ShiftAssignment


@login_required
def event_list(request):
    events = Event.objects.filter(is_active=True)
    return render(request, "events/event_list.html", {"events": events})


@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    shifts = event.shifts.prefetch_related("assignments")
    return render(request, "events/event_detail.html", {"event": event, "shifts": shifts})


@login_required
def shift_signup(request, pk):
    shift = get_object_or_404(Shift, pk=pk)

    if ShiftAssignment.objects.filter(shift=shift, user=request.user).exists():
        messages.warning(request, "Du bist bereits für diese Schicht angemeldet.")
        return redirect("event_detail", pk=shift.event.pk)

    if shift.is_full():
        status = ShiftAssignment.Status.WAITLIST
        messages.info(request, "Schicht voll – du wurdest auf die Warteliste gesetzt.")
    else:
        status = ShiftAssignment.Status.CONFIRMED
        messages.success(request, "Erfolgreich für die Schicht angemeldet!")

    ShiftAssignment.objects.create(shift=shift, user=request.user, status=status)
    return redirect("event_detail", pk=shift.event.pk)


@login_required
def shift_cancel(request, pk):
    assignment = get_object_or_404(ShiftAssignment, shift__pk=pk, user=request.user)
    shift = assignment.shift
    assignment.delete()
    messages.info(request, "Anmeldung storniert.")

    # Warteliste aufrücken
    next_in_line = ShiftAssignment.objects.filter(
        shift=shift, status=ShiftAssignment.Status.WAITLIST
    ).order_by("registered_at").first()

    if next_in_line and not shift.is_full():
        next_in_line.status = ShiftAssignment.Status.CONFIRMED
        next_in_line.save()
        messages.success(request, f"{next_in_line.user.get_full_name()} von der Warteliste bestätigt.")

    return redirect("event_detail", pk=shift.event.pk)
