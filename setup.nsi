; 5/17/16 from http://www.py2exe.org/index.cgi/SingleFileExecutable
!define py2exeOutputDir 'dist'
!define exe             'md2html.exe'
;!define icon            'C:\python23\py.ico'
!define compressor      'lzma'  ;one of 'zlib', 'bzip2', 'lzma'
!define onlyOneInstance
!include FileFunc.nsh
!insertmacro GetParameters

; - - - - do not edit below this line, normaly - - - -
!ifdef compressor
    SetCompressor ${compressor}
!else
    SetCompress Off
!endif
Name ${exe}
OutFile ${exe}
;SilentInstall silent
RequestExecutionLevel user
!ifdef icon
    Icon ${icon}
!endif

InstType exec
InstType install
!define INST_EXEC 1
!define INST_INSTALL 2
Var CurDir ;CWD when the installer is started.

;If we choose to install.
Page Directory
Page InstFiles


Section -exec
  SectionIn ${INST_EXEC}
    
    ; Get directory from which the exe was called
    ;System::Call "kernel32::GetCurrentDirectory(i ${NSIS_MAX_STRLEN}, t .r0)"
    
    ; Unzip into pluginsdir
    InitPluginsDir
    SetOutPath '$PLUGINSDIR'
    File /r '${py2exeOutputDir}\*.*'
    
    ; Set working dir and execute, passing through commandline params
    SetOutPath '$CurDir'
    ${GetParameters} $R0
    nsexec::exec '"$PLUGINSDIR\${exe}" $R0'
    Pop $R2
    SetErrorLevel $R2
 
SectionEnd

Section -install
  SectionIn ${INST_INSTALL}
  SetOutPath $InstDir
  File /r '${py2exeOutputDir}\*.*'
SectionEnd

Function .onInit
  ; - - - - Allow only one installer instance - - - -
!ifdef onlyOneInstance
 System::Call "kernel32::CreateMutexA(i 0, i 0, t '$(^Name)') i .r0 ?e"
 Pop $0
 StrCmp $0 0 launch
  Abort
 launch:
!endif
; - - - - Allow only one installer instance - - - -
    ; Get directory from which the exe was called
    System::Call "kernel32::GetCurrentDirectory(i ${NSIS_MAX_STRLEN}, t .r0)"
    StrCpy $CurDir "$0"
    ${GetParameters} $0
    ;MessageBox MB_OK "after GetParameters $$0=$0" ; debug
    ${GetOptions} "$0" "/install" $1
    IfErrors exec 0
    ;MessageBox MB_OK "Did not get error flag, installing" ; debug
    ;Install, not silent
    SetSilent normal
    IntOp $0 ${INST_INSTALL} - 1
    SetCurInstType $0
    StrCpy $InstDir $CurDir
    GoTo end
  exec:
    ;Install, execute, and remove.
    SetSilent Silent
    IntOp $0 ${INST_EXEC} - 1
    SetCurInstType $0
    End:
FunctionEnd
