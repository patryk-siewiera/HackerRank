<?php

function test($ar)
{
    $how_many = count($ar);
    return $how_many;
}

$ar = array("jeden"=>"23", "dwa", "trzy");
echo(test($ar));

echo $ar["jeden"];

