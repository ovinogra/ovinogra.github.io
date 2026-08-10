## Installing and Deploying

This repo is intended to be used with Docker for local development.

### Local development

From the repository root:

1. Run the first-time setup:
   ```bash
   docker compose up --build
   ```
2. Subsequent runs:
   ```bash
   docker compose up
   ```
3. Open the site at:
   ```text
   http://localhost:8080
   ```

The local container uses the project’s Dockerfile and docker-compose.yml to build and serve the Jekyll site.

### Helper scripts

Use the Conda environment for local helper scripts such as pre-commit and image optimization.

```bash
conda create -n moonenv python=3.11
conda activate moonenv
pip install -r req.txt
```

- `python scripts/optimize_images.py`: convert png images into jpegs
  - `python scripts/optimize_images.py --input-dir assets/img/illustrations_raw --output-dir assets/img/illustrations --quality 88`
