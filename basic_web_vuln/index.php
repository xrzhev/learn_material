<!DOCTYPE html>
<html lang=ja>
<head>
  <meta charset=utf-8>
  <title>ストライクウィッチーズ応援サイト</title>
</head>
<body>
  <video playsinline autoplay muted loop>
    <source src="img/bg.mp4" type="video/mp4">
  </video>
  <div id=maincontent>
    <a>このサイトはストライクウィッチーズを心から応援する会の会員サイトです</a><br>
    <form action="/" method="post">
      <input type="text" name="username" placeholder="Username"><br>
      <input type="password" name="password" placeholder="Password"><br>
      <input type="submit" value="Login">
    </form>
  </div>
<!--
 For Maintainers
 Need Sauce? Here. /construction/index.php.dev
-->
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
	z-index: 2;
	margin: auto;
}
</style>

<?php
if($_SERVER["REQUEST_METHOD"] === "POST") {
  session_start();
  $db = new SQLite3("./creds.sqlite3");
  $result = $db->query("SELECT * FROM users");

  if(isset($_POST["username"]) && isset($_POST["password"])) {
    $username = $_POST["username"];
    $password = $_POST["password"];
  } else {
    $username = "";
    $password = "";
  }

  if(preg_match("/^'.*/", $username) or preg_match("/^'.*/", $password)) {
   echo "<h1>不正アクセスは管理者に報告されます<h1>";
  }

  //
  // superSecure!
  //
  $sql = "SELECT password FROM users WHERE username = :username";
  $stmt = $db -> prepare($sql);
  $stmt -> bindParam(":username", $username);
  $ret = $stmt -> execute();
  while($row = $ret -> fetchArray(SQLITE3_ASSOC)) {
    $db_hashed_password = $row["password"];
  }
  if(password_verify($password, $db_hashed_password)) {
    $fp = fopen("./hitokoto.txt", "r");
    while ($line = fgets($fp)) {
      echo "$line<br>";
    }
    fclose($fp);
  }
}
?>

