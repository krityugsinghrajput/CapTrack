from django.urls import path
from .views import ExpenseFormSubmissionView, UpdateStatusView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ExpenseFormSubmissionView.as_view()),  # For GET and POST to submit and get forms
    path('forms/<int:pk>/update/', UpdateStatusView.as_view()),  # For updating status by pk
]

# Serve media files during development
if settings.DEBUG:  # Ensure this is only done in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
