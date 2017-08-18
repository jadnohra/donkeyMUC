BASE=~/github/Urho3D-1.6
pushd BASE
cd ..
curl "https://codeload.github.com/urho3d/Urho3D/zip/1.6" -o Urho3D-1.6.zip
unzip Urho3D-1.6.zip
rm Urho3D-1.6.zip
cd Urho3D-1.6
sh cmake_generic.sh ./build
cd build
make
popd