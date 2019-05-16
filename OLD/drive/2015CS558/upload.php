<html><body><center>
<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$uploadFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if file is a actual tar.gz or fake
if(isset($_POST["submit"])) {
///////////////////////////////////////////////////////////////
// Check if file already exists
	if (file_exists($target_file)) {
    echo "The file already exists. If you want to re-submit contact the TA.";
    //chmod($target_file,0755);
    //unlink($target_file);
    //echo "delete the file";
    $uploadOk = 0;
	}elseif($uploadFileType != "gz" and $uploadFileType != "tar" and $uploadFileType != "zip" and $uploadFileType != "bz2") {
		echo "Only compressed files of types tar.gz, zip can be uploaded.";
		$uploadOk = 0;
	}else{
		/*$z = gzopen($_FILES["fileToUpload"]["name"],'r');
		if (!$z){
			$zip = new ZipArchive;
			$res = $zip->open($_FILES["fileToUpload"]["name"]);
			if ($res === TRUE){
				$zip->close();
        echo "debug_zip_close";
			}else{
        echo "Not a valid compressed file";
				$uploadOk = 0;
			}
		}else{
        //echo "debug_gz_close";
			gzclose($z);
		}
   */
	}
}
// Check if $uploadOk is set to 0 by an error
//echo "debug";
if ($uploadOk == 0) {
    echo "<br><h1>Sorry, your file with size ".$_FILES["fileToUpload"]["size"]."KB was not uploaded.</h1>";
// if everything is ok, try to upload file
} else {
	if ($_FILES["fileToUpload"]['error'] === UPLOAD_ERR_OK) { 
	//uploading successfully done 
	} else { 
 		echo "<br>Error:";
    switch($_FILES["fileToUpload"]['error']){
                                             case UPLOAD_ERR_INI_SIZE:
                                                  echo "Too Big Document";
                                                  break;
                                             case UPLOAD_ERR_FORM_SIZE:
                                                  echo "Too big Document";
                                                  break;
                                             case UPLOAD_ERR_PARTIAL:
                                                  echo "Partial Upload. Try again.";
                                                  break;
                                             case UPLOAD_ERR_NO_FILE:
                                                  echo "No file was uploaded.";
                                                  break;
                                             case UPLOAD_ERR_NO_TMP_DIR:
                                                  echo "Missing a temporary folder.";
                                                  break;
                                             case UPLOAD_ERR_CANT_WRITE:
                                                  echo "Failed to write file to disk.";
                                                  break;
                                             case UPLOAD_ERR_EXTENSION:
                                                  echo "Extension error";
                                                  break;
                                             default:
                                                     echo "Unrecognized. Please contact TA.";
                                                     break;
    }
	} 
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "<br>The file <b style='color:#009933'>". basename( $_FILES["fileToUpload"]["name"]). "</b> has been uploaded.";
		    shell_exec('python submitted.py');
    } else {
        echo "<br> <h1>Sorry, Operation not permited.</h1>";
    }
}

?>
<br><a href="FileList.php">List of already submitted files.</a>
</center>

</body></html>
