# Vscode

## Extensions:

### For Common Editor

- `VisualStudioExptTeam.vscodeintellicode`: IntelliCode
- `formulahendry.auto-close-tag`: Auto Close Tag
- `oderwat.indent-rainbow` : Indent Rainbow
- `shardulm94.trailing-spaces`: Trailing Spaces

### For Python

- `ms-python.python`: Python
    - `ms-python.vscode-pylance`: Pylance
    - `ms-toolsai.jupyter`: Jupyter support
        - `ms-toolsai.jupyter-keymap`: Jupyter keymap
        - `ms-toolsai.jupyter-renderers`: Jupyter renderers
        - `ms-toolsai.vscode-jupyter-slideshow`: Jupyter slideshow
        - `ms-toolsai.vscode-jupyter-cell-tags`: Jupyter cell tags
- `ms-python.pylint`: Linting support for python files
- `ms-python.isort`: Import Organization support for python files

### For Database

- `cweijan.vscode-mysql-client2`: MySQL Client
- `mongodb.mongodb-vscode`: Mongo DB

### For Github

- `GitHub.copilot`
- `GitHub.vscode-pull-request-github`: GitHub Pull Request
    - `vscode.github-authentication`: GitHub Authentication
- `GitHub.github-vscode-theme`: GitHub Theme

## Settings:

File: `.vscode/settings.json`

```
{
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.analysis.typeCheckingMode": "basic",
    "python.defaultInterpreterPath": ".venv/bin/python3",
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=120"
    ],
    "python.linting.pylintEnabled": false,
    "python.linting.enabled": false,
    "python.linting.banditEnabled": false,
    "python.linting.mypyEnabled": false,
    "python.formatting.autopep8Args": ["--max-line-length", "250", "--experimental"],
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "python.analysis.autoImportCompletions": true,
    "editor.wordWrap": "off",
    "explorer.confirmDelete": false,
    "editor.renderWhitespace": "all",
}

```
## Launch Server

File: `.vscode/launch.json`

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "dj runserver",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver", "0.0.0.0:8000"
            ],
            "django": true,
            "justMyCode": false
        },
        {
            "name": "dj shell",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "shell"
            ],
            "django": true,
            "justMyCode": false
        },
        {
            "name": "dj migrate",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "migrate",
            ],
            "django": true,
            "justMyCode": false
        },
        {
            "name": "dj command",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "sample_cmd",
                "-sample_option"
            ],
            "django": true,
            "justMyCode": false
        },
    ]
}

```
