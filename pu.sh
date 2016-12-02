#!/bin/sh
echo 'commit message?:'
read msg
git add .
git commit -m msg
echo 'pushing...'
git push
echo 'end'
