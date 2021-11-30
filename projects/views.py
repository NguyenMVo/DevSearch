from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Project, Tag
from .forms import ProductForm, ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects
from .testmodel import test


def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)

def products(request):
    # projects, search_query = searchProjects(request)
    product = Product.objects.all()
    custom_range, projects = paginateProjects(request, product, 1000)

    context = {'projects': projects,
               'search_query': '', 'custom_range': ''}
    return render(request, 'projects/products.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)
    a = False
    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form, 'ketqua':a})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'project': project}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)

list_class = {15:'QuanAo',17:'TuiVi',2:'Camera',10:'MayGiat',21:'XeTai',19:'XeDapDien',16:'TuLanh',0:'Amply',4:'DienThoai',13:'NuocHoa',6:'GiayDep',11:'MayLanh',12:'MayTinhBang',18:'XeDap',7:'GiuongNem',14:'Oto',20:'XeMay',5:'DongHo',9:'Laptop',3:'CayCanh',1:'BanGhe',8:'KeTu'}


def createProduct(request):
    form = ProductForm()
    a=False
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            # product.save()
            kq = test(product.featured_image)
            print(kq)
            print(product.category)
            
            if str(kq)==str(product.category):
                print('---------------dung-------------')
                product.is_published = True
                product.category = list_class[int(product.category)]
                product.save()
                return redirect('projects')
            else:
                a = True
                print(a)


    context = {'form': form, 'ketqua':a}
    return render(request, "projects/project_form.html", context)