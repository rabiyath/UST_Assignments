prime() {
   num=$1
   count=0

   if [ "$num" -lt 2 ]; then
        echo "$num is not prime "
        return
   fi

   for (( i=2; i<=num/2; i++ ))
   do
        if [ $((num % i)) -eq 0 ]; then
           count=1
           break
        fi
   done


   if [ "$count" -eq 0 ]; then
        echo "$num is a prime"
   else
        echo "$num is not prime"
   fi

}

echo "Enter a number:"
read num

prime "$num"