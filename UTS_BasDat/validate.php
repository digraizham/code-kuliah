<?php
if (isset($_POST['g-recaptcha-response'])) {
    
    $secreatkey = "6LcyP2UjAAAAAJZDcrX90I-IIe-rBwP39-nr2eXo";
    $ip = $_SERVER['REMOTE_ADDR'];
    $response = $_POST['g-recaptcha-response'];
    $url = "https://www.google.com/recaptcha/api/siteverify?secret=$secreatkey&response=$response&remoteip=$ip";
    $fire = file_get_contents($url);
    $data = json_decode($fire);

    if($data->success==true){
        echo "success";
    }
    else{
        echo "please Fill recaptcha";
    }
}
else {
    echo "Whats wrong with you?";
}
?>
