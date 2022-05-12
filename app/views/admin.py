from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import permission_classes

from app.filters import LetterFilter
from app.forms import CreateBranchForm, CreateStaffForm, CreateClientForm
from app.models import Letter, Staff
from app.permissions import IsAdminMixin
from core.settings import CLIENTS


def admin_letter(request):
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

    return render(request, 'app/admin/letter.html', context)


def admin_letter_cert(request):
    letters_queryset = Letter.objects.filter(client__username=CLIENTS['certificate']).order_by('-id')
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

    return render(request, 'app/admin/cerf-letter.html', context)


def _merge_pdf():
    import fitz

    result = fitz.open()
    list_pdfs = list(filter(lambda x: x,
                            Letter.objects.filter(client__username=CLIENTS['certificate']).values_list('file',
                                                                                                       flat=True)))
    for pdf in list_pdfs:
        with fitz.open(f'media/{pdf}') as mfile:
            result.insert_pdf(mfile)

    result.save('test.pdf')
    return result


def admin_letter_generate_link(request):
    # pdf = open('app/tmp/cerf/000000000001.pdf')
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'inline;filename=some_file.pdf'
    # return response
    response_file = _merge_pdf()
    return FileResponse(response_file, content_type='application/pdf')
    # return FileResponse(open('test.pdf', 'rb'), content_type='application/pdf')


def admin_letter_population(request):
    letters_queryset = Letter.objects.filter(client__username=CLIENTS['population']).order_by('-id')
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

    return render(request, 'app/admin/common-letter.html', context)


def admin_letter_juridik(request):
    letters_queryset = Letter.objects.filter(client__username=CLIENTS['juridik']).order_by('-id')
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

    return render(request, 'app/admin/juridik-letter.html', context)


@permission_classes((IsAdminMixin,))
def admin_client(request):
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
    return render(request, 'app/admin/client.html', context)


@permission_classes((IsAdminMixin,))
def admin_create_client(request):
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.client = request.user
            staff.save()
            return redirect('admin_staff_page')
    else:
        form = CreateClientForm()
    return render(request, 'app/admin/create-client.html', {'form': form})


@permission_classes((IsAdminMixin,))
def admin_staff(request):
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
    return render(request, 'app/admin/staff.html', context)


@permission_classes((IsAdminMixin,))
def admin_create_staff(request):
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.client = request.user
            staff.save()
            return redirect('admin_staff_page')
    else:
        form = CreateStaffForm()
    return render(request, 'app/admin/create-staff.html', {'form': form})


@permission_classes((IsAdminMixin,))
def admin_report(request):
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
    return render(request, 'app/admin/report.html', context)


@permission_classes((IsAdminMixin,))
def admin_branch(request):
    branches = Staff.objects.order_by('-id')
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
    return render(request, 'app/admin/branch.html', context)


@permission_classes((IsAdminMixin,))
def admin_create_branch(request):
    if request.method == 'POST':
        form = CreateBranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.client = request.user
            branch.role = Staff.CLIENT
            branch.password = make_password(form.cleaned_data['password'])
            branch.save()
            return redirect('admin_branch_page')
    else:
        form = CreateBranchForm()
    return render(request, 'app/admin/create-branch.html', {'form': form})
