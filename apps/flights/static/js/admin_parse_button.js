(function($) {
    jQuery(document).ready(function($) {
        $('.parse-btn').click(function() {
            var textField = $(this).closest('.parse-check').prevAll('[name$="-text"]').first();
            var textFieldValue = textField.val();
            var resultSpan = $(this).siblings('.parse-result');

            // Perform AJAX request to check the parsing
            $.ajax({
                url: '/admin/check-parse/',  // Adjust the URL as needed
                method: 'POST',
                data: { text: textFieldValue },
                success: function(response) {
                    resultSpan.text(response.success ? 'Parse OK' : 'Parse Failed');
                },
                error: function() {
                    resultSpan.text('Error');
                }
            });
        });
    });
})(django.jQuery);
