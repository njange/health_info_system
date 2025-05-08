
# 🏥 Health Information System

A modern web-based **Health Information System** built with **Django** and **PostgreSQL**, containerized using **Docker**, and deployed via **GitHub Actions**. This system provides a scalable backend infrastructure to manage patient records, appointments, and healthcare-related data.

---

## 📂 Project Structure

```
health_info_system/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── app/                     # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                    # Your main application logic
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── ...
├── manage.py                # Django CLI entry point
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Docker multi-container setup
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (excluded in .gitignore)
└── README.md                # You're reading it 😄
```

---

## 🛠️ Tech Stack

| Layer               | Technology              |
|---------------------|-------------------------|
| **Framework**       | Django 4+               |
| **Database**        | PostgreSQL 14+          |
| **DevOps**          | Docker, GitHub Actions  |
| **Deployment**      | CI/CD Pipeline (GitHub) |
| **Language**        | Python 3.10             |
| **OS**              | Ubuntu (Docker-based)   |

---

## 🚀 Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- Docker + Docker Compose
- GitHub Account for Actions
- PostgreSQL 14+ (if running outside Docker)

---

### 🧪 Local Development

1. **Clone the repository:**

```bash
git clone https://github.com/njange/health_info_system.git
cd health_info_system
```

2. **Copy environment variables:**

```bash
cp .env.example .env
# Edit .env to match your local DB credentials
```

3. **Build and run using Docker Compose:**

```bash
docker-compose up --build
```

4. **Run migrations:**

```bash
docker-compose exec web python manage.py migrate
```

5. **Create superuser:**

```bash
docker-compose exec web python manage.py createsuperuser
```

6. **Access the app:**

- App: [http://localhost:8000](http://localhost:8000)
- Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

---

### 🧪 Running Tests

```bash
docker-compose exec web python manage.py test
```

---

### ⚙️ GitHub Actions (CI/CD)

This project uses **GitHub Actions** to:

- Install dependencies
- Run tests and migrations
- Deploy the application

> The workflow YAML file is located at `.github/workflows/deploy.yml`.

You can customize secrets and deployment targets in your repo's **GitHub > Settings > Secrets and variables**.

---


## 📁 Environment Variables (`.env`)

| Variable Name        | Description                        |
|----------------------|------------------------------------|
| `DEBUG`              | Enable/disable debug mode          |
| `SECRET_KEY`         | Django secret key                  |
| `POSTGRES_DB`        | Database name                      |
| `POSTGRES_USER`      | PostgreSQL username                |
| `POSTGRES_PASSWORD`  | PostgreSQL password                |
| `POSTGRES_HOST`      | DB host (e.g., `db`)               |
| `POSTGRES_PORT`      | Port (default: 5432)               |

---

## 👥 Contributing

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 🔒 Security

- All secrets are stored securely via GitHub Secrets.
- PostgreSQL is isolated via Docker network.
- Debug is turned off in production.
- Django security best practices followed (e.g., `ALLOWED_HOSTS`, HTTPS settings).

---

## 📚 License

MIT License © 2025 [Your Name or Org]

---

## 🙋‍♂️ Need Help?

If you have questions, feel free to open an [issue](https://github.com/njange/health_info_system/issues) or contact the maintainer.
