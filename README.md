# win7-auto-rearmer

In Windows 7 you can use the `rearm` flag from `slmgr` to extend the time you can use it without activation. 
This *Python 3* script runs that command and attempts to increase the maximum times you can rearm (by default 3 times).

**Must run with administrator privileges.**

## Wallpaper changer

Beside the constant activation messages and the desktop wallpaper changing to a black color, there are no restrictions. The `wallpaper-changer` tool can be used to set the desktop wallpaper to another picture. It can be run automatically by setting up a scheduled task to execute the tool.

By default, the tool changes the wallpaper to the original Windows 7 wallpaper. Change the picture at `C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg` or recompile the tool with another path if you want a different picture.
