from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from app.filters import LetterFilter
from app.models import Letter, Staff


def moderator_letter(request):
    letters_queryset = Letter.objects.all()
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


def moderator_client(request):
    staff_queryset = Staff.objects.all()
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


def moderator_staff(request):
    staffs_queryset = Staff.objects.all()
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


def moderator_report(request):
    reports = Staff.objects.all()
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


def moderator_branch(request):
    branches = Staff.objects.all()
    page = request.GET.get('page', 1)

    # my_filter = LetterFilter(request.GET, staff_queryest)
    # staff_queryest = my_filter.qs

    paginator = Paginator(branches, 10)
    try:
        branches = paginator.page(page)
    except PageNotAnInteger:
        branches = paginator.page(1)
    except EmptyPage:
        branches = paginator.page(paginator.num_pages)

    context = {
        'branches': branches,
        # 'my_filter': my_filter
    }
    return render(request, 'app/moderator/branch.html', context)
