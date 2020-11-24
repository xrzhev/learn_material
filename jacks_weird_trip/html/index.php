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
    <h1>IF YOU HAVE "admin" PRIV, CLICK THIS LINK.</h1>
    <h3><a href="/admin.php">ADMIN_PAGE</a><h3>
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
  z-index: 2;
  margin: auto;
}
</style>
