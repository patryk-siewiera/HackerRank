<?php
$handle = fopen ("php://stdin","r");
fscanf($handle, "%d", $number_of_elements);
$array = explode(" ", fgets($handle));
array_walk($array, 'intval');
echo array_sum($array);
?>