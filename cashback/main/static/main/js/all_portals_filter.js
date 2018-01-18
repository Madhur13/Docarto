$(document).ready(function(){

	$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});
});

$('.cat_filter_allPortals').each(function(){
		
		$(this).change(function(){
				console.log("sdddddd");
				if(this.checked)
				{
					all_portals_filter.push(this.getAttribute("value") );		//$(this).val()
				}
				else
				{
					index = all_portals_filter.indexOf(this.getAttribute("value"));
					if(index!=-1)
						all_portals_filter.splice(index,1);
				}
				console.log(all_portals_filter);
        $.ajax({
  				url: '/main/getPortalsByCategory',
  				type: 'POST',
  				data : {all_portals_filter : all_portals_filter},
  				success : function(response){
  					$('#allPortals').html(response);
  				}
  			});

			});



		});
