<?php
require("vendor/autoload.php");
require("creds.php");
use \Firebase\JWT\JWT;

try {
  $dec_jwt = JWT::decode($_COOKIE['AMI'], $KEY, array('HS256'));
  $priv = $dec_jwt->priv;
  if(strcmp($priv, 'admin') !== 0) {
    echo "YOUR NOT ADMIN! PLEASE CHECK YOUR PRIV.<br>";
  } else {
  echo $FLAG;
  }
} catch(Exception $e) {
  echo "VALIDATION ERROR. SEND VALID CREDENTIAL.<br>";
}

?>

