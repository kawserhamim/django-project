from django.shortcuts import render , get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

def index1(request):
    return render(request, 'tweet/index1.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form': form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user =request.user)
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
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    # tweet.delete()
    return HttpResponseForbidden("You are not allowed to delete this tweet.")