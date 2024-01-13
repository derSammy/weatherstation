<?php  $files = glob("pictures/*.*");
$file = array_rand($files, 1);

// Setze Header-Informationen zuerst
//function refresh($time) {
//    $current_url = $_SERVER['REQUEST_URI'];
//    header("Refresh: " . $time . "; URL=$current_url");
//}

// Rufe die refresh-Funktion mit einem Wert von 10 auf
//refresh(10);

// Führe die restlichen HTML-Ausgaben durch
echo '<body style="background-color:black; "><p style="text-align:center; padding-top:5%; padding-bottom:5%; "><img src="'.$files[$file].'" width="100%" height="auto" ></p>';
