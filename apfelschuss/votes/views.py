from django.shortcuts import render

from apfelschuss.votes.models import Voting

def voting(request):
    featured = Voting.objects.filter(featured=True)
    context = {
        'object_list': featured
    }
    return render(request, 'votes/voting.html', context)

def archive(request):
    return render(request, 'votes/archive.html', {})
