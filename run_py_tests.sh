array=(`find . -name "*test*.py"`)

for i in "${array[@]}"
do
    echo $i
    python3 $i
    echo
done