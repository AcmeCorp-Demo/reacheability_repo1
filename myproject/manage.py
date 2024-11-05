import os
import django
from django import forms
from django.utils.encoding import uri_to_iri

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Replace 'your_project.settings' with your settings module
django.setup()

def main():
    # Part 1: URI to IRI conversion
    uri = "https://example.com/path/%C3%A9cole"
    iri = uri_to_iri(uri)
    print("Converted IRI:", iri)  # Expected output: https://example.com/path/école

    # Part 2: Django form with multiple file uploads
    class UploadMultipleFilesForm(forms.Form):
        files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    form = UploadMultipleFilesForm()
    print("Form HTML:")
    print(form.as_p())

if __name__ == "__main__":
    main()
