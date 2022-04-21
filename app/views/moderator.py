from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from rest_framework.decorators import permission_classes

from app.filters import LetterFilter
from app.forms import CreateClientForm, CreateStaffForm
from app.models import Letter, Staff
from app.permissions import IsModeratorMixin


@permission_classes([IsModeratorMixin])
def moderator_letter(request):
    letters_queryset = Letter.objects.order_by('-id')
    page = request.GET.get('page', 1)

    my_filter = LetterFilter(request.GET, letters_queryset)
    letters_queryset = my_filter.qs

    paginator = Paginator(letters_queryset, 10)
    try:
        letters_queryset = paginator.page(page)
    except PageNotAnInteger:
        letters_queryset = paginator.page(1)
    except EmptyPage:
        letters_queryset = paginator.page(paginator.num_pages)

    context = {
        'letters': letters_queryset,
        'my_filter': my_filter
    }

    return render(request, 'app/moderator/letter.html', context)


@permission_classes((IsModeratorMixin,))
def moderator_client(request):
    staff_queryset = Staff.objects.order_by('-id')
    page = request.GET.get('page', 1)

    # my_filter = LetterFilter(request.GET, staff_queryest)
    # staff_queryest = my_filter.qs

    paginator = Paginator(staff_queryset, 10)
    try:
        staff_queryset = paginator.page(page)
    except PageNotAnInteger:
        staff_queryset = paginator.page(1)
    except EmptyPage:
        staff_queryset = paginator.page(paginator.num_pages)

    context = {
        'clients': staff_queryset,
        # 'my_filter': my_filter
    }
    return render(request, 'app/moderator/client.html', context)


@permission_classes((IsModeratorMixin,))
def moderator_create_client(request):
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.client = request.user
            staff.save()
            return redirect('mod_client_page')
    else:
        form = CreateClientForm()
    return render(request, 'app/moderator/create-client.html', {'form': form})


@permission_classes((IsModeratorMixin,))
def moderator_staff(request):
    staffs_queryset = Staff.objects.order_by('-id')
    page = request.GET.get('page', 1)

    # my_filter = LetterFilter(request.GET, staff_queryest)
    # staff_queryest = my_filter.qs

    paginator = Paginator(staffs_queryset, 10)
    try:
        staffs_queryset = paginator.page(page)
    except PageNotAnInteger:
        staffs_queryset = paginator.page(1)
    except EmptyPage:
        staffs_queryset = paginator.page(paginator.num_pages)

    context = {
        'staffs': staffs_queryset,
        # 'my_filter': my_filter
    }
    return render(request, 'app/moderator/staff.html', context)


@permission_classes((IsModeratorMixin,))
def moderator_create_staff(request):
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.client = request.user
            staff.save()
            return redirect('mod_staff_page')
    else:
        form = CreateStaffForm()
    return render(request, 'app/moderator/create-staff.html', {'form': form})


@permission_classes((IsModeratorMixin,))
def moderator_report(request):
    reports = Staff.objects.order_by('-id')
    page = request.GET.get('page', 1)

    # my_filter = LetterFilter(request.GET, staff_queryest)
    # staff_queryest = my_filter.qs

    paginator = Paginator(reports, 10)
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)

    context = {
        'reports': reports,
        # 'my_filter': my_filter
    }
    return render(request, 'app/moderator/report.html', context)
