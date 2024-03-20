rm -rf ./tempdir

mkdir tempdir

cp holamundo.py tempdir/

echo "FROM python:3" >> tempdir/Dockerfile
echo "WORKDIR /home/myapp" >> tempdir/Dockerfile


echo "COPY holamundo.py ./" >> tempdir/Dockerfile


echo "EXPOSE 5050" >> tempdir/Dockerfile

echo "CMD python3 ./holamundo.py" >> tempdir/Dockerfile

cd tempdir

docker build -t python .

docker run -t -d -p 5050:5050 --name python2 python

docker ps -a