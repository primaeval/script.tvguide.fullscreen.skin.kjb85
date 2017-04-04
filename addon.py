import xbmc,xbmcgui,xbmcaddon

d = xbmcgui.Dialog()
ok = d.ok("TV Guide Fullscreen","Set this Skin as default?")
if ok:
    tvgf = xbmcaddon.Addon("script.tvguide.fullscreen")
    if tvgf:
        tvgf.setSetting('skin.source', '2')
        tvgf.setSetting('skin.folder', 'special://home/addons/script.tvguide.fullscreen.skin.kjb85/')
        tvgf.setSetting('skin.user', 'Skin')
        tvgf.setSetting('action.bar', 'false')
        tvgf.setSetting('epg.focus.color', '[COLOR ffffffff]white[/COLOR]')
        tvgf.setSetting('epg.nofocus.color', '[COLOR ffffffff]white[/COLOR]')
