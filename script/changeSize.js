function autoResize(id) {
	var H=document.getElementById(id).contentDocument.documentElement.scrollHeight+15;
	alert("H="+H);
    document.getElementById(id).height = document.getElementById(id).contentDocument.documentElement.scrollHeight+15; //Chrome

    document.getElementById(id).height = document.getElementById(id).contentWindow.document.body.scrollHeight+15; //FF, IE
}
