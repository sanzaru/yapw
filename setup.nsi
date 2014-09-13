#CONSTANTS
!define VERSION "0.0.1b"

OutFile Setup-${VERSION}.exe
Name "YAPW ${VERSION} Setup"

InstallDir "C:\YAPW-${VERSION}\"
LicenseData LICENSE
BrandingText "YAPW ${VERSION} installation. (C)2008, Martin Albrecht"
ShowUninstDetails show
CRCCheck on
XPStyle on

# Pages
Page license
Page directory
Page instfiles


Section	
	SetOutPath $INSTDIR
	File /r release\${VERSION}\*
	CreateDirectory $INSTDIR\logs
	
	WriteUninstaller $INSTDIR\uninstall.exe
	
	CreateShortCut "$SMPROGRAMS\YAPW\YAPW.lnk" "$INSTDIR\yapw.bat"
	CreateShortCut "$SMPROGRAMS\YAPW\Uninstall YAPW.lnk" "$INSTDIR\uninstall.exe"
	
	WriteRegStr HKLM "Software\YAPW\" "uninstall" "$INSTDIR\uninstall.exe"
	WriteRegStr HKLM "Software\YAPW\" "version" "${VERSION}"
	WriteRegStr HKLM "Software\YAPW\" "path" "$INSTDIR"
	
	Return
SectionEnd


Section "Uninstall"

	MessageBox MB_YESNO|MB_ICONQUESTION "Do you really want to uninstall YAPW?" IDNO exit

  Delete /REBOOTOK $INSTDIR\*.*
  Delete /REBOOTOK $INSTDIR\contrib\*.*
  Delete /REBOOTOK $INSTDIR\logs\*.*
  Delete /REBOOTOK $INSTDIR\www\*.*
  RMDir /r $INSTDIR\contrib
  RMDir /r $INSTDIR\www
  RMDir /r $INSTDIR\logs
  RMDir /r $INSTDIR
  DeleteRegKey HKLM "Software\YAPW\"
  
  RMDir /r "$SMPROGRAMS\YAPW\"
  
  exit:
	Return
SectionEnd
