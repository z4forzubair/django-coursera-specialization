from django.http import HttpResponse


# Create your views here.

def index(request):
    views_count = request.session.get('views_count', 0) + 1
    request.session['views_count'] = views_count
    if views_count > 4: del request.session['views_count']
    html = HttpResponse(f"view count={views_count}")
    html.set_cookie('dj4e_cookie', 'f1cdeb87', max_age=1000)
    return html
