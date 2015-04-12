$(document).ready(function() {           
    $('#checkbox').click(function(evt) {                           
            $.ajax(
                '/check/' + $(this).attr('value'),
                { 
                dataType: 'json',
                // /check/runid/entryid/
                success: function(response)
                { 
                  if(!$(evt.target).is('input'))
                    evt.target = $(evt.target).children('.checkbox');
                  $(evt.target).prop('checked',response['state']);
                },
                error: function(e, x, r) { 
                  alert("Failed");
                  alert( $(this).attr('value') );
                }
            }); 
        return false;

    }); 
});
