# Copilot Instructions for Teracloud Streams Documentation Site

## Project Overview
This is a MkDocs-based documentation site for Teracloud Streams developer tools, using the Material theme. It includes gettingstarted guides, blog posts, and VS Code extension docs.

## Architecture
- **Site Structure**: Content in `docs/`, shared includes in `includes/`, custom styles in `docs/stylesheets/`.
- **Build System**: MkDocs with plugins (blog, minify, search). Configured in `mkdocs.yml`.
- **Navigation**: Defined in `mkdocs.yml` nav section, with sections like Getting Started, VS Code Extension, Blog.
- **Assets**: Images and icons in `docs/assets/`, custom CSS in `docs/stylesheets/extra.css`.

## Key Workflows
- **Local Development**: Run `mkdocs serve` for live-reloading server.
- **Build**: Use `mkdocs build` to generate static site in `site/` directory.
- **Dependencies**: Install with `pip install -r requirements.txt` (includes mkdocs-material, extensions, plugins).

## Conventions
- **Markdown Extensions**: Use pymdownx features like tabs, tasklists, mermaid diagrams (e.g., flowcharts in `docs/gettingstarted/index.md`).
- **Includes**: Share content via `includes/` (e.g., `includes/abbreviations.md` auto-appended via snippets extension).
- **Abbreviations**: Define in `includes/abbreviations.md` (e.g., *[SPL]: Streams Processing Language*).
- **Blog Posts**: Place in `docs/blog/posts/`, follow naming like `welcome.md`.
- **Front Matter**: Use YAML for page metadata (e.g., `hide: - navigation` in `docs/index.md`).

## Patterns
- **Diagrams**: Embed Mermaid in markdown for flowcharts (e.g., developer journey in gettingstarted).
- **Links**: Use relative paths for internal links, external to official docs.
- **Code Blocks**: Enable copy feature via theme config.
- **Social/Extra**: Configure in `mkdocs.yml` extra section for links and generator info.

## Integration Points
- **External Docs**: Links to `https://doc.streams.teracloud.com` for full product docs.
- **GitHub**: Social link to `https://teracloud-streams.github.io/`.
- **Email**: Contact via `mailto:info.streams@teracloud.com`.

Reference: `mkdocs.yml` for config, `docs/index.md` for home page structure, `docs/gettingstarted/index.md` for navigation examples.