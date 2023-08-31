from django.http import HttpResponse, JsonResponse
from .models import Post

def hello_world(request):
        html_form = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Form</title>
        </head>
        <body>
            <h1>Contact Us</h1>
            <p>Please fill out the form below to get in touch with us.</p>
            
            <form action="/submit" method="post">
                <!-- Name Field -->
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <!-- Email Field -->
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <!-- Message Field -->
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
                
                <!-- Submit Button -->
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
        """
        return HttpResponse(html_form)

def json(request):
    posts = Post.objects.all()
    content = [{"content": post.content, "title": post.title} for post in posts]
    context = {
        "resource":content
    }
    return JsonResponse(context)
    