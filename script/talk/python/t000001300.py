# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Sleeping Ursine
#-----------------------------------------------------
def t000001300_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000001300_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t000001300_1000():
    """State 0,2,3"""
    assert t000001300_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000001300_2000():
    """State 0,2,3"""
    assert t000001300_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000001300_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6210:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t000001300_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t000001300_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001300_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000001300_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000001300_x1()
    else:
        """State 4,7"""
        call = t000001300_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000001300_x1()
    """State 9"""
    return 0

def t000001300_x4():
    """State 0,1"""
    assert t000001300_x1()
    """State 2"""
    return 0

def t000001300_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000001300_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000001300_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000001300_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000001300_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000001300_x13(val1=val1, z1=z1)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t000001300_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000001300_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000001300_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000001300_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000001300_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000001300_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000001300_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000001300_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000001300_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001300_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000001300_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t000001300_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000001300_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001300_x10(z6=_, val6=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t000001300_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000001300_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000001300_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001300_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000001300_x12():
    """State 0,1"""
    assert t000001300_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t000001300_x13(val1=5, z1=1):
    """State 0,2"""
    assert t000001300_x23()
    """State 1"""
    call = t000001300_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000001300_x25()
    """State 4"""
    return 0

def t000001300_x14():
    """State 0,1"""
    assert t000001300_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t000001300_x15(val5=30):
    """State 0,1"""
    call = t000001300_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000001300_x26()
    """State 3"""
    return 0

def t000001300_x16():
    """State 0,1"""
    assert t000001300_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t000001300_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000001300_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000001300_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000001300_x28()
    """Unused"""
    """State 6"""
    return 0

def t000001300_x18():
    """State 0,2"""
    call = t000001300_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000001300_x19():
    """State 0,1"""
    assert t000001300_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t000001300_x20():
    """State 0,1"""
    assert t000001300_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t000001300_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000001300_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000001300_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000001300_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000001300_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000001300_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000001300_x23():
    """State 0,1"""
    assert t000001300_x24()
    """State 2"""
    return 0

def t000001300_x24():
    """State 0,1"""
    assert t000001300_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t000001300_x25():
    """State 0,1"""
    call = t000001300_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000001300_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001300_x26():
    """State 0,1"""
    call = t000001300_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000001300_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001300_x27():
    """State 0,1"""
    call = t000001300_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000001300_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001300_x28():
    """State 0,1"""
    call = t000001300_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000001300_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001300_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t000001300_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t000001300_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t000001300_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t000001300_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001300_x32():
    """State 0,1"""
    assert t000001300_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t000001300_x33():
    """State 0,1"""
    assert t000001300_x1()
    """State 2"""
    return 0

def t000001300_x34():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t000001300_x35():
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000001300_x40()
    """State 9"""
    return 0

def t000001300_x36():
    """State 0,1"""
    assert t000001300_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000)
                
    """State 4"""
    return 0

# Time Selection
def t000001300_x40():
    c1110()
    
    while True:
        ClearTalkListData()

        # Clear Adjustment
        AddTalkListData(5, 80101006, -1)
        
        # Randomise Time
        AddTalkListData(1, 80101005, -1)
        
        # Force Day
        AddTalkListData(2, 80101002, -1)
        
        # Force Noon
        AddTalkListData(3, 80101003, -1)
        
        # Force Night
        AddTalkListData(4, 80101004, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Randomise Time
        if GetTalkListEntryResult() == 1:
            call = t000001300_x50(80101010)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 1)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Force Day
        elif GetTalkListEntryResult() == 2:
            call = t000001300_x50(80101011)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 1)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Force Noon
        elif GetTalkListEntryResult() == 3:
            call = t000001300_x50(80101012)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 1)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Force Night
        elif GetTalkListEntryResult() == 4:
            call = t000001300_x50(80101013)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 1)
            elif call.Get() == 1:
                pass
            return 0
        # Clear Adjustment
        elif GetTalkListEntryResult() == 5:
            call = t000001300_x50(80101014)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
        assert CheckSpecificPersonTalkHasEnded(0) == 1
            
# Utility
def t000001300_x50(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0