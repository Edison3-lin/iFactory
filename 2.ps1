if(Test-path "ref_addr_step3.spd") {
    $ref_addr_step3_file = Get-content ref_addr_step3.spd
    $line = 0
    $pin_type = 0
    foreach ($item in $ref_addr_step3_file) {
        # For Single-Ended
        if( $item.Contains(".Connect ") -and $item.Contains(" NEXT "))
        {
            $line += 1
            $pin_type = 1
            continue
        }    
        if( $item.Contains(".Connect ") -and $item.Contains(" FEXT "))
        {
            $line += 1
            $pin_type = 1
            continue
        }    

        # For Differential Pair
        if( $item.Contains(".Connect ") -and $item.Contains("Diff_FEXT"))
        {
            $line += 1
            $pin_type = 2
            continue
        }    
        if( $item.Contains(".Connect ") -and $item.Contains("Diff_NEXT"))
        {
            $line += 1
            $pin_type = 2
            continue
        }

        if( $item.Contains(".EndC"))
        {
            $line += 1
            $pin_type = 0
            continue
        }      
                     
        if($pin_type -eq 1)  
        {
            if($item.EndsWith("::GND"))
            {
                $ref_addr_step3_file[$line] = $item.remove(0, 3).insert(0,"gnd")
            }
            else
            {
                $ref_addr_step3_file[$line] = $item.remove(0, 3).insert(0,"pos")
            }
        }

        if($pin_type -eq 2)  
        {
            if($item.EndsWith("::GND"))
            {
                $ref_addr_step3_file[$line] = $item.remove(0, 3).insert(0,"gnd")
            }
            elseif($item.EndsWith('P'))
            {
                $ref_addr_step3_file[$line] = $item.remove(0, 3).insert(0,"pos")
            }
            elseif($item.EndsWith('N')) 
            {
                $ref_addr_step3_file[$line] = $item.remove(0, 3).insert(0,"neg")
            }
        }

        $line += 1   
    }
}

Set-Content ref_addr_step3.spd $ref_addr_step3_file

# $FileContent = Get-Content "t.txt" 
# $FileContent | % { If ($_.ReadCount -ge 90 -and $_.ReadCount -le 120) {$_ -Replace "WARN","DEBUG"} Else {$_} } | Set-Content -Path "t.txt" 