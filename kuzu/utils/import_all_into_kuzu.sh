
for py_file in $(ls ./import/*.py | sort); do
    echo "Executing $py_file...";
    python3 $py_file
    if [ $? -ne 0 ]; then
        echo "Error executing $py_file, exiting...";
        exit 1;
    fi;
done
