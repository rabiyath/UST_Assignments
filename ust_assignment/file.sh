chkfile() {

  file=$1

  if [ -e "$file" ]; then
     echo "File exists: $file"

     if [ -r "$file" ]; then
        echo "Read permission: Yes"
     else
        echo "Read permission: No"
     fi


     if [ -w "$file" ]; then
        echo "Write permission: Yes"
     else
        echo "Write permission: No"
     fi

     if [ -x "$file" ]; then
        echo "Execute permission: Yes"
     else
        echo "Execute permission: No"
     fi

  else
      echo "File not found"

  fi

}

echo "Enter file name:"
read file

chkfile "$file"