number() {
   num=$1
   if [ "$num" -gt 0 ]; then
      echo "The number is +ve"
   elif [ "$num" -lt 0 ]; then
      echo "The number is -ve"
   else
      echo "The number is ZERO"
   fi
}

echo "Enetr a number:"
read num

number "$num"