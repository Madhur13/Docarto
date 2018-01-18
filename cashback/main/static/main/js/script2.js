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

$('.cat_filter, .comp_filter').each(function(){

		$(this).change(function(){
			if(this.getAttribute("class")=='cat_filter')
			{
				if(this.checked)
				{
					cat_filter.push(this.getAttribute("value") );		//$(this).val()
				}
				else
				{
					index = cat_filter.indexOf(this.getAttribute("value"));
					if(index!=-1)
						cat_filter.splice(index,1);
				}
			}
			else if(this.getAttribute("class")=='comp_filter')
			{
				if(this.checked)
				{
					comp_filter.push(this.getAttribute("value") );		//$(this).val()
				}
				else
				{
					index = comp_filter.indexOf(this.getAttribute("value"));
					if(index!=-1)
						comp_filter.splice(index,1);
				}
			}
			console.log(comp_filter);
			$.ajax({
				url: '/main/offers',
				type: 'POST',
				data : {comp_filter : comp_filter, cat_filter : cat_filter },
				success : function(response){
					$('#offers_disp').html(response);
				}
			});


		});

});
