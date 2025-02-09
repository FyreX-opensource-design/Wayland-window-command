try:
    import dbus
except:
    pass

def getActiveWindowLinuxWayland():
    session_bus = dbus.SessionBus()
    
    try:
        # Access the XDG Desktop Portal
        proxy = session_bus.get_object("org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop")
        interface = dbus.Interface(proxy, "org.freedesktop.portal.Background")
        
        # Get active window information
        active_window = interface.Get("org.freedesktop.portal.ActiveWindow", "ActiveWindow")

        return active_window
    except Exception as e:
        return f"Error: {e}"