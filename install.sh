#! /bin/bash

current_dir=$PWD
pip install -r requirements.txt

cd
if test ".bashrc"
then
    echo "alias pdf='python $current_dir/src/main.py'" >> .bashrc
fi

if test ".zshrc"
then
    echo "alias pdf='python $current_dir/src/main.py'" >> .zshrc
fi