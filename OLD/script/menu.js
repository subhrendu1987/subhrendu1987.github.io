function displayVisible(a){
//	alert("Visible:"+a);
	if(a=="pub_menu"){
		document.getElementById("pub_submenu").style="display:display";
	}
	
}
function displayNone(a){
//	alert("None:"+a);
	if(a=="pub_menu"){
		document.getElementById("pub_submenu").style="display:none";
	}
}

function buttonClick(a){
 //alert(a);
 document.getElementById("mainframe").src=a;
}

function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
//    document.getElementById("mainframe").className=;
  }
