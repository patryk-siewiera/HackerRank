<?php

// Complete the staircase function below.
function staircase($n)
{
    $space = ' ';
    $symbol = '#';
    $how_much_space = 0;
    $how_much_symbol = 0;

    for ($i=1; $i<$n+1; $i++)
    {
        $how_much_space = $n - $i;
        $how_much_symbol =  $i;

        $temp_space = str_repeat($space, $how_much_space);
        $temp_symbol = str_repeat($symbol, $how_much_symbol);

        echo $temp_space;
        echo $temp_symbol, "\n";
    }

}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

staircase($n);

fclose($stdin);
