<?php

/*
 * Complete the timeConversion function below.
 */
function timeConversion($s)
{
    $hour = substr($s, 0, 2);
    $rest = substr($s, 2, 6);
    $am_pm = substr($s, 8, 2);

    if ($am_pm == 'PM') {
        $hour = $hour + 12;
        if ($hour == 24) {
            $hour = '12';
        }
    } elseif ($am_pm == 'AM') {
        if ($hour == 12) {
            $hour = '00';
        }
    }
    $score = $hour . $rest;
    return $score;
}


$__fp = fopen("php://stdin", "r");

fscanf($__fp, "%[^\n]", $s);

$result = timeConversion($s);

print_r($result);

fclose($__fp);
