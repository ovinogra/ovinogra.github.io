Forked from [al-folio](https://github.com/alshedivat/al-folio/tree/main), but removes dependency on pre-built docker containers and slimmed overall to remove unused features.

## Installing and Deploying

1. Fork the al-folio repo. Make name of repo be `<your-github-username>.github.io` if intending to use [GitHub pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites).
2. Go to `Settings -> Actions -> General -> Workflow permissions` and give `Read and write permissions` to GitHub Actions.
3. Open file `_config.yml`, set `url` to `https://<your-github-username>.github.io` and leave `baseurl` **empty** (do NOT delete it), as `baseurl:`.
4. Wait until the GitHub action with subtitle `Deploy site` finishes (check your repository **Actions** tab). This create the `gh-pages` branch. 
5. Go to `Settings -> Pages -> Build and deployment`, make sure that `Source` is set to `Deploy from a branch` and set the branch to `gh-pages` (NOT to main).
6. Wait until the GitHub action `pages-build-deployment` finishes (check your repository **Actions** tab), which takes ~45s, then navigate to `https://<your-github-username>.github.io` in your browser.
7. Customize by merging edits to `main` branch.

## Local Development

First time: 
```bash
$ docker compose up --build
```

Subsequent times:
```bash
$ docker compose up
```
