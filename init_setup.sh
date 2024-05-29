echo[$(date)]:"start the init_setup file"
echo[$(date)]:"first create a virtual environment"

conda create -p env python==3.11 -y

echo[$(date)]: "then activate this"

source activate ./env

echo[$(data)]: "then execute the git init"

git init

echo[$(date)]: "end of init_setup.sh file"
