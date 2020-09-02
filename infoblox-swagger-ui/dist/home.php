<html>
<head><title>Swagger Documentation</title>
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.info{
  width:60%;
  padding: 30px;


}

.top-container {
  background-color: #f1f1f1;
  padding: 30px;
  text-align: center;
}

.header {
  padding: 10px 16px;
  background: #333;
  color: #f1f1f1;
}
.content {
  padding: 16px;
}

.sticky {
  position: fixed;
  top: 0;
  width: 97.4%;
}

.sticky + .content {
  padding-top: 102px;
}
select {
  width: 30%;
  padding: 5px 15px;
  border: none;
  border-radius: 4px;
  background-color: #5C9F3A;
  color: #f1f1f1;

}
select:hover {
background-color:#f1c1a1;
color:#000000;
}

input[type=submit] {
  background-color: #4C50AF;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
input[type=submit]:hover {
  background-color: #50AF4C;
}


fieldset {
  padding: 1em;
  font:80%/1 sans-serif;
  width: 40%;
  }

.information{
  padding: 1em;
  font:80%/1 sans-serif;
  width: 100%;
  height: auto;

}
label {
  float:left;
  width:45%;
  margin-right:0.5em;
  padding-top:0.2em;
  text-align:right;
  font-weight:bold;
  }
a:link, a:visited {
  background-color: #4c50AF;
  color: white;
  padding: 12px 20px;
  border-radius: 4px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: #50AF4C;
}

label{
 font-size: 14px;
}
</style>



</head>
<body>


<div class="header" id="myHeader">
  <center><img style="float:left;height:45px;width:130px;" src="data:image/png;base64,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" alt="vsethia@infoblox.com"/>
   <h2>WAPI Swagger Documentation</h2></center>
</div>
<center><br/><br/><div>
<?php
if($_POST["host"] && $_POST["username"] && $_POST["password"] && $_POST["version"] ){
?>
<fieldset>
<h3>Welcome!! <br/>

<br/><br/>
Please wait while we generate the Swagger documentation!!<br/><br/>
<?php
$message = shell_exec("./script.sh ".$_POST["version"]." ".$_POST["host"]);
?>
<br/><hr/><br/>
Please click here to view the definition<br/><br/>
</h3><a href="index.html">Click here</a>
</fieldset>
<?php }
elseif($_POST["host"] && $_POST["username"] && $_POST["password"]){
?>

<?php

$curl = curl_init();

$login = $_POST["username"];
$password = $_POST["password"];

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://".$_POST["host"]."/wapi/v1.0/?_schema",
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_USERPWD => $login.":".$password,
  CURLOPT_SSL_VERIFYHOST => false
));

$response = curl_exec($curl);
#echo "response is being generated";
curl_close($curl);
$result = json_decode($response, true);
$supported = $result["supported_versions"];
$calc = array_count_values($supported);
if($calc["2.11"] == 1){
?>
<fieldset>
    <form  action="home.php" method="post">
            <label>Enter the Grid master IP / FQDN: </label>
            <input type="text" name="host" value=<?php echo $_POST["host"] ?> readonly><br/><br/>
            <label>Enter the Grid master username: </label>
            <input type="text" name="username" value=<?php echo $_POST["username"] ?> readonly><br/><br/>
            <label>Enter the Grid master password: </label>
            <input type="password" name="password" value=<?php echo $_POST["password"] ?> readonly><br/><br/>
            <label>Select the WAPI version: </label>
            <select name="version">
              <option value="v2.8">v2.8</option>
              <option value="v2.9">v2.9</option>
              <option value="v2.10">v2.10</option>
              <option value="v2.11" selected>v2.11</option>
            </select>
            <br/><br/><input type="submit" name="Submit">
        </form>
</fieldset>

<?php
}
elseif($calc["2.9"] == 1){
?>
<fieldset>
    <form  action="home.php" method="post">
            <label>Enter the Grid master IP / FQDN: </label>
            <input type="text" name="host" value=<?php echo $_POST["host"] ?> readonly><br/><br/>
            <label>Enter the Grid master username: </label>
            <input type="text" name="username" value=<?php echo $_POST["username"] ?> readonly><br/><br/>
            <label>Enter the Grid master password: </label>
            <input type="password" name="password" value=<?php echo $_POST["password"] ?> readonly><br/><br/>
            
            <label>Select the WAPI version: </label>
            <select name="version">
              <option value="v2.7">v2.7</option>
              <option value="v2.8">v2.8</option>
              <option value="v2.9">v2.9</option>
              <option value="v2.10" selected>v2.10</option>
            </select>
            <br/><br/><input type="submit" name="Submit">
        </form>
</fieldset>

<?php
}
else{
?>
<fieldset>
<h2>Invalid input!!</h2><h3> Either this IP-address/FQDN does not correspond to a grid master or the credentials are invalid!!</h3>
<a href="./home.php">Resubmit</a>
</fieldset>
<?php }}

else{
?>
<fieldset>
    <form  id="a" action="home.php" method="post">
    <label>Enter the Grid master IP / FQDN: </label>
    <input type="text" name="host"><br/><br/>
    <label>Enter the Grid master username: </label>
    <input type="text" name="username"><br/><br/>
    <label>Enter the Grid master password: </label>
    <input type="password" name="password"><br/><br/> 
        <br/><br/><input id="one" type="submit" name="Submit" onclick="change()">
        </form>
</fieldset>
<?php }
?>

<script type="text/javascript">
  function change(){
    var elem = document.getElementById("one");
    elem.value = "Vaidating"
    elem.style.cssText = 'background-color: red; color: white;';
  }
</script>
</body>
</html>
