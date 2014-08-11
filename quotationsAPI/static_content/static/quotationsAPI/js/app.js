$( document ).ready(function() {
	$.get( "http://127.0.0.1:8000/quotations/", function( data ) {
	  results = data['results'];
	  for (var i=0; i<results.length; i++) {
		  $( ".container" ).html( results[i]['text'] );	  	
	  }
	});
});