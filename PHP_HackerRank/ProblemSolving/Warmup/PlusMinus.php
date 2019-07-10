<?php

// Complete the plusMinus function below.
function plusMinus($arr, $n)
{
    $positive = 0;
    $negative = 0;
    $zeros = 0;

    for ($i = 0; $i < $n; $i++) {
        if ($arr[$i] == 0) {
            $zeros++;
        } elseif ($arr[$i] > 0) {
            $positive++;
        } elseif ($arr[$i] < 0) {
            $negative++;
        }
    }

    echo $positive / $n, "\n";
    echo $negative / $n, "\n";
    echo $zeros /$n ;

}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

fscanf($stdin, "%[^\n]", $arr_temp);

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

plusMinus($arr, $n);

fclose($stdin);
