# Use a recent Ruby slim base
FROM ruby:3.2-slim

# Install system packages needed for Jekyll
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    imagemagick \
    inotify-tools \
    procps \
    git \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /srv/jekyll

# Ensure bundler matches your lockfile
COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v "$(grep 'BUNDLED WITH' -A1 Gemfile.lock | tail -1)" && \
    bundle install --jobs 4

# Copy the rest of your site
# COPY . .

# Create a non-root user
ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} app && \
    useradd -m -u ${UID} -g ${GID} app

USER app
EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--livereload"]
