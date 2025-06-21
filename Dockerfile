# Use a recent Ruby slim base
FROM ruby:3.2-slim

# Install build essentials + Node for Jekyll
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    locales \
    imagemagick \
    build-essential \
    zlib1g-dev \
    python3-pip \
    inotify-tools procps && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    pip install nbconvert --break-system-packages

# RUN apt-get update -qq && \
#     apt-get install -y build-essential curl nodejs git imagemagick && \
#     rm -rf /var/lib/apt/lists/*

WORKDIR /srv/jekyll

# Ensure bundler matches your lockfile
COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v "$(grep 'BUNDLED WITH' -A1 Gemfile.lock | tail -1)" && \
    bundle install --jobs 4

# Copy the rest of your site
COPY . .

# Add a non-root user (better ownership)
RUN groupadd -g 1000 app && \
    useradd -u 1000 -g app -m app && \
    chown -R app:app /srv/jekyll

USER app
EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--livereload"]
