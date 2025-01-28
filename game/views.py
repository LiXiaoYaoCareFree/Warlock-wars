from django.http import HttpResponse

def index(resquest):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://tse2-mm.cn.bing.net/th/id/OIP-C.Y-i9FNrjN1VkUa3fEwX9EwHaE9?w=231&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7" width=1000>'
    return HttpResponse(line1 + line2)




# Create your views here.
