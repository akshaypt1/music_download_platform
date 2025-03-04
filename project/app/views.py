from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import User  # Importing your custom User model
from .models import Music
from .forms import MusicUploadForm


# Secure Login View
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if password == user.password:  # Directly comparing passwords (Hashing to be added later)
                request.session['user_id'] = user.id  # Store user session manually
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'login.html')

# Secure Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = User(username=username, email=email, password=password)  # Store password as plain text for now
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')

    return render(request, 'signup.html')
# def home(request):
#     return render(request, 'home.html')
def home(request):
    # Set your display limits here
    LATEST_LIMIT = 6  # Show 5 latest songs
    TRENDING_LIMIT = 6  # Show 6 trending songs
    
    trending_music = Music.objects.filter(is_trending=True)[:TRENDING_LIMIT]
    latest_music = Music.objects.order_by('-upload_date')[:LATEST_LIMIT]
    
    return render(request, 'home.html', {
        'music_list': trending_music,
        'latest_music': latest_music
    })

# Upload music
def upload_music(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = MusicUploadForm()
    return render(request, 'upload.html', {'form': form})

# List and download music
def music_list(request):
    music_files = Music.objects.all()
    return render(request, 'music_list.html', {'music_files': music_files})

def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    return render(request, 'music_detail.html', {'music': music})
    

