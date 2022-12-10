from django.shortcuts import render, redirect
from main.forms import DirectForm, GroupForm
from main.models import DirectMessage, GroupMessage, MessageStatus

# Create your views here.
def homepage(request):
    direct_messages = DirectMessage.objects.all
    group_messages = GroupMessage.objects.all
    if request.method == "POST" and 'direct' in request.POST:
        dform = DirectForm(request.POST)
        print(dform.errors)
        if dform.is_valid():
            dform.save()
            return redirect("home")
        
    if request.method == "POST" and 'group' in request.POST:
        gform = GroupForm(request.POST)
        print(gform.errors)
        if gform.is_valid():
            gform.save()
            return redirect("home")
    else:
        dform = DirectForm
        gform = GroupForm

    context = {
        "direct_message": direct_messages,
        "group_message": group_messages,
        "dform": dform,
        "gform": gform,
    }
    return render(request, "home.html", context)


def direct(request):
    if request.method == "POST":
        form = DirectForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("direct")
        
    else:
        form = DirectForm

    context = {
        "form": form,
    }
    return render(request, "direct.html", context)


def group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = GroupForm

    context = {"form": form}
    return render(request, "group.html", context)
