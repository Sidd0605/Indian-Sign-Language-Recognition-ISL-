#! /bin/sh
echo "======================="
echo "Welcome to setup"
echo "======================="

if [ -f "env/bin/activate" ];
then
    echo "Enabling Unix virtual env"
    . env/bin/activate
elif [ -f "env/Scripts/activate" ];
then
    echo "Enabling Windows-style virtual env"
    . env/Scripts/activate
else
    echo "No virtual env found, using system python"
fi

python3 main.py

if command -v deactivate >/dev/null 2>&1;
then
    deactivate
fi
