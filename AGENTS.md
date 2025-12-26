## Committing code

Before running git commit, verify that the llamabot CLI is available and working.

1) Quick check

```zsh
llamabot --help
```

If the help text appears and the command exits successfully, you’re good to commit.

2) Detect missing/incorrect installation (one-liner)

```zsh
if command -v llamabot >/dev/null 2>&1; then llamabot --help; else echo "llamabot not on PATH"; fi
```

3) Troubleshooting (if the command is not found or fails)

- Ensure your virtual environment is activated (if the tool is installed there):
    ```zsh
    source .venv/bin/activate  # or your venv activation command
    ```
- Check where the executable would be found:
    ```zsh
    which llamabot      # or: type -a llamabot
    ```
- Install or reinstall locally:
    ```zsh
    uv tool install llamabot
    ```

4) After confirming llamabot --help works, proceed with your commit

```zsh
git add .
git commit
```

## Using pre-commit in this repository

Follow these steps from the project root (where `.git` and `pyproject.toml` live):

1) Check for existing pre-commit hooks

```zsh
[ -f .git/hooks/pre-commit ] && echo "pre-commit hook exists" || echo "no pre-commit hook found"
ls -l .git/hooks/pre-commit || true
cat .git/hooks/pre-commit || true
```

2) Run the project's pre-commit checks via `uvx`

```zsh
uvx pre-commit
```

3) If no hook was present, install `pre-commit` hooks

```zsh
pre-commit install
# to also install the pre-push hook:
pre-commit install --hook-type pre-push
```

4) Verify installation and run hooks manually

```zsh
[ -f .git/hooks/pre-commit ] && echo "pre-commit hook installed" || echo "installation failed"
pre-commit run --all-files
uvx pre-commit
```

5) Troubleshooting notes

- If `pre-commit install` fails in constrained CI environments, try `pre-commit install --install-hooks`.
- Ensure `pre-commit` and `uvx` are installed in the same Python environment you use for development.

These steps let you run the repository's configured checks and ensure git hooks are installed for local commits.
