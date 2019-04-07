from django.shortcuts import render

from apfelschuss.votes.models import Voting

def voting(request):
    queryset = Voting.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'votes/voting.html', context)
