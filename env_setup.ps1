# installer pakkemanager chocolatey fra www.chocolatey.com
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) --y


### programmer til programmering i skolen
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# installerer en rekke unix-kommandoer (touch, ls, cd, grep etc.) samt
# bash-type autokomplettering
#Set-ExecutionPolicy Bypass -Scope Process -Force; choco install unxutils --y		    
Set-ExecutionPolicy Bypass -Scope Process -Force; choco install clink --y			
# bli kvitt irriterende langt prompt
# Endrer pÂ milj¯variabelen PROMPT
#cmd
#setx PROMPT skriv kommando$$$S
#powershell

# installer anaconda (samling med programvare for programmering i bla. python)
#Set-ExecutionPolicy Bypass -Scope Process -Force; choco install anaconda3 --y		

# forbedret shell (optional)
Set-ExecutionPolicy Bypass -Scope Process -Force; choco install cmder --y		
#Set-ExecutionPolicy Bypass -Scope Process -Force; choco install microsoft-windows-terminal --y


# installer git for versjonskontroll og opprett et virtuelt milj√∏
conda install git                                                               
conda create -n envmain m2-base                                                
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# arduino-ide
# Set-ExecutionPolicy Bypass -Scope Process -Force; choco install arduino        

# software for utvikling av elektronikk
# Set-ExecutionPolicy Bypass -Scope Process -Force; choco install fritzing       



# diverse nyttig
# open source split, merge og rotering av pdf
# Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install pdfsam		

# Bruk vim eller emacs p√• windows! :->
# Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install vim			
# Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install emacs

## nettverkssniffing
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install wireshark
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install rawcap
#

## nettverksverkt√∏y
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install curl
#
#
## run on upstart monitorering
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install autoruns


# definer hotkeys for automatisering
# choco install autohotkey





