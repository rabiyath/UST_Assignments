echo "Enter a number:"
read num

if [ "$num" -lt 0 ]; then
   echo "Please enter +ve Number"
   exit 1
fi

rev=0

while [ "$num" -gt 0 ]
do
   rem=$((num % 10))
   rev=$((rev * 10 + rem))
   num=$((num / 10))
done

echo "Reversed number:$rev"