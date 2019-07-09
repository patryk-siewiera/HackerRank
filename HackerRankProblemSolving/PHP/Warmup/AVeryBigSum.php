<?php

function aVeryBigSum($ar)
{
//    print_r($ar);       # print whole array
    $sum = array_sum($ar);
    return $sum;
}

function input_array()
{
    $handle = fopen("php://stdin", "r");        #open stream stdin
    fscanf($handle, "%d", $number_of_elements);    #input int into number_of_elements
    $array = explode(" ", fgets($handle));            # array of items into $array
    return $array;
}

$array = input_array();
echo(aVeryBigSum($array));