; ----------------VARIABLES-----------------

History := []
History1 := ""
ResetOnSpace := ;
ResetOnDelete := ;
backcount := 0

; ----------------FILE_READS----------------

FileReadLine, ResetOnSpace, settings.txt, 2
FileReadLine, ResetOnDelete, settings.txt, 4
file := FileOpen("history.txt", "w")
file.Close()

; ----------------CODE_LOOP----------------

While(1>0)
{
	Input, LastKey, T86400 L1 V
	backcount := 0
	History1 = %History1%%LastKey%
	if (StrLen(History1) > 12)
	{
		StringTrimLeft, History1, History1, 1
		History[1] := ""
	}
	file := FileOpen("history.txt", "w")
	file.Write(History1)
	file.Close()
}

; ----------------KEY_BINDINGS----------------

~Backspace::
	backcount := 0
	if (ResetOnDelete == 0)
	{
		if (History1)
		{
			StringTrimRight, History1, History1, 1
			file := FileOpen("history.txt", "w")
			file.Write(History1)
			file.Close()
		}
		else if (!History1)
		{
			History1 := History[1]
			History[1] := ""
			file := FileOpen("history.txt", "w")
			file.Write(History1)
			file.Close()
		}
	}
	if (ResetOnDelete == 1)
	{
		History1 := ""
		file := FileOpen("history.txt", "w")
		file.Close()
	}
	return

~Space::
	if (ResetOnSpace == 0)
	{
		History[1] := History1
		History1 := ""
		file := FileOpen("history.txt", "w")
		file.Close()
	}
	if (ResetOnSpace == 1)
	{
		History1 := ""
		file := FileOpen("history.txt", "w")
		file.Close()
	}

~^Backspace::
	History1 := ""
	file := FileOpen("history.txt", "w")
	file.Close()
	backcount += 1
	if (backcount >= 2)
	{
		History[1] := ""
	}

; TODO: VARIABLE HISTORY WITH UP TO 12 WORDS IN MEMORY
	
; TODO: ASSIGN JOB FOR SPACE, RETURN, AND TAB KEYS THAT WILL REGISTER THEIR FUNCTIONS (space will remove history, return will remove last letter from history, tab will do somting)
; TODO: ASSIGN ~RButton AND ~LButton, AND ENTER, AND ARROW KEYS A MACRO TO REMOVE HISTORY WHEN PRESSED (LINE CHANGE = NO MORE HISTORY)