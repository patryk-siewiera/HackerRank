<?php

// Complete the miniMaxSum function below.
function miniMaxSum($arr)
{
    asort($arr);

    $arr_min = array_slice($arr, 0, 4);
    $arr_max = array_slice($arr, 0, 4);

    $arr_min_sum = array_sum($arr_min);
    $arr_max_sum = array_sum($arr_max);


    print_r($arr_min_sum);
    echo " ";
    print_r($arr_max_sum);
}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%[^\n]", $arr_temp);

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

miniMaxSum($arr);

fclose($stdin);
