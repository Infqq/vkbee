def event_flags_get(number)
    if number == 1:
        return 'REPLACE_MESSAGE_FLAGS'
    if number == 2:
        return 'SET_MESSAGE_FLAGS'
    if number == 3:
        return 'RESET_MESSAGE_FLAGS'
    if number == 4:
        return 'ADD_NEW_MESSAGE'
    if number == 5:
        return 'EDIT_MESSAGE'
    if number == 6:
        return 'INCOMING_MESSAGE_READ'
    if number == 7:
        return 'OUTCOMING_MESSAGE_READ'
    if number == 8:
        return 'FRIEND_ONLINE'
    if number == 9:
        return 'FRIEND_OFFLINE'
    if number == 10:
        return 'RESET_MESSAGE_FLAGS2'
    if number == 11:
        return 'REPLACE_MESSAGE_FLAGS2'
    if number == 12:
        return 'SET_MESSAGE_FLAGS2'
    if number == 13:
        return 'DELETE_MESSAGE'
    if number == 14:
        return 'UNDO_DELETE_MESSAGE'
    if number == 20:
        return 'MAJOR_ID_CHANGED'
