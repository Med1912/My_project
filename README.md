# ngo-project-deployment

## 📦 Project Name

**A full-stack application with a FastAPI backend and Vite + React frontend.**  
Built with Docker, deployed via GitHub Actions, and structured for scalable development and deployment.

## 🛠️ Technologies

- **Backend**: FastAPI, SQLAlchemy, Alembic
- **Frontend**: Vite, React
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: OAuth2 with JWT
- **Secrets Management**: GitHub Secrets
- **Web Server**: Nginx (optional for future production)
- **Testing**: Pytest for backend, Vitest for frontend
- **Linting**: Flake8 for backend, ESLint for frontend
- **Version Control**: Git, GitHub
- **Environment Management**: Docker Compose for local development

## 🚀 Features

- 🔒 Submodules for frontend and backend
- ✅ CI/CD with linting, testing and building
- 🐳 Dockerized services using Docker
- 🔐 Secrets managed with GitHub Actions
- 🌐 Optional Nginx + HTTPS setup for future production

## ⚙️ Setup Instructions


### Build and run the Docker containers

```bash
docker-compose up --build
```

### Run the backend migrations

```bash
docker-compose exec backend alembic upgrade head
```

### Access the application

- **Backend**: [http://localhost:8000](http://localhost:8000)
  
- **Frontend**: [http://localhost:3000](http://localhost:3000)
md
Docker Image

[![Docker Pulls](https://img.shields.io/docker/pulls/mohamedkarbous/my-python-app)](https://hub.docker.com/r/mohamedkarbous/my-python-app)

Pull the image:

bash
docker pull mohamedkarbous/my-python-app:latest
```



