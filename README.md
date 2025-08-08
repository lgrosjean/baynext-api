# Baynext API

A FastAPI-based backend service for managing Marketing Mix Modeling (MMM) datasets, jobs, and pipelines. This API provides endpoints for dataset management, pipeline execution, and analytics for marketing attribution modeling.

## 🚀 Features

- **Dataset Management**: Upload, validate, and manage marketing datasets
- **Pipeline Orchestration**: Create and execute MMM analysis pipelines
- **Job Monitoring**: Track the status and progress of analytical jobs
- **User Authentication**: Secure API access with JWT tokens
- **Database Integration**: PostgreSQL with SQLModel ORM
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation

## 🛠️ Technology Stack

- **Framework**: FastAPI 0.115+
- **Database**: PostgreSQL with SQLModel
- **Authentication**: JWT with python-jose
- **File Storage**: Vercel Blob integration
- **AI Engine**: Google Meridian
- **Testing**: pytest with async support
- **Linting**: Ruff
- **Dependency Management**: uv

## 📋 Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- PostgreSQL database
- Environment variables configured (see `.env` setup below)

## 🏃‍♂️ Quick Start

### 1. Install Dependencies

```bash
# Install all dependencies
uv sync
```

### 2. Environment Setup

Create a `.env` file in the backend directory:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/baynext_dev
```

### 3. Start Development Server

```bash
# Start the development server
uv run fastapi dev app/main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/v1/health


## 📁 Project Structure

```
backend/
├── app/
│   ├── api/v1/           # API endpoints
│   ├── core/             # Core functionality (db, security, settings)
│   ├── schemas/          # SQLModel schemas/models
│   ├── services/         # Business logic services
│   ├── tasks/            # Background tasks
│   ├── utils/            # Utility functions
│   └── validations/      # Data validation schemas
├── tests/               # Test suite
├── Makefile             # Development commands
├── pyproject.toml       # Dependencies and config
└── README.md           # This file
```

## 🔧 API Endpoints

### Health Check
- `GET /v1/health` - Service health status

### Authentication
- `GET /v1/me` - Get current user info

### Projects & Datasets
- `GET /v1/projects/{project_id}/datasets` - List project datasets
- `GET /v1/projects/{project_id}/datasets/{dataset_id}` - Get dataset details

### Jobs & Pipelines
- `GET /v1/projects/{project_id}/jobs` - List project jobs
- `GET /v1/projects/{project_id}/pipelines` - List project pipelines

## 🔐 Authentication

The API uses Bearer token authentication. Include your token in the Authorization header:

```bash
curl -H "Authorization: Bearer your-token-here" http://localhost:8000/v1/me
```

## 🌍 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `AUTH_SECRET` | Secret for JWT token signing | Yes |

## 🚀 Deployment

### Production Build
```bash
make run-prod
```

### Docker (if using)
```bash
docker build -t baynext-api .
docker run -p 8000:8000 baynext-api
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests
5. Run linting
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request


## 🆘 Troubleshooting

### Database Connection Issues
- Check your `DATABASE_URL` in `.env`
- Ensure PostgreSQL is running
- Verify database credentials

### Import Errors
- Run `make install` to sync dependencies
- Check Python version (requires 3.12+)

### Seeding Issues
- Check database connectivity
- Ensure migrations are up to date: `uv run alembic upgrade head`
- Clear existing data: `make clear`

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Typer Documentation](https://typer.tiangolo.com/)

---

**Happy coding! 🎉**
