from django.shortcuts import render

# Create your views here.

posts=[{
        'author':'John Doe',
        'title':'Blog post 1',
        'date_posted':'Jan 5, 2023',
        'content':'First Post Content'            
    }, {
        'author':'William',
        'title':'Blog post 2',
        'date_posted':'Jan 1, 2023',
        'content':'Second Post Content'            
    }]
    
def home(request):
    context={
            'posts': posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')