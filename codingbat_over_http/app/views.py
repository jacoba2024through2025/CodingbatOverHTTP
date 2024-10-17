from django.http.response import HttpResponse
from django.http.request import HttpRequest

def near_hundred(request: HttpRequest, n: int) -> HttpResponse:
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return HttpResponse(True) 
    else:
        return HttpResponse(False)
        
def string_splosion(request :HttpRequest, s: str) -> HttpResponse:
    result = ''.join(s[:i] for i in range(1, len(s) + 1))
    return HttpResponse({result})

def cat_dog(request :HttpRequest, catdog: str) -> HttpResponse:
    cat_count = catdog.count('cat')
    dog_count = catdog.count('dog')
    return HttpResponse(cat_count == dog_count)

def lone_sum(request :HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    test = 0
    if a != b and a != c:
        test += a
    if b != a and b != c:
        test += b
    if c != b and c != a:
        test += c
    return HttpResponse(test)

