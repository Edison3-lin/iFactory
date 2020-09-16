# get-process -processname ex*
# Write-Host "Edison"
$a = (Get-Item 'e:\EC\P6\PinSet.ini').LastWriteTime
Write-Host "$a" 
