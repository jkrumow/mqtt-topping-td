def onValueChange(par, _):
    state = par.eval()
    if state is True:
        parent().ActivateClient()
    else:
        parent().DeactivateClient()
