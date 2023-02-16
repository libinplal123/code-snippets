Step 3: Create a JavaScript file to handle the form submission using AJAX.

Create a new JavaScript file called register.js in the static directory of the registration app. This file should handle the form submission using AJAX.

javascript
Copy code
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
