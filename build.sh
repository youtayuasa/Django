set -o errexit
export DJANGO_SETTINGS_MODULE=bookproject.settings
cd /opt/render/project/src
pip install -r requirements.txt
python3 bookproject/manage.py collectstatic --no-input
python3 bookproject/manage.py migrate