from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Idea,Division
from .forms import IdeaForm,FilterForm
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, idea_id):
    try:
        idea = Idea.objects.get(pk=idea_id);
    except Idea.DoesNotExist:
        return render(request, 'no_image.html')
    
    try:
        img_url = idea.image.url
    except ValueError:
        img_url = ""

    pub_date = idea.pub_date

    messages = (
        '<p>주제: {subject}</p>'.format(subject=idea.subject),
        '<p>구분: {subject}</p>'.format(subject=idea.division.division),
        '<p>수정일: {subject}</p>'.format(subject=idea.created_at),
        '<p><img src="{url}" style="max-width: 100%; height: auto;"/></p>'.format(url=img_url),
        '<p>발행일: {subject}</p>'.format(subject=pub_date),
        '<p><a href="{edit_url}">편집하기</a>'.format(edit_url=idea.get_edit_url()),
        '<p><a href="{url}">목록 보기</a>'.format(url=reverse_lazy('list')),
    )
    ctx = {
        'idea': idea,
        'img_url': img_url,
        'page_title': "아이디어 디테일",
    }
    return render(request, 'detail.html', ctx)
    #return HttpResponse('\n'.join(messages))

def new(request):

    if request.method == "GET":
        form = IdeaForm()
    elif request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj.get_absolute_url())

    ctx = {
        'form': form,
        'page_title': "새 포스팅",
    }
    return render(request, 'edit.html', ctx)

def edit(request, idea_id):
    post = get_object_or_404(Idea, pk=idea_id)
    if request.method == "GET":
        form = IdeaForm(instance=post)
    elif request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            obj = post.save()
            return redirect(post.get_absolute_url())

    ctx = {
        'form': form,
        'page_title': "포스팅 수정",
    }
    return render(request, 'edit.html', ctx)

def calendar(request, year, month):
    ctx = {
        'page_title': "야미 다이어리 캘린더",
    }
    return render(request, 'calendar.html', ctx)

def calendar_today(request):
    #retrun calendar(request, today.year, today.month)
    now = datetime.datetime.now()
    return calendar(request, now.year, now.month)
    #return HttpResponse("You're looking calendar at %d/%d." % (today.year, today.month))

def list(request):

    photos = Idea.objects.order_by('-pub_date','image', '-created_at')
    get_div = ''
    if request.method == "POST":
        get_div = format(request.POST["division"])
        get_image = format(request.POST["image"])
        get_pub = request.POST["pub"]
        if get_div is not "":
            photos = photos.filter(division = get_div)

        if get_image is "y":
            photos = photos.exclude(image__exact='')
        elif get_image is "n":
            photos = photos.filter(image__exact='')

        if get_pub is "y":
            photos = photos.exclude(pub_date__isnull=True)
        elif get_pub is "n":
            photos = photos.filter(pub_date__isnull=True)
            #photos = photos.filter(pub_date__exact='')

    #get_div = 'all'
    #get_div = format(request.GET["division"])


    ctx = {
        'page_title': "아이디어 목록",
        'photos': photos,
        'new' : reverse_lazy('new'),
        'divisions' : Division.objects.order_by('pk'),
        'gdiv' : get_div,
        'form' : FilterForm(),
    }

    return render(request, 'list.html', ctx)

def simple_upload(request):
    if request.method == 'POST':
        idea = Idea()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
