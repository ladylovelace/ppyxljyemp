function redirectToQuery(){
    term = document.forms["form"]["query"].value;
    term = term.replace(/[^0-9]/g,"");
    if(term.length == 14)
    	window.location = window.location+"?q="+term;
}
    