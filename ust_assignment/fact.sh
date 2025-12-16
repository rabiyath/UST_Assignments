factorial() {
   num=$1
   fact=1

   while [ "$num" -gt 1 ]
   do
        fact=$((fact * num))
        num=$((num - 1))
   done

   echo "Factorial is:$fact"
}

echo "Enter a number:"
read number

factorial "$number"