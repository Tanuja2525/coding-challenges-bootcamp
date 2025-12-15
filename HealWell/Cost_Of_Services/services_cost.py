def get_selected(services, costs, indexes):
    sel_s = []
    sel_c = []
    for i in indexes:
        if i < len(services):
            sel_s.append(services[i])
            sel_c.append(costs[i])
    if not sel_s:
        raise ValueError("No valid services selected")
    return sel_s, sel_c
