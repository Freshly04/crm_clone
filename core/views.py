from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from . models import Record
from . forms import AddRecordForm, UpdateRecordForm


def home(request):
    context = {}
    return render(request, "core/home.html", context)


@login_required
def dashboard(request):
    user_records = Record.objects.filter(created_by=request.user)

    context = {"user_records": user_records}
    return render(request, "core/dashboard.html", context)


@login_required
def add_record(request):
    form = AddRecordForm()

    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()
            return redirect("core:dashboard")

    context = {
        "form": form,
        "title": "Add Record",
    }
    return render(request, "core/record_form.html", context)


@login_required
def record_detail(request, pk):
    # record = get_object_or_404(Record, pk=pk)
    record = Record.objects.get(pk=pk, created_by=request.user)

    context = {"record": record}
    return render(request, "core/record_detail.html", context)


@login_required
def update_record(request, pk):
    record = Record.objects.get(pk=pk, created_by=request.user)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("core:dashboard")

    context = {
        "form": form,
        "title": "Update Record",
    }
    return render(request, "core/record_form.html", context)



@login_required
def delete_record(request, pk):
    record = Record.objects.get(pk=pk, created_by=request.user)

    if request.method == "POST":
        record.delete()
        return redirect("core:dashboard")

    context = {"record": record}
    return render(request, "core/delete_record.html", context)




