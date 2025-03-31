# myteam_members_docker
This is a Dockerized Solution for Team member Management App in Django REST (Python).

# Usage - 

1. Git Clone <repo Name>
2. cd <director>
3. **Build the image**
   docker build -t myteam_members_backend .
5. **(Run migrations but also mount the local folder containing your code so that db.sqlite3 stays on your host:)**
   docker run --rm -it \
  -v "$(pwd)":/app \
  myteam_members_backend \
  python manage.py migrate
6. **Run the server, again mount the same volume**
   docker run -p 8000:8000 \
  -v "$(pwd)":/app \
  myteam_members_backend

**Pre-requisite - Should Have Python and Docker Setup.**


