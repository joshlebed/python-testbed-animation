if [[ $(ls -Art | grep .py) ]]; then
    echo "found a python file"
    # get most recent file and increment
    fullfile=$(ls -Art | grep .py | tail -n 1 | tr -d '0-9')
    echo $fullfile

    filename=$(basename -- "$fullfile")
    extension="${filename##*.}"
    filename="${filename%.*}"

    echo $filename
    echo $extension
    echo $filename

    # start counting at v2, and increment until a slot is found
    i=2
    while [[ -e $filename$i.$extension || -L $filename$i.$extension ]] ; do
        let i++
    done
    filename=$filename$i
    $VISUAL "$filename".$extension

else
    echo "no python files found, creating a new one"
    $VISUAL version1.py
fi