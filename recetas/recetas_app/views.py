
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecetaForm, UserRegistrationForm
from .models import Receta, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm

def lista_recetas(request):
    recetas = Receta.objects.all().order_by('-creado_en')
    return render(request, 'recetas_app/listar_recetas.html', {'recetas': recetas})

@login_required
def subir_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user  # Set the logged-in user as the author
            receta.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas_app/subir_recetas.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'recetas_app/register.html', {'form': form})

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)  # Fetch the specific receta by primary key
    return render(request, 'recetas_app/detalle_receta.html', {'receta': receta})

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    recetas = Receta.objects.filter(autor=request.user)
    return render(request, 'recetas_app/user_profile.html', {'profile': profile, 'recetas': recetas})

@login_required
def update_profile(request):
    profile = request.user.profile  # Access the profile of the logged-in user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the profile page after saving
    else:
        form = ProfileUpdateForm(instance=profile)  # Pre-fill the form with the current data
    return render(request, 'recetas_app/update_profile.html', {'form': form})