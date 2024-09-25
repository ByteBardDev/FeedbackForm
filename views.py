from django.shortcuts import render

# Create your views here.

from .forms import FeedbackForm

def feedback_view(request):
    form = FeedbackForm()
    message = ""
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Display the thank-you message
            message = "Thank you for your feedback!"
            form = FeedbackForm()  # Clear the form after submission
    
    return render(request, 'feedback/feedback.html', {'form': form, 'message': message})
