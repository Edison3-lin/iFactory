# $wsh = New-Object -ComObject WScript.Shell
# $ans = $wsh.Popup("今天還愉快嗎？", 7, "請作答", 4 + 32)
# $msg = ""
# Switch ($ans) {
#     6 { $msg = "很高興聽到您今天感覺愉快！" }
#     7 { $msg = "希望您可以忘掉不愉快的事！" }
#     -1 { $msg = "有人在嗎？" }
# }

# $ans = $wsh.Popup($msg)

#顯示本機磁碟機的空間狀態
# $strComputer = "."
# $Disks = Get-WmiObject -Class Win32_LogicalDisk -Filter "DriveType = 3"`
#     -ComputerName $strComputer

# foreach ($Disk in $Disks) {
#     $XX = "xxxx: {0}" -f $Disk.MediaType
#     $ID = "磁碟機代碼：{0}" -f $Disk.DeviceID
#     $Label = "磁碟機名稱：{0}" -f $Disk.VolumeName
#     $Size = "磁碟機大小：{0:0.0} GB" -f ($Disk.Size / 1GB)
#     $FreeSpace = "剩餘的空間：{0:0.0} GB" -f ($Disk.FreeSpace / 1GB)
#     $Used = ([int64]$Disk.size - [int64]$Disk.FreeSpace)
#     $SpaceUsed = "已用的空間：{0:0.0} GB" -f ($Used / 1GB)
#     $Percent = ($Used * 100.0) / $Disk.Size
#     $Percent = "已用的比例：{0:N0}" -f $Percent

#     "---------------------"
#     "$XX"
#     "$ID"
#     "$Label"
#     "$Size"
#     "$FreeSpace"
#     "$SpaceUsed"
#     "$Percent %"
# }

#本機電腦的環境變數
# $strComputer = "."

# $colItems = Get-WmiObject -Class Win32_Environment `
#     -Namespace "root\CIMV2" `
#   -ComputerName $strComputer

# foreach ($objItem in $colItems) {
#       Write-Host "標題：" $objItem.Caption
#       Write-Host "說明：" $objItem.Description
#       Write-Host "安裝日期：" $objItem.InstallationDate
#       Write-Host "名稱：" $objItem.Name
#       Write-Host "狀態：" $objItem.Status
#       Write-Host "是否為系統變數：" $objItem.SystemVariable
#       Write-Host "使用者名稱：" $objItem.UserName
#       Write-Host "變數值：" $objItem.VariableValue
# }

#三維餅圖
# create new excel instance
# $objExcel = New-Object -comobject Excel.Application
# $objExcel.Visible = $True
# $objWorkbook = $objExcel.Workbooks.Add()
# $objWorksheet = $objWorkbook.Worksheets.Item(1)

# # write information to the excel file
# $i = 0
# $first10 = (ps | sort ws -Descending | select -first 10)
# $first10 | foreach -Process { $i ; $objWorksheet.Cells.Item($i, 1) = $_.name; $objWorksheet.Cells.Item($i, 2) = $_.ws }
# $otherMem = (ps | measure ws -s).Sum – ($first10 | measure ws -s).Sum
# $objWorksheet.Cells.Item(11, 1) = “Others”; $objWorksheet.Cells.Item(11, 2) = $otherMem

# # draw the pie chart
# $objCharts = $objWorksheet.ChartObjects()
# $objChart = $objCharts.Add(0, 0, 500, 300)
# $objChart.Chart.SetSourceData($objWorksheet.range(“A1:B11”), 2)
# $objChart.Chart.ChartType = 70
# $objChart.Chart.ApplyDataLabels(5)


# Get-History | Out-File 1.txt
# Get-Process | Out-File 2.txt
# Get-Process | Format-List
# Measure-Command { &"c:\Users\All Users\test.cmd" }
# Get-Process | Format-Table
# Invoke-History 1
# Get-Process | Format-Table

# $scriptPath = Split-Path $script:MyInvocation.MyCommand.Path #當前應用程序目錄

# Write-Host "Current script directory is $scriptPath" -ForegroundColor Yellow

# $file1 = ((Get-Item 'd:\Backup\Office2019\ProPlus2019Retail.img').length / 1GB)
# $file2 = ((Get-Item 'd:\Backup\tcup75.exe').length / 1MB)

# Write-Host($file1)
# Write-Host($file2)
# # Write-Host((Get-Item $file1).length/1GB)
# if(($file1 -lt 25) -and ($file1 -gt 4)){
#     Write-Host('111111')
# }else {
#     Write-Host('888888')
# }


# $Ref_Size = 24
# $Data_Size = 25
# if(($Ref_Size -lt 25) -and ($Data_Size -lt 25))
# {
#     Write-Host("<=25")
# }
# elseif (($Ref_Size -gt 50) -and ($Data_Size -gt 50)) 
# {
#     Write-Host(">=50")
# }
# else 
# {
#     Write-Host(">=25 <=50")
# }



# $s_file = gci | where-object { $_.Name -match "_powersi_boardfile.s\D{2,4}p" } | % {$_.FullName}
# Write-Host($s_file)
# Write-Host((Get-Item $s_file).Length)
# Test-Path -path "test2.ps1"

# Add-Content 1.txt ‘example!'


# $json = (Get-Content 'd:\VPL\xxx\.info' -Raw) | ConvertFrom-Json
# Write-Host($json.board_file)


# $powerdc_location = Split-Path $MyInvocation.MyCommand.Path
# $uid = $powerdc_location.split('\')[-1]
# Write-Host($powerdc_location)

# $M_file = gci | where-object { $_.Name -match "_powersi_boardfile.bat" } | % {$_.FullName}
# if($M_file -eq $null)
# {
# # $TDR = test-path $M_file
# Write-Host('true')
# }
# else {
# Write-Host('false')
    
# }

# $f = Get-Content ./b.log | Select-String "Layer_Count="
# $file = ($f -split "Layer_Count=")
# if($file -gt 4){
#     Write-Host($file)
# }
# $file | Add-Content "edison1_log.txt"

# $StringABC = ""

# If ([String]::IsNullOrEmpty($StringABC))
# {
#     Write-Host "The string is null or empty."
# }
# Else
# {
#     Write-Host "The string is not empty."
# }

# $file = Get-Content ./sim_item.csv
# $port = ([string]$file[0]).Split("`t")[1].TrimStart("`"").TrimEnd("`"")
# Write-Host([int]$port + 1)

# $sim_CSV = Get-Content ./sim_item.csv
# $spd_file = gci | where-object { $_.Name -like "*_powersi_boardfile.spd" } | % {$_.FullName}
# foreach($item in $spd_file){
# Write-Host "$item"
# }


# $log_files = gci | where-object { $_.Name -match "powersi_boardfile_.*\d.log" } | % {$_.FullName}
# $simulation_count = 0
# foreach ($item in $log_files) {
#     $simulation_count++
# }

# Write-Host "$simulation_count"
# if($simulation_count -gt 1) {
#     $log_file = [string]$log_files[$i-1].Split("")
# }
# else {
#     $log_file = $log_files
# }    

# Write-Host "$log_file"

# $a = Get-Item .\*_powersi_boardfile_[0-9]*.log
# # $b = gci | foreach-Object{$_.LastWriteTime}
# if($a){
#     $i = $a[0]
#     foreach ($item in $a) {
#         if($i.lastwritetime -lt $item.lastwritetime){
#             $i = $item    
#         }
#     }
#     write-host "$i $(Get-Date $i.lastwritetime)"
# }

# $data_file = gci | where-object { $_.Name -match "_powersi_boardfile_" } | % {$_.FullName}
# write-host "data_file=$data_file"
# create a new stopwatch

# $stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

# # run a command
# # $info = Get-Hotfix

# # stop the stopwatch, and report the milliseconds
# $stopwatch.Stop()
# $stopwatch.Elapsed.Milliseconds

# # continue the stopwatch
# $stopwatch.Start()
# # $stopwatch.Restart()  # <- resets stopwatch

# # run another command
# $files = Get-ChildItem -Path $env:windir
# Write-Host "$files"
# # Write-Host "$files"
# cls

# # again, stop the stopwatch and report accumulated runtime in milliseconds
# $stopwatch.Stop()
# $stopwatch.Elapsed.Milliseconds

# $StopWatch = New-Object -TypeName System.Diagnostics.Stopwatch 


# $timer = [System.Diagnostics.Stopwatch]::StartNew()
# while ($timer.Elapsed.TotalSeconds -lt 10) {
#     ## Do some stuff here
#     ## Wait a specific interval
#     Start-Sleep -Seconds 1
  
#     ## Check the time
#     $totalSecs = [math]::Round($timer.Elapsed.TotalSeconds, 0)
#     Write-host "Still waiting for action  to complete after [$totalSecs] seconds..."
# }


[datetime]$t1 = '11:11:11'
[datetime]$t2 = '11:12:18'
[datetime]$t3 = '11:11:13'
[datetime]$t4 = '11:11:14'
[datetime]$t5 = '11:11:15'

if($t1 -le $t2){
    # $i = ($t2 - $t1)| New-TimeSpan
    $q = (get-date $t2) - (get-date $t1)
    # $i = $q.ToInt16
    Write-Host($q) 
}


$TimeString = $q
$TimeSpan = [System.TimeSpan]::Parse($TimeString)
$Seconds = [System.Math]::Round($TimeSpan.TotalSeconds, 0)
write-host($Seconds.ToString() + " Seconds")




