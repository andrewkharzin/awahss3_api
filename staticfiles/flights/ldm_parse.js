(function($) {
    $(document).ready(function() {
      $('.parse-button').on('click', function() {
        var prefix = $(this).data('formset-prefix');
        var parseButton = $('#' + prefix + '-parse_button');
        var parseStatus = $('#' + prefix + '-parse_status');
        var ldmText = $('#' + prefix + '-text').val();
        
        // Implement your parsing logic here
        var parsedData = parse_ldm_text(ldmText);
  
        if (parsedData) {
          parseStatus.text('Parsing successful.');
          parseStatus.addClass('parse-success');
          parseButton.val('1');  // Set the parse_button field to '1'
          parseStatus.val('Success');  // Set the parse_status field
        } else {
          parseStatus.text('Parsing failed.');
          parseStatus.addClass('parse-error');
          parseButton.val('0');  // Set the parse_button field to '0'
          parseStatus.val('Error');  // Set the parse_status field
        }
      });
    });
  })(django.jQuery);
  