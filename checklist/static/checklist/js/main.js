$(document).ready(function() {           
    $('#checkbox').click(function(evt) {                           
            $.ajax(
                '/check/' + $(evt.target).attr('value'),
                { 
                dataType: 'json',
                // /check/runid/entryid/
                success: function(response) { 
                  $(evt.target).children('.checkbox').prop('checked',response['state']);
                },
                error: function(e, x, r) { 
                  alert("Failed");
                  alert( $(evt.target).attr('value') );
                }
            }); 
      $('.checkbox').unbind();
        return false;

    }); 
});
