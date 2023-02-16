Create a JavaScript file to handle the form submission using AJAX.

Create a new JavaScript file called register.js in the static directory of the registration app. This file should handle the form submission using AJAX.

$(document).ready(function() {
  $('#register-form').on('submit', function(event) {
    event.preventDefault();
    $.ajax({
      url: '/register/',
      type: 'POST',
      data: $(this).serialize(),
      success: function(response) {
        if (response.success) {
          window.location.href = '/';
        }
      }
    });
  });
});
$(document).ready(function() {
  $('#register-form').on('submit', function(event) {
    event.preventDefault();
    $.ajax({
      url: '/register/',
      type: 'POST',
      data: $(this).serialize(),
      success: function(response) {
        if (response.success) {
          window.location.href = '/';
        }
      }
    });
  });
});
Step 4: Add the JavaScript file to the template and include it in the HTML.

Add the following line to the register.html template to include the register.js file:

php
Copy code
{% block extra_js %}
  <script src="{% static 'registration/register.js' %}"></script>
{% endblock %}
