from django.shortcuts import render


def socket_test_view(request):
    return render(request, "chat/socket_test.html")