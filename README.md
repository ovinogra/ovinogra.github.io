Uses [al-folio](https://github.com/alshedivat/al-folio/tree/main) as a starting point, but slims out unused features.

## Installing and Deploying

This repo is intended to be used with Docker for local development and GitHub Actions for deployment to GitHub Pages.

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

### Deploying to GitHub Pages

To stand up deployment in a fresh copy of this repo:

1. Create a GitHub repository. If you want a user/site URL, name it `<your-github-username>.github.io`.
2. In the repository settings, allow GitHub Actions to write to the repository and enable GitHub Pages.
3. Update `_config.yml` so that:
   - `url` points to your GitHub Pages URL, for example `https://<your-github-username>.github.io`
   - `baseurl` is left empty, i.e. `baseurl:`
4. Commit and push your changes to the default branch (usually `main`).
5. The workflow in `.github/workflows/deploy.yml` will build the site and deploy it to the `gh-pages` branch on push.
6. In GitHub Pages settings, set the source to “Deploy from a branch” and choose `gh-pages`.
7. Wait for the Pages build to finish, then visit your site at `https://<your-github-username>.github.io`.
