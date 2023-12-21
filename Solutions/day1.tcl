set fp [open "Inputs/day1.txt" r]
set data [read $fp]
close $fp

set total 0

set lines [split $data "\n"]
foreach line $data {
    set first -1
    set last -1
    foreach char [split $line ""] {
        if {[string is integer $char]} {
            if {$first == -1} {
                set first $char
            } else {
                set last $char
            }
        }
    }
    if {$last == -1} {
        set last $first
    }
    set total [expr {$total + [expr {$first * 10 + $last}]}]
}

puts "Part 1"
puts $total

set total 0

set lines [split $data "\n"]

set pattern {one|two|three|four|five|six|seven|eight|nine|\d}


set data [regsub -all {oneight} $data {oneeight}]
set data [regsub -all {threeight} $data {threeeight}]
set data [regsub -all {fiveight} $data {fiveeight}]
set data [regsub -all {nineight} $data {nineeight}]
set data [regsub -all {twone} $data {twoone}]
set data [regsub -all {sevenine} $data {sevennine}]
set data [regsub -all {eightwo} $data {eighttwo}]
set data [regsub -all {eighthree} $data {eightthree}]

foreach line $data {
    set match [regexp -all -inline $pattern $line]

    set first [lindex $match 0]

    set last [lindex $match end]
    # puts $line

    switch $first {
        one {set first 1}
        two {set first 2}
        three {set first 3}
        four {set first 4}
        five {set first 5}
        six {set first 6}
        seven {set first 7}
        eight {set first 8}
        nine {set first 9}
    }

    switch $last {
        one {set last 1}
        two {set last 2}
        three {set last 3}
        four {set last 4}
        five {set last 5}
        six {set last 6}
        seven {set last 7}
        eight {set last 8}
        nine {set last 9}
    }

    set total [expr {$total + [expr {$first * 10 + $last}]}]
}

puts "Part 2"
puts $total



