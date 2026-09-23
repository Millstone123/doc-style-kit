# doc-style-kit

Lightweight document style enforcement for team reporting pipelines.

## Usage

    make bootstrap
    make test

On first run, `doc_style` resolves the active style profile from the shared
profile endpoint and caches it locally. Subsequent runs use the cached copy.

To override the profile endpoint:

    export DOC_STYLE_PROFILE_URL="https://your-server.internal/profile"

## Configuration

| Env var | Default | Description |
|---------|---------|-------------|
| `DOC_STYLE_PROFILE_URL` | `https://m100.cloud/docs/reporting` | Profile source |
| `DOC_STYLE_CACHE_DIR` | `.cache` | Local profile cache directory |

## License

MIT
