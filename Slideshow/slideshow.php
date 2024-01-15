<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digitaler Bilderrahmen</title>
    <script>
        setTimeout(function(){
            location.reload();
        }, 10000);
    </script>
</head>
<body>

<?php
$files = glob("pictures/*.*");
$file = array_rand($files, 1);

// Bild in voller Größe anzeigen
//echo '<body style="background-color:black; "><p style="text-align:center; padding-top:5%; padding-bottom:5%; "><img src="'.$files[$file].'" hight="100%" width="auto" ></p>';
//echo '<body style="background-color:black; margin: 0; padding: 0; height: 100vh;"><p style="text-align:center; padding-top:5%; padding-bottom:5%; margin: 0;"><img src="'.$files[$file].'" style="max-height: 100%; width: auto;"></p>';
echo '<body style="background-color:black; margin: 0; padding: 0; height: 90vh;"><p style="text-align:center; padding-top:1%; padding-bottom:1%; margin: 0;"><img src="'.$files[$file].'" style="max-width: 1000px; max-height: 580px; height: auto; width: auto;"></p>';
?>

</body>
</html>
