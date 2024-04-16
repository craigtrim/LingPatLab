<#
    .SYNOPSIS
    Download a machine learning model if it does not exist.

    .DESCRIPTION
    This script uses PowerShell to download a specified machine learning model from a specific URL if the model does not already exist in the specified directory.

    .INPUTS
    None. You cannot pipe objects to this script.

    .OUTPUTS
    None.

    .EXAMPLE
    PS> .\poetry_download_model.ps1
#>

# Define parameters for the script, with default values
param(
    [Parameter()]
    [System.String]
    $directoryPath = 'resources/lib',

    [Parameter()]
    [System.String]
    $destination = 'resources/lib/en_core_web_sm-3.7.0.tar.gz',

    [Parameter()]
    [System.String]
    $source = 'https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.0/en_core_web_sm-3.7.0.tar.gz'
)

# Check if the target directory exists
# If not, create the directory and all necessary parent directories
if (-not (Test-Path $directoryPath)) {
    New-Item -ItemType Directory -Force -Path $directoryPath
}

# Check if the target file already exists in the directory
# If not, download the file from the source URL and save it to the destination
if (-not(Test-Path -Path $destination -PathType Leaf)) {
    try {
        Invoke-WebRequest -Uri $source -OutFile $destination
        Write-Host "Model [$destination] has been downloaded."
    }
    # If there is an exception (like a network error), throw an error message
    catch {
        throw $_.Exception.Message
    }
}
# If the file already exists, write a message to the console and exit
else {
    Write-Host "Model [$destination] has already been downloaded."
}
