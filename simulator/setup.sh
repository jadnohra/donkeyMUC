pip install pybullet
python check_bullet.py

if python ./check_bullet.py | grep -q '0.999826'; then
  echo "Looks good"
else
  echo "Something is wrong"
fi
