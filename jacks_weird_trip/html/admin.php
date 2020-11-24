<?php
require("vendor/autoload.php");
require("creds.php");
use \Firebase\JWT\JWT;

try {
  $dec_jwt = JWT::decode($_COOKIE['AMI'], $KEY, array('HS256'));
  $priv = $dec_jwt->priv;
  if(strcmp($priv, 'admin') !== 0) {
    $return_val = "YOUR NOT ADMIN! PLEASE CHECK YOUR PRIV.";
  } else {
    $return_val = $FLAG;
  }
} catch(Exception $e) {
    $return_val = "VALIDATION ERROR. SEND VALID CREDENTIAL.";
}

?>


<!DOCTYPE html>
<html lang=ja> <head>
  <meta charset=utf-8>
  <title>Jack's Weird Trip</title>
</head>
<body>
  <video playsinline autoplay muted loop>
    <source src="img/bg.mp4" type="video/mp4">
  </video>
  <div id=maincontent>
  <h1><?php echo $return_val ?><h1>
  </div>
</body>
</html>

<style>
video{
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: -100;
  background-size: cover;
  opacity: 0.4;
}
#maincontent {
  position: relative;
  text-align:center;
  z-index: 2
  margin: auto;
}
</style>

