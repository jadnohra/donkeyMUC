pip install pybullet
python `dirname $0`/check_bullet.py

if python `dirname $0`/check_bullet.py | grep -q '0.999826'; then
  echo "Looks good"
else
  echo "Something is wrong"
fi
