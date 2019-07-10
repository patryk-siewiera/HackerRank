<?php

$a = 73;
$b = 67;
$c = 38;
$d = 33;


$val = 44;

$div = $val / 5;
$mod = $val % 5;

echo "\n".$mod."\n";

if ($mod > 3) {
    print((intval($div)) * 5 + 5);
} else {
    print($val);
}

