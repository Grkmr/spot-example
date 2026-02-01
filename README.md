# SpotExample

POC plugin that uses prebuilt **Spot** wheels generated in [**spot-wheeler**](https://github.com/Grkmr/spot-wheeler)

## Requirements

- `uv` (Astral)
- Linux (x86_64 or aarch64)

## Development

Create the environment and install dependencies:

```sh
uv sync
```

Build / check the plugin:

```sh
uv run ocelescope build
```

## Wheels

This project expects the Spot wheel(s) to be present locally and referenced via `tool.uv.sources`
in `pyproject.toml`.

Typical layout:

```text
src/spotexample/wheels/
  spot_local-...-x86_64.whl
  spot_local-...-aarch64.whl
```

## CI

See `.github/workflows/` for the CI build.
