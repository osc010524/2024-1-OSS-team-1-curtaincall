from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import File
from django.shortcuts import render, get_object_or_404
import CurtainCallApp.cookies as ck


# Create your views here.
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response("Swagger 연동 테스트")


# File Upload View
class FileUploadView(APIView):
    permission_classes = [permissions.AllowAny]  # 모든 사용자가 접근 가능

    def post(self, request):  # request 객체를 통해 파일을 받아옴
        file = request.data.get('file')  # request 객체에서 파일을 가져옴
        File.objects.create(file=file)  # 파일을 DB에 저장
        # 등록에 성공했으면 CurtainCallApp/로 이동하여 등록된 URL을 확인하
        herf = '/CurtainCallApp/'
        return redirect(herf)


def index(request):
    file_list = File.objects.order_by('-file')
    context = {'file_list': file_list}
    return render(request, 'file_list.html', context)


def detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    context = {'file': file}
    return render(request, 'file_detail.html', {'file': file})


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')


class CookieView(APIView):
    permission_classes = [permissions.AllowAny]  # 모든 사용자가 접근 가능

    def post(self, request):
        href = '/CurtainCallApp/main/'
        response = redirect(href)
        response = ck.set_guest_id(request, response)
        guest_id = ck.get_guest_id(request)
        print(guest_id)
        return response
