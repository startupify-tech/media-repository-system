# from django.shortcuts import render
# from django.contrib.auth.models import User
#
# # Create your views here.
#
# def user(request):
#     args={'user': request.user}
#     {{user}}
#     return render(request,'index.html',args)
#

# users/views.py


from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    #permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
