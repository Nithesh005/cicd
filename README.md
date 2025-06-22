# Simple Flask App with CI/CD

A very simple Flask application with a complete CI/CD pipeline.

## What is CI/CD?

**CI (Continuous Integration)**: Automatically building and testing your code when you push changes
**CD (Continuous Deployment)**: Automatically deploying your app when tests pass

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the app locally

```bash
python app.py
```

The app will start on `http://localhost:5000`

## Endpoints

- `GET /` - Returns "Hello, World!"
- `GET /api/hello` - Returns JSON: `{"message": "hello world"}`

## Testing

Run tests locally:
```bash
python -m pytest test_app.py -v
```

Run with coverage:
```bash
python -m pytest test_app.py --cov=app
```

## CI/CD Pipeline

This project includes a complete CI/CD pipeline using GitHub Actions:

### What the pipeline does:

1. **On every push/PR**:
   - Runs linting (code quality checks)
   - Runs unit tests
   - Generates test coverage report
   - Uploads coverage to Codecov

2. **On main/master branch only**:
   - Deploys to production (Render)

### Pipeline stages:

1. **CI Stage** (`test` job):
   - Checkout code
   - Setup Python environment
   - Cache dependencies (faster builds)
   - Install requirements
   - Run linting with flake8
   - Run unit tests with pytest
   - Generate coverage report
   - Upload coverage to Codecov

2. **CD Stage** (`deploy` job):
   - Only runs if CI passes
   - Only runs on main/master branch
   - Deploys to Render (production)

### How to set up the pipeline:

1. **Push your code to GitHub**
2. **Enable GitHub Actions** (should be automatic)
3. **For deployment, you'll need to**:
   - Create a Render account
   - Connect your GitHub repo to Render
   - Add secrets to GitHub:
     - `RENDER_TOKEN`: Your Render API token
     - `RENDER_SERVICE_ID`: Your Render service ID

### Pipeline files:

- `.github/workflows/ci.yml` - Basic CI (testing only)
- `.github/workflows/ci-cd.yml` - Complete CI/CD pipeline
- `render.yaml` - Render deployment configuration

## Learning Path

1. **Start with basic CI** (`.github/workflows/ci.yml`)
2. **Add tests** (`test_app.py`)
3. **Add code quality** (flake8 linting)
4. **Add coverage reporting**
5. **Add deployment** (CD stage)
6. **Optimize** (caching, parallel jobs, etc.)

## Next Steps

- Add more comprehensive tests
- Add security scanning
- Add performance testing
- Set up staging environment
- Add database migrations
- Add monitoring and logging 