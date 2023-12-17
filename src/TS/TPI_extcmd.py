from rp2 import StateMachine, asm_pio, PIO

def EXT_CMD(MQ: StateMachine):                                                     # External, used-defined command

    esc = MQ.put
    
    SEND_MSG(MQ, "User-definde command", "", 1)


@micropython.native
def SEND_MSG(MQ: StateMachine, msg, msg1, st: bytes):                              # Sends 'msg', 'msg1' to the TS, with 'st' status code

    esc = MQ.put

    esc(64)
    esc(129)
    esc(st)
    esc(13)
    for m in msg:
        esc(m)
    if msg1:
        esc(13)
        for m in msg1:
            esc(m)
    esc(0)
    
    return




EXT_LD_funct = {
    
    "TPI:EXTCMD" : EXT_CMD,
    }

EXT_SA_funct = {
    
    "TPI:EXTCMD" : EXT_CMD,
    }


