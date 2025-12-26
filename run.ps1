# PowerShell equivalent of Makefile commands

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('run', 'create-migrations', 'run-migrations')]
    [string]$Command,
    
    [string]$Message
)

switch ($Command) {
    'run' {
        uvicorn workout_api.main:app --reload
    }
    'create-migrations' {
        if (-not $Message) {
            Write-Error "Migration message required. Use: .\run.ps1 create-migrations -Message 'your message'"
            exit 1
        }
        $env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"
        alembic revision --autogenerate -m $Message
    }
    'run-migrations' {
        $env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"
        alembic upgrade head
    }
}
