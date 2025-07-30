from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import FriendshipRequest,User
from .serializers import UserSerializer,FriendshipSerializer



@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id':request.user.id,
        'name':request.user.name,
        'email':request.user.email,
    })




@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        form.save()
        return JsonResponse({
            'message': 'success',
            'errors': {}
        })
    else:
        message='error'

    return JsonResponse({
        'message': message,
        'errors': form.errors
    },status=400)
    
@api_view(['GET'])
def friends(request,pk):
    user=User.objects.get(pk=pk)
    requests=[]
    
    if user == request.user:
        requests=FriendshipRequest.objects.filter(created_for=request.user)
        requests=FriendshipSerializer(requests,many=True)
        requests=requests.data
    
    friends=user.friends.all()
    return JsonResponse({
        'user':UserSerializer(user).data,
        'friends':UserSerializer(friends,many=True).data,
        'requests':requests
    },safe=False)
    
    
@api_view(['POST'])
def send_friendship_request(request,pk):
    user=User.objects.get(pk=pk)
    friend_request=FriendshipRequest.objects.create(created_for=user,created_by=request.user)
    
    # print('send_friend_request',pk)
    return JsonResponse({'message':'Friend request send successful'})


@api_view(['POST'])
def handle_request(request,pk,status):
    user=User.objects.get(pk=pk)
    friendship_request=FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship_request.status=status
    friendship_request.save()
    
    return JsonResponse({
        'message':'friend request updated'
    })

