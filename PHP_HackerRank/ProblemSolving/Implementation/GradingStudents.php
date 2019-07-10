<?php

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

function gradingStudents($grades)
{
    $result = [];
    foreach ($grades as $note) {
        $temp = $note;
        while ($temp % 5 != 0) {
            $temp++;
        }
        if (($temp - $note < 3) && ($temp > 38))
            $note = $temp;

        $result[] = $note;
    }
    return $result;
}

$grades_count = intval(trim(fgets(STDIN)));

$grades = array();

for ($i = 0; $i < $grades_count; $i++) {
    $grades_item = intval(trim(fgets(STDIN)));
    $grades[] = $grades_item;
}

$result = gradingStudents($grades);

echo $result;

