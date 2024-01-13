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
echo '<body style="background-color:black; "><p style="text-align:center; padding-top:5%; padding-bottom:5%; "><img src="'.$files[$file].'" width="100%" height="auto" ></p>';
?>

</body>
</html>