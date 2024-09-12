from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Comment
import threading

def create_comment(request):
    print(f"Thread ID (caller): {threading.get_ident()}")

    # Create a new comment instance and save it
    c = Comment(name="Test Comment", comment="This is a test.", status="pending")
    c.save()

    return render(request, 'template.html')
