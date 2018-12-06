# Python does GNU Cut

Example:

    echo '1|2|3|4|5|6|7' | python cut.py -d '|' -f-2,3-4,5- -
