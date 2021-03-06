if not no_dbus:
    class DbusObject(dbus.service.Object):

        @dbus.service.method("org.musicd.qmdc", in_signature='', out_signature='')
        def Next(self):
            qmdc.nextTrack()

        @dbus.service.method("org.musicd.qmdc", in_signature='', out_signature='')
        def Prev(self):
            qmdc.prevTrack()

        @dbus.service.method("org.musicd.qmdc", in_signature='', out_signature='')
        def Pause(self):
            qmdc.togglePause()
            
        @dbus.service.method("org.musicd.qmdc", in_signature='', out_signature='')
        def Stop(self):
            qmdc.stopTrack()

        @dbus.service.method("org.musicd.qmdc", in_signature='', out_signature='s')
        def NowPlaying(self):
            return qmdc.trackTitle + " by " + qmdc.trackArtist + " on " + qmdc.trackAlbum

