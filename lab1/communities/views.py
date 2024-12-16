from django.shortcuts import render
from .models import Community

def communities_list(req):
    return render(req, 'communities/communities_list.html')



def communities_list(request):
    communities = Community.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})