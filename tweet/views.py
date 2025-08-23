from django.shortcuts import render
from . import forms  # ✅ added
from django.http import HttpResponseRedirect  # ✅ added
from . import models  # ✅ added
from django.shortcuts import get_object_or_404  # ✅ added


def index1(request):
    return render(request, 'tweet/index1.html')  # ✅ no "templates/"

def tweet_list(request):
    tweets = models.Tweet.objects.all().order_by('-created_at')  # ✅ added
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})  # ✅ added
def tweet_create(request):
    if request.method == 'POST':
        form = forms.TweetForm(request.POST, request.FILES)  # ✅ added
        if form.is_valid():
            form.save()  # ✅ added
            return HttpResponseRedirect('/tweets/')  # ✅ added
    else:
        form = forms.TweetForm()  # ✅ added
    return render(request, 'tweet/tweet_create.html', {'form': form})  # ✅ added
