<html>
<head>
<style type="text/css">
	.tg  {border-collapse:collapse;border-spacing:0;border-color:#bbb;}
	.tg td{font-family:Arial, sans-serif;font-size:14px;padding:2px 20px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#594F4F;background-color:#E0FFEB;}
	.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:2px 20px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#493F3F;background-color:#9DE0AD;}
	.tg .tg-s6z2{text-align:center}
	.tg .tg-ugh9{background-color:#C2FFD6}
</style>
</head>
<!---------------------------------------------------------------------------------------------------------------->
<body><center>
<div id="auth">		    
Please Enter Your Password
<form method="post" action="FileDownload.php">
<input type="password" name="password" />
<input type="submit" name="submit" />
</form>
<hr>
</div>
<!---------------------------------------------------------------------------------------------------------------->
<?php if($error_message){ echo $error_message; } ?>
<!---------------------------------------------------------------------------------------------------------------->
<?php
$generated_password = "whatever";
if(isset($_POST['submit'])){

$password = $_POST['password'];
//Password Check
if($password == $generated_password){
?>
<style type="text/css">
	  #auth{
	  	   display:none;
       }
       td {
    	  	width: 25%;
       }
</style>
<h1> List of Submitted Files</h1>
<hr>
<table border="1">
<tr><td> First Deadline </td><td> <b>27/01/15</b> </td><td> Second Deadline </td><td> <b>29/01/15</b> </td></b></tr>
</table>

<table class="tg">
<col style="width:5%">
<col style="width:35%">
<col style="width:35%">
<thead><tr>
<td class="tg-s6z2"> </td><th class="tg-s6z2" colspan="3">File Repo</th>
</tr>
</thead><tr>
	<td class='tg-ugh9'> <b>Sl.</b></td> <td class='tg-031e'><b> FileName </b></td> <td class='tg-ugh9'> <b>Submitted At </b></td>
</tr>
<!---------------------------------------------------------------------------------------------------------------->
<?php
             $dir    = 'uploads/';
             $files = scandir($dir);
		   $n=count($files);
		   for($i=2;$i<$n;$i=$i+1){
			  echo "<tr>";
					echo "<td class='tg-031e'>".($i-1)."</td>"
						."<td class='tg-ugh9'><a href='uploads/".$files[$i]."'>".$files[$i]."</a> </td>"
						."<td class='tg-031e'>".date ("F d Y h:i:s. A", filemtime('uploads/'.$files[$i]))."</td>";
			  echo "</tr>";
		   }
		   unset($files);
}
else{
             echo "<tr><td colspan='4'><h2 style='color:#FF0000'>Not Authorized</h2></td></tr>";
}

}

?>
<!----------------------------------------------------------------------------------------------------------------> 
</table>
</center></body></html>
