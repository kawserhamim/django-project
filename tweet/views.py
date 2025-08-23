from django.shortcuts import render  # ✅ added
from django.shortcuts import redirect  # ✅ added
from django.http import HttpResponse  # ✅ added
from django.urls import reverse  # ✅ added
from django.contrib.auth.models import User  # ✅ added
from django.contrib import messages  # ✅ added
from . import forms  # ✅ added
from django.http import HttpResponseRedirect  # ✅ added
from . import models  # ✅ added
from django.shortcuts import get_object_or_404  # ✅ added
from django.contrib.auth.decorators import login_required  # ✅ added
from django.views.generic import ListView  # ✅ added
from django.views.decorators.http import require_POST  # ✅ added
from django.http import JsonResponse  # ✅ added
from django.core.paginator import Paginator  # ✅ added
from django.conf import settings  # ✅ added


def index1(request):
    return render(request, 'tweet/index1.html')  # ✅ no "templates/"

def tweet_list(request):
    tweets = models.Tweet.objects.all().order_by('-created_at')  # ✅ added
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})  # ✅ added
def tweet_create(request):
    if request.method == 'POST':
        form = forms.TweetForm(request.POST, request.FILES)  # ✅ added
        if form.is_valid():
            tweet = form.save(commit=False)  # ✅ added
            tweet.user = request.user  # ✅ added
            tweet.save()  # ✅ added
            return redirect('tweet_list')  # ✅ added
    else:
        form = forms.TweetForm()  # ✅ added
    return render(request, 'tweet/tweet_create.html', {'form': form})  # ✅ added




def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(models.Tweet, id=tweet_id, user = request.user)  # ✅ added
    if request.method == 'POST':
        form = forms.TweetForm(request.POST, request.FILES, instance=tweet)  # ✅ added
        if form.is_valid():
            tweet = form.save(commit=True)  # ✅ added
            tweet.user = request.user  # ✅ added
            tweet.save()  # ✅ added
            
            return redirect('tweet_list')  # ✅ added
    else:
        form = forms.TweetForm(instance=tweet)  # ✅ added
    return render(request, 'tweet/tweet_edit.html', {'form': form})  # ✅ added




def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(models.Tweet, id=tweet_id, user=request.user)  # ✅ added
    if request.method == 'POST':
        tweet.delete()  # ✅ added
        messages.success(request, 'Tweet deleted successfully.')  # ✅ added
        return redirect('tweet_list')  # ✅ added
    return render(request, 'tweet/tweet_delete.html', {'tweet': tweet})  # ✅ added