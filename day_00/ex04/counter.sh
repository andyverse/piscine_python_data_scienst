# /bin/sh

echo "\"name\"","\"count\"" > hh_uniq_positions.csv
(tail -n +2 ../ex03/hh_positions.csv | \
awk 'BEGIN { FS = OFS = "," }
    {
        if (index($3, "Junior"))
            JUN++
        if (index($3, "Middle"))
            MID++
        if (index($3, "Senior"))
            SEN++
    }
    END { print "\"Senior\"",
                SEN "\n\"Junior\"",
                JUN "\n\"Middle\"", MID }
    ') | sort -t',' -rnk 2 >> hh_uniq_positions.csv