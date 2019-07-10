<?php

// Complete the birthdayCakeCandles function below.
function birthdayCakeCandles($ar)
{
    sort($ar);
    $size_n = sizeof($ar);
    $how_much = 0;

    for ($i = 0; $i < $size_n; $i++) {
        if ($ar[$size_n - 1] == $ar[$i]) {
            $how_much++;
        }
    }
    return $how_much;
}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $ar_count);

fscanf($stdin, "%[^\n]", $ar_temp);

$ar = array_map('intval', preg_split('/ /', $ar_temp, -1, PREG_SPLIT_NO_EMPTY));

$result = birthdayCakeCandles($ar);

fclose($stdin);