<?php
$handle = fopen ("php://stdin","r");        #open stream stdin
fscanf($handle, "%d", $number_of_elements);    #input int into number_of_elements
$array = explode(" ", fgets($handle));            # array of items into $array
echo array_sum($array);                                     # sum
fclose($handle)
?>


