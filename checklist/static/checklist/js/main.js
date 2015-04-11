$(document).ready(function() {           
    $('.checkbox-complete').click(function() {                           
            $.ajax({ 
                data: $(this).serialize(), 
                type: $(this).attr('name'), 
                url: '/check/' + $(this).attr('value') + '/' + $(this).attr('id'), 
                // /check/runid/entryid/
                success: function(response) { 
                  alert("YES");
                },
                error: function(e, x, r) { 
                  alert("NO");
                }
            }); 
        return false;

    }); 
});
