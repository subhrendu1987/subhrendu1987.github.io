<html>
<head>
<style type="text/css">
     td {width: 25%;}
	.tg  {border-collapse:collapse;border-spacing:0;border-color:#bbb;}
	.tg td{font-family:Arial, sans-serif;font-size:14px;padding:2px 20px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#594F4F;background-color:#E0FFEB;}
	.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:2px 20px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#493F3F;background-color:#9DE0AD;}
	.tg .tg-s6z2{text-align:center}
	.tg .tg-ugh9{background-color:#C2FFD6}
</style>
<style type="text/css">
	  #auth{
	  	   display:none;
       }
       
</style>
</head>
<!---------------------------------------------------------------------------------------------------------------->
<body><center>
<h1> List of Submitted Files</h1>
<hr>
<table class="tg">
<tr>
<th> Sl. </th>
<th>File Name</th>
<th> Upload Time </th>
</tr>

<?php
$dir    = 'uploads/';
$files = scandir($dir);
$n=count($files);
//foreach ($files as &$value) {
for($i=2;$i<$n;$i=$i+1){
    echo "<tr>";
    echo "<td class='tg-031e'>".($i-1)."</td>"
    	."<td class='tg-031e'>".$files[$i+0]."</td>"
    	."<td class='tg-031e'>".date ("F d Y h:i:s. A", filectime('uploads/'.$files[$i]))."</td>";
    echo "<tr>";
}
unset($files);
?>
</table>
</center></body></html>
