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
                  alert("Failed" + $(evt.target).parent().attr('value'));
                  alert( $(evt.target).prop('tagName') );
                }
            }); 
        return false;

    }); 
});
