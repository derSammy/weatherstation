<?php $files = glob("pictures/*.*");
$file = array_rand($files, 1);
echo '<body style="background-color:black; "><p style="text-align:center; padding-top:5%; padding-bottom:5%; "><img src="'.$files[$file].'" width="100%" height="auto" ></p>';

function refresh( $time ){
$current_url = $_SERVER[ 'REQUEST_URI' ];
return header( "Refresh: " . $time . "; URL=$current_url" );
}
refresh( 10 );
