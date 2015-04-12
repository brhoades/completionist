$(document).ready(function() {           
    $('.checkbox').click(function(evt) {                           
            $.ajax(
                '/check/' + $(evt.target).parent().attr('value'),
                { 
                dataType: 'json',
                // /check/runid/entryid/
                success: function(response) { 
                  $(evt.target).prop('checked',response['state']);
                },
                error: function(e, x, r) { 
                  alert("Failed");
                  alert( $(evt.target).parent().attr('value') );
                }
            }); 
        return false;

    }); 
});
