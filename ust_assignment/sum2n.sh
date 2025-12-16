sum_to_n() {
   n=$1
   sum=0

   for (( i=1; i<=n; i++ ))
   do
        sum=$((sum + i))
   done

   echo "Sum of 1 to $n numbers:$sum"
}

echo "Enter a number:"
read num

sum_to_n "$num"