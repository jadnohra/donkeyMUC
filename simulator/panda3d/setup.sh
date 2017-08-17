pip install --pre --extra-index-url https://archive.panda3d.org/ panda3d
python `dirname $0`/check_panda3d.py

if python `dirname $0`/check_panda3d.py | grep -q '0.997222'; then
  echo "Looks good"
else
  echo "Something is wrong"
fi
