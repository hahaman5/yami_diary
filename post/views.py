from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Idea,Division
from .forms import IdeaForm
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, idea_id):
    try:
        idea = Idea.objects.get(pk=idea_id);
    except Idea.DoesNotExist:
        return HttpResponse("사진이 없습니다.")
    
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
    return HttpResponse('\n'.join(messages))

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
    }
    return render(request, 'edit.html', ctx)

def calendar(request, cdate):
    return HttpResponse("You're voting on idea %s." % date)

def list(request):

    get_div = ''
    if request.method == "POST":
        get_div = format(request.POST["division"])
        get_image = request.POST["image"]
        get_pub = request.POST["pub"]
        photos = photos.filter(division = get_div)

    photos = Idea.objects.order_by('-created_at')
    #get_div = 'all'
    #get_div = format(request.GET["division"])


    ctx = {
        'photos': photos,
        'new' : reverse_lazy('new'),
        'divisions' : Division.objects.order_by('pk'),
        'gdiv' : get_div,
    }

    return render(request, 'list.html', ctx)
