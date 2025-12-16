add() {
    echo "Result: $(( $1 + $2 ))"
}

subtract() {
    echo "Result: $(( $1 - $2 ))"
}

multiply() {
    echo "Result: $(( $1 * $2 ))"
}

divide() {
    if [ "$2" -eq 0 ]; then
        echo "Error: Division by zero not allowed"
    else
        echo "Result: $(( $1 / $2 ))"
    fi
}

while true
do
    echo " Calculator Menu"
    echo "1. Add"
    echo "2. Subtract"
    echo "3. Multiply"
    echo "4. Divide"
    echo "5. Exit"
    echo "Enter your choice:"
    read choice

    if [ "$choice" -eq 5 ]; then
        echo "Exiting..."
        break
    fi

    echo "Enter first number:"
    read a
    echo "Enter second number:"
    read b

    case $choice in
        1) add "$a" "$b" ;;
        2) subtract "$a" "$b" ;;
        3) multiply "$a" "$b" ;;
        4) divide "$a" "$b" ;;
        *) echo "Invalid choice" ;;
    esac
done