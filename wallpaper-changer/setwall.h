#ifndef _SETWALL_
#define _SETWALL_

#include <iostream>
#include <windows.h>

int changeBackground(const char* pathToImage) {

    wchar_t wcp[MAX_PATH];
    mbstowcs(wcp, pathToImage, strlen(pathToImage) + 1);
    LPWSTR imgPath = wcp;

    std::wcout<<"Changing background to: "<<imgPath<<std::endl;
    int spInfoRes = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgPath, SPIF_SENDCHANGE);

    return spInfoRes;
}

int changeBackground(LPWSTR pathToImage) {

    /* Convert from LPWSTR to char*
    char imgPathChar[MAX_PATH] = {0x0};
    wcstombs(imgPathChar, imgPath, wcslen(imgPath));
    */

    std::wcout<<"Changing background to: "<<pathToImage<<std::endl;
    int spInfoRes = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathToImage, SPIF_SENDCHANGE);

    return spInfoRes;
}

#endif /* _SETWALL_ */