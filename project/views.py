from django.shortcuts import render


def index(request):
    """
    pybo 목록 출력
    """
    return render(request, 'main.html')