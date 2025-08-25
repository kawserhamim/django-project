from django.shortcuts import render , get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
def index1(request):
    return render(request, 'tweet/index1.html')
@login_required
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

@login_required
def tweet_personal_list(request):
    tweets = Tweet.objects.filter(user = request.user).order_by('-created_at')
    return render(request, 'tweet/tweet_personal_tweet.html', {'tweets': tweets})

def alert(request):
    return render(request, 'tweet/alert.html')

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # Associate the tweet with the logged-in user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form': form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet_form.html', {'form': form})

from django.http import HttpResponseForbidden

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    # tweet.delete()
    return HttpResponseForbidden("You are not allowed to delete this tweet.")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            messages.success(request, "Account created successfully!")
            return redirect('tweet_list')
    else:
        form = SignUpForm()
    return render(request, "tweet/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back {username}!")
                return redirect('tweet_list')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "tweet/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out successfully.")
    return redirect("/login/")