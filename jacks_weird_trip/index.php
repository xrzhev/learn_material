<?php
require("vendor/autoload.php");
require("creds.php");
use \Firebase\JWT\JWT;

$payload = array(
  'priv' => 'normy'
);

$jwt = JWT::encode($payload, $KEY);
setcookie("AMI", $jwt);
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
    <a>IF YOU HAVE "admin" PRIV, CLICK THIS LINK.</a><br>
    <a href="/admin.php">ADMIN_PAGE</a>
  </div>
</body>
</html>
