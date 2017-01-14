@ECHO OFF

set PY=python
set PELICAN=pelican
set BASEDIR=%cd%
set INPUTDIR=%BASEDIR%\content
set OUTPUTDIR=%BASEDIR%\output
set CONFFILE=%BASEDIR%\pelicanconf.py
set PUBLISHCONF=%BASEDIR%\publishconf.py

:: FTP_HOST=localhost
:: FTP_USER=anonymous
:: FTP_TARGET_DIR=/

:: SSH_HOST=localhost
:: SSH_PORT=22
:: SSH_USER=root
:: SSH_TARGET_DIR=/var/www

:: S3_BUCKET=my_s3_bucket

:: CLOUDFILES_USERNAME=my_rackspace_username
:: CLOUDFILES_API_KEY=my_rackspace_api_key
:: CLOUDFILES_CONTAINER=my_cloudfiles_container

:: DROPBOX_DIR=~/Dropbox/Public/

:: GITHUB_PAGES_BRANCH=master

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo. Makefile for a pelican Web site
	echo.
	echo. Usage:
	echo.    make html                           [re]generate the web site
	echo.    make clean                          remove the generated files
	echo.    make regenerate                     regenerate files upon modification
	echo.    make publish                        generate using production settings
	echo.    make server [PORT=8000]             serve site at http://localhost:8000
	echo.    make ssh_upload                     upload the web site via SSH
	echo.    make rsync_upload                   upload the web site via rsync+ssh
	echo.    make dropbox_upload                 upload the web site via Dropbox
	echo.    make ftp_upload                     upload the web site via FTP
	echo.    make s3_upload                      upload the web site via S3
	echo.    make cf_upload                      upload the web site via Cloud Files
	echo.    make github                         upload the web site via gh-pages
	echo.
	echo. Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html
	echo. Set the RELATIVE variable to 1 to enable relative urls
	echo.
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%OUTPUTDIR%\*) do rmdir /q /s %%i
	del /q /s %OUTPUTDIR%\*
	goto end
)

if "%1" == "html" (
	%PELICAN% %INPUTDIR% -o %OUTPUTDIR% -s %CONFFILE%
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %OUTPUTDIR%
	goto end
)

if "%1" == "regenerate" (
	%PELICAN% -r %INPUTDIR% -o %OUTPUTDIR% -s %CONFFILE% %PELICANOPTS%
)

if "%1" == "server" (
	set SERVER=%2
	set PORT=%3
	echo Pelican is running at http://localhost:8000/ Press Ctrl+C to stop.
	cd %OUTPUTDIR% && %PY% -m pelican.server %PORT% %SERVER% && cd ..
)

if "%1" == "publish" (
	%PELICAN% %INPUTDIR% -o %OUTPUTDIR% -s %PUBLISHCONF% %PELICANOPTS%
)

if "%1" == "ssh_upload" (
	echo Sorry this function undeveloped
)

if "%1" == "dropbox_upload" (
	echo Sorry this function undeveloped
)

if "%1" == "ftp_upload" (
	echo Sorry this function undeveloped
	:: ftp ftp://%FTP_USER%@%FTP_HOST% -e "mirror -R %OUTPUTDIR% %FTP_TARGET_DIR% ; quit"
)

if "%1" == "s3_upload" (
	echo Sorry this function undeveloped
)

if "%1" == "cf_upload" (
	echo Sorry this function undeveloped
)

if "%1" == "github" (
	echo Sorry this function undeveloped
	:: cd output
	:: git init
	:: git add .
	:: git commit -am "Site Update %Date%"
	:: git remote add %URL%
	:: git push
)

:end
