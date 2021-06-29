from django.shortcuts import render
from .models import BlogPost
def blog_post_detail_page(request):
    obj = BlogPost.objects.get(id=1)
    template_name = 'blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)
# Create your views here.
