from django.views import generic


class HomeView(generic.TemplateView):
    """
    Class for the main site view.

    Members:
        none
    """
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        """
        Function to get the data for the get request.

        Parameters:
            kwargs - the extra arguments.

        Returns:
            the requested data.
        """
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        """
        Function for the get request.

        Parameters:
            request - the request.
            args    - non keyword extra arguments.
            kwargs  - keyword extra arguments.

        Returns:
            the page.
        """
        return super().get(request, args, kwargs)
