$(document).ready(function() {           
    $('.checkbox').change(function(evt) {                           
            $.ajax(
                '/check/' + $(evt.target).parent().attr('value'),
                { 
                dataType: 'json',
                // /check/runid/entryid/
                success: function(response)
                { 
                  $(evt.target).prop('checked',response['state']);
                },
                error: function(e, x, r) { 
                  alert("Error, you are not logged in.");
                  $(evt.target).prop('checked',!$(evt.target).prop('checked'));
                }
            }); 
        return false;

    }); 
});
