<html><body><center>

<?php
$dir    = 'uploads/';
$files = scandir($dir);
$n=count($files);
//foreach ($files as &$value) {
for($i=2;$i<$n;$i=$i+1){
    $user_name = "cs558";
    $path='uploads/'.$files[$i];
    //$ret=chown($path,$user_name);
    $ret=chmod($path,0755);
    //$stat = stat($path);
    //print_r(posix_getpwuid($stat['uid']));
    echo " ".$ret." - ".$files[$i+0]."<br>";
}
unset($files);
?>
<h1>404. Custom File Not Found</h1>
</center>

</body></html>
