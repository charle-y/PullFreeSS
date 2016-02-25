tasklist|findstr /i "Shadowsocks">nul&&(taskkill /im Shadowsocks.exe 2>nul&&grep.exe&&taskkill /im Shadowsocks.exe /f /t 2>nul&&start "" "Shadowsocks.exe")
ping -n 5 0 >nul