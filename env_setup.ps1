# installer pakkemanager chocolatey fra www.chocolatey.com
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) --y


### programmer til programmering i skolen
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# installerer en rekke unix-kommandoer (touch, ls, cd, grep etc.) samt
# bash-type autokomplettering
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install unxutils --y		    
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install clink --y			

C:\Users\eindr\Documents\GitHub\programmering_uskole
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install anaconda3 --y		
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install cmder --y		# forbedret shell (optional)


conda install git                                                               # versjonskontroll
conda create -n envskole m2-base                                                # lager et virtuelt miljø
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install arduino        # arduino-ide
# Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install fritzing       # software for utvikling av elektronikk



# diverse nyttig
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install pdfsam		# open source split, merge og rotering av pdf
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install vim			# vim editor (på windows! :-> )
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install emacs			# emacs editor (på windows! :-> )
#
## nettverkssniffing
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install wireshark
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install rawcap
#
## nettverksverktøy
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install curl
#
#
## run on upstart monitorering
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install autoruns



# definer hotkeys for automatisering
# choco install autohotkey





