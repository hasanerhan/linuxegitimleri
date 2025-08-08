#!/bin/bash

Is_this_prime() {
    number=$1 #it takes the value of number from the first parameter.

    if (( number < 2 )); then #this line starts a conditional check.It asks: "is the value of number less than 2"
        return 1 #return 1 immediately exits the function with a "failure" status. This is a quick way to stop the check because numbers less than 2 are never prime.
    fi

    for (( i=2; i<number; i++ )); do #this for loop iterates through numbers, starting from i=2. It continues as long as i is less than the number variable, incrementing i by one after each step.
        if (( number % i == 0 )); then #this line checks for divisibility.The expression number % i == 0 simply asks: "Is the remainder of number divided by i equal to zero? if the answer is yes,the number is perfectly divisible and the condition is true. 
            return 1 #return 1 immediately exist the function with a "failure"status.it means the number is not prime.
        fi
    done 

    return 0 #this immediately exits the function with a "success"status.it means the number is prime.
}

for irmak in $(seq 2 67); do #this for loop iterates through every number from 2 to 80.It assgins each number to variable irmak in each step of loop.
    if Is_this_prime $irmak; then 
        echo "$irmak" #this line checks if the number irmak is prime.If the check is succesful, the echo command prints that number to screen.
    fi
done
