function redirectToQuery(){
    term = document.forms["form"]["query"].value;
    term = term.replace(/[^0-9]/g,"");
    alert(term);
    window.location = window.location+"?q="+term;
}

function showResults()
{
    alert("55");
}
    