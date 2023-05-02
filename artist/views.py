from django.http import JsonResponse
from .models import Work, Client, Artist
from django.contrib.auth.models import User
from .serializers import WorkSerializer, UserSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def work_list(request):
    print('All works')
    works = Work.objects.all()

    #Getting the work_type query value
    work_type = request.GET.get('work_type')
    if work_type:
        works = works.filter(work_type=work_type)
    
    #Getting the work_type query value
    artist_name = request.GET.get('artist')
    if artist_name:
        works = works.filter(artist__name__icontains=artist_name)

    serializer = WorkSerializer(works, many=True)
    return JsonResponse({"works": serializer.data}, safe=False)


@api_view(['GET', 'POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return JsonResponse({'Error': 'Please provide both username and password'})
    
    # create the user
    user = User.objects.create_user(username, password=password)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False)
