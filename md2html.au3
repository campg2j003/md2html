#include <FileConstants.au3>
#include <array.au3>
#include <AutoItConstants.au3>

func DbgMsg($s)
	Local $rtn = MsgBox($MB_OKCANCEL, "", $s)
	If $rtn == $IDCANCEL Then Exit 1
EndFunc


Func Usage()
	ConsoleWriteError("Usage: This program can run as a stand-alone executable or install itself in a folder.  " & @CRLF _
				 & "To install: md2html /install" & @CRLF _
				 & "To display usage as a stand-alone executable: md2html -h" & @CRLF)
EndFunc

; Sets @Error if any file is not installed.  Sets @extended to number of uninstalled files.
Func InstallFiles($InstDir)
	Local $Err = 0 ; number of files not installed
	;DbgMsg("Installing to " & $InstDir) ; debug
	$Err += FileInstall("dist\bz2.pyd", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\library.zip", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\md2html.exe", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\pyexpat.pyd", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\python27.dll", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\unicodedata.pyd", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\_elementtree.pyd", $InstDir, $FC_OVERWRITE)?0:1
	$Err += FileInstall("dist\_hashlib.pyd", $InstDir, $FC_OVERWRITE)?0:1
	If $Err Then SetError(1, $Err)
EndFunc
			
#region main
;DbgMsg("cmdLine[0] = " & $CmdLine[0]) ; debug
If $CmdLine[0] = 0 Then
	Usage()
	Exit
ElseIf $CmdLine[1] = "/install" Then
	$InstDir = FileSelectFolder("Install to folder:", @WorkingDir)
	If @Error Then
		MsgBox($MB_OK, "Error", "No installation folder")
		Exit 1
	EndIf
		;DbgMsg("InstDir ends with " & StringRight($InstDir, 1) & ", <> \ = " & (StringRight($InstDir, 1) <> "\"))
	If StringRight($InstDir, 1) <> "\" Then $InstDir &= "\"
	InstallFiles($InstDir)
	If @Error Then
		MsgBox($MB_OK, "Error", String(@Extended) & " files were not installed")
		Exit 1
	Else
		MsgBox($MB_OK, "Success", "Installation complete.  Remove " & $InstDir & " to uninstall")
		Exit 0
	EndIf
Else
	; Execute
	$InstDir = @TempDir & "\md2html\"
	DirRemove($InstDir, $DIR_REMOVE)
	DirCreate($InstDir)
	InstallFiles($InstDir)
	; Get command line parameters to pass to executable.
	$sArgs = _ArrayToString($CmdLine, " ", 1, $CmdLine[0])
	$sCmd = $InstDir & "md2html.exe" & " " & $sArgs
	;DbgMsg("Running command: " & $sCmd) ; debug
	$rtn = RunWait($sCmd, "", @SW_HIDE, $STDIO_INHERIT_PARENT)
	DirRemove($InstDir, $DIR_REMOVE)

EndIf ; else execute
#endregion main
