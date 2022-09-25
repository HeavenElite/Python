$Computers = Import-Csv .\ITLabData.csv
for ( $i = 0; $i -lt $Computers.Length; $i++) {

    $Username   = $Computers[$i].Account
    $Password   = ConvertTo-SecureString -AsPlainText $Computers[$i].Password -Force
    $Credential = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$Password

    $Result =  Invoke-Command -ComputerName $Computers[$i].IP -Credential $Credential -ScriptBlock {Get-PSDrive -PSProvider FileSystem} -WarningAction SilentlyContinue -ErrorAction SilentlyContinue
    
[System.Console]::Beep(1000,1000)

