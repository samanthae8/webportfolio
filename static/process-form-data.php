<?PHP
$name = $_POST['name'];
$email = $_POST['email'];
$comment = $_POST['comment'];
$file = $_POST['file'];
$f_data = $name "," $email "," $file "," $comment "n";
$file = fopen("comments.txt", "a");
fwrite($file, $f_data);
fclose($file);
?>


