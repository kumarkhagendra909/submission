from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Comment
import threading




# views.py
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
    else:
        form = CommentForm()

    return render(request, 'add_comments.html', {'form': form})

def comments_list(request):
    comments = Comment.objects.all()
    threadId = threading.get_ident()
    
    return render(request, 'index.html', {'comments': comments, 'threadId': threadId})


# def create_comment(request):
#     print(f"Thread ID (caller): {threading.get_ident()}")

#     # Create a new comment instance and save it
#     c = Comment(name="Test Comment", comment="This is a test.", status="pending")
#     c.save()

#     return render(request, 'template.html')
